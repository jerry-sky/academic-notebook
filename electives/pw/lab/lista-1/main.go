package main

import (
	"os"
	"strconv"
)

// Takes care of all the work being done by a single vertice in the graph.
//
// It is supposed to be run as a go-routine.
func runVertice(node *Node) {

	// keep listening for messages
	for {
		select {
		// get the latest message
		case msg := <-node.stash:
			// take a break
			SleepForSomeTime()

			// log message’s arrival
			LogMessageInTransit(msg, node)

			// pick a random neighbouring vertice to send the message to
			neighbours := node.neighbours
			target := neighbours[RandomInteger(len(neighbours))].stash

			// send the message when it is possible
			target <- msg

		// or sleep for some time
		default:
			SleepForSomeTime()
		}
	}

}

func main() {

	argv := os.Args

	if len(argv) < 4 {
		println("necessary arguments: n d k")
		return
	}

	n, err1 := strconv.Atoi(argv[1])
	d, err2 := strconv.Atoi(argv[2])
	k, err3 := strconv.Atoi(argv[3])

	if err1 != nil || err2 != nil || err3 != nil {
		println("all arguments need to be integer numbers")
		return
	}

	vertices := make([]*Node, n)

	// generate all graph vertices
	for i := 0; i < n; i++ {

		// generate a list of neighbours
		neighbours := make([]*Node, 0)

		// each vertice contains a channel to keep the messages during transit
		// and a list of neighbouring vertices
		vertices[i] = &Node{
			stash:      make(chan *Message, 1),
			neighbours: neighbours,
			id:         i,
		}

		// create an edge between this newly created node and the previous one
		if i != 0 {
			previous := vertices[i-1]
			previous.neighbours = append(previous.neighbours, vertices[i])
		}

	}

	// generate shortcuts between random graph vertices
	for i := 0; i < d; i++ {

		// pick some two vertices
		oneIndex := RandomInteger(n)
		twoIndex := RandomInteger(n)

		// swap if necessary
		if oneIndex > twoIndex {
			oneIndex, twoIndex = twoIndex, oneIndex
		}
		// if the edge leads to the same vertice then skip
		if oneIndex == twoIndex {
			i--
			continue
		}
		one := vertices[oneIndex]
		two := vertices[twoIndex]

		one.neighbours = append(one.neighbours, two)

	}

	// print the graph
	graph := make(Columns, 0)
	graph.PrintGraph(vertices)

	// start listening for log messages
	go LoggerPrintMessages()

	// start up all nodes
	for i, node := range vertices {
		if i != n-1 {
			go runVertice(node)
		}
	}

	input := vertices[0]

	// start sending the messages
	go sender(input, k)

	output := vertices[n-1]

	// start receiving the messages
	messages := receiver(output, k)

	// wait for the logger to finish printing all the messages
	<-LoggerDone

	// print the stats
	println("\n\033[1mStats:\033[0m\n")
	for _, node := range vertices {
		println("node", node.id, "seen:")
		for _, msg := range node.seen {
			println("message ‘" + msg.contents + "’")
		}
		println()
	}

	for _, msg := range messages {
		println("message ‘" + msg.contents + "’ visited:")
		for _, node := range msg.visited {
			println("node", node.id)
		}
		println()
	}

}
