package main

import (
	"os"
	"strconv"
)

func main() {

	argv := os.Args

	if len(argv) < 4 {
		println("necessary arguments: ‹n› ‹d› ‹b› ‹k› ‹h› ‹maxSleep›")
		return
	}

	n, err1 := strconv.Atoi(argv[1])
	d, err2 := strconv.Atoi(argv[2])
	b, err3 := strconv.Atoi(argv[3])
	k, err4 := strconv.Atoi(argv[4])
	h, err5 := strconv.Atoi(argv[5])
	_maxSleep, err6 := strconv.Atoi(argv[4])

	if err1 != nil || err2 != nil || err3 != nil || err4 != nil || err5 != nil || err6 != nil {
		println("all arguments need to be integer numbers")
		return
	}

	maxSleep := float64(1.0) / float64(_maxSleep)

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
	// remember already made shortcuts
	shortcuts := make(map[string]bool, d)
	edgeTag := func(one int, two int) string {
		return strconv.Itoa(one) + " → " + strconv.Itoa(two)
	}

	for i := 0; i < d; i++ {

		// pick some two vertices
		oneIndex := RandomInteger(n)
		twoIndex := RandomInteger(n)

		// swap if necessary
		if oneIndex > twoIndex {
			oneIndex, twoIndex = twoIndex, oneIndex
		}
		// if the edge leads to the same vertice then skip
		// if the edge already exists, then skip
		if oneIndex == twoIndex || shortcuts[edgeTag(oneIndex, twoIndex)] {
			i--
			continue
		}
		one := vertices[oneIndex]
		two := vertices[twoIndex]

		// remember that shortcut
		shortcuts[edgeTag(oneIndex, twoIndex)] = true

		one.neighbours = append(one.neighbours, two)

	}

	// print the shortcut edges
	println("shortcuts:")
	for edge := range shortcuts {
		println(edge)
	}
	println()

	// generate detours between random graph vertices
	// remember already made detours
	detours := make(map[string]bool, b)

	for i := 0; i < b; i++ {

		// pick some two vertices
		oneIndex := RandomInteger(n)
		twoIndex := RandomInteger(n)

		// swap if necessary
		if oneIndex < twoIndex {
			oneIndex, twoIndex = twoIndex, oneIndex
		}
		// if the edge leads to the same vertice then skip
		// if the edge already exists, then skip
		if oneIndex == twoIndex || detours[edgeTag(oneIndex, twoIndex)] {
			i--
			continue
		}
		one := vertices[oneIndex]
		two := vertices[twoIndex]

		// remember that detour
		detours[edgeTag(oneIndex, twoIndex)] = true

		one.neighbours = append(one.neighbours, two)

	}

	// print all detours
	println("detours:")
	for edge := range detours {
		println(edge)
	}
	println()

	// start listening for log messages
	go LoggerPrintMessages()

	// register all messages’ deaths
	deathLog := make(chan bool)

	// start up all nodes
	for i, node := range vertices {
		if i != n-1 {
			go runVertice(node, maxSleep, deathLog)
		}
	}

	input := vertices[0]

	// start sending the messages
	go sender(input, k, maxSleep, h)

	output := vertices[n-1]

	// start receiving the messages
	messages := receiver(output, k, maxSleep, deathLog)

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
