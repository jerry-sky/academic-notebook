package main

import (
	"os"
	"strconv"
)

var done = make(chan bool, 1)

func main() {

	argv := os.Args

	if len(argv) < 4 {
		println("necessary arguments: n d maxSleep")
		return
	}

	n, err1 := strconv.Atoi(argv[1])
	d, err2 := strconv.Atoi(argv[2])
	_maxSleep, err3 := strconv.Atoi(argv[3])

	if err1 != nil || err2 != nil || err3 != nil {
		println("all arguments need to be integer numbers")
		return
	}

	maxSleep := float64(1.0) / float64(_maxSleep)

	nodes := make([]*Node, n)

	// generate all graph nodes
	for i := 0; i < n; i++ {

		routing := &Routing{
			// we only need `n-1`–sized arrays but it is more convienient this way,
			// having this universal direct ID-based access
			cost:    make([]int, n),
			nexthop: make([]*Node, n),
			changed: make([]bool, n),
		}

		current := &Node{
			stash:      make(chan *Message, 1),
			neighbours: make([]*Node, 0),
			id:         i,
			routing:    routing,
		}
		nodes[i] = current

		// create an edge between this newly created node and the previous one
		if i != 0 {
			previous := nodes[i-1]
			previous.neighbours = append(previous.neighbours, current)
			current.neighbours = append(current.neighbours, previous)
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

		// if the edge leads to the same vertice then skip
		// if the edge already exists, then skip
		if oneIndex == twoIndex || shortcuts[edgeTag(oneIndex, twoIndex)] {
			i--
			continue
		}
		one := nodes[oneIndex]
		two := nodes[twoIndex]

		// remember that shortcut
		shortcuts[edgeTag(oneIndex, twoIndex)] = true

		one.neighbours = append(one.neighbours, two)
		two.neighbours = append(two.neighbours, one)

	}

	// generate routing information based only on the main Hamilton path
	// consisting of edges {v, v+1}
	for i := 0; i < n; i++ {
		current := nodes[i]

		var previous *Node = nil
		if i > 0 {
			previous = nodes[i-1]
		}
		var next *Node = nil
		if i < n-1 {
			next = nodes[i+1]
		}

		for j := 0; j < n; j++ {
			// the case of routing from `i` to `i` is unnecessary (skip)
			if j == i {
				current.routing.changed[j] = false
				continue
			}

			current.routing.changed[j] = true
			current.routing.cost[j] = Abs(i - j)
			if i < j {
				current.routing.nexthop[j] = next
			} else { // i > j
				current.routing.nexthop[j] = previous
			}
		}
	}

	// generate routing information for the direct neighbours
	for i := 0; i < n; i++ {
		current := nodes[i]

		for _, neighbour := range current.neighbours {
			neighbourID := neighbour.id
			current.routing.cost[neighbourID] = 1
			current.routing.nexthop[neighbourID] = neighbour
		}
	}

	// print the graph
	println("shortcuts:")
	for edge := range shortcuts {
		println(edge)
	}
	println()

	// start listening for log messages
	go LoggerPrintMessages()

	go func() {
		for {
			currentState := 0
			for _, node := range nodes {
				currentState += Sum(node.routing.changed...)
			}

			if currentState == 0 {
				done <- true
			}

			SleepForSomeTime(maxSleep)
		}
	}()

	// start up all nodes
	for _, node := range nodes {
		go Sender(node, n, maxSleep)
		go Receiver(node, n)
	}

	// wait for all nodes to get to know the network fully
	<-done
	// notify the logger that the time has come
	LoggerClose()
	// wait for the logger
	<-LoggerDone

	// print the routing tables for all nodes
	println("\nrouting tables for all nodes")
	println("\x1b[1mformat: ‘next hop node id’ → ‘destination node id’ (cost)")
	println("    or: ‘next hop node id’ direct // for direct neighbours")
	println("\x1b[0m")
	for _, node := range nodes {
		println("node", node.id, "— routing table:")

		for j := 0; j < n; j++ {
			if j != node.id {
				nextHopID := node.routing.nexthop[j].id
				if nextHopID != j {
					println(" ", nextHopID, "→", j, "("+strconv.Itoa(node.routing.cost[j])+")")
				} else {
					println(" ", nextHopID, "direct")
				}
			}
		}

		println()
	}

}
