package main

import (
	"os"
	"strconv"
)

func main() {

	argv := os.Args

	if len(argv) < 7 {
		println("necessary arguments: ‹n› ‹d› ‹b› ‹k› ‹h› ‹maxSleep›")
		return
	}

	errors := make([]error, len(argv))
	errors[0] = nil

	var n, d, b, k, h, _maxSleep, plundererInterval int

	n, errors[1] = strconv.Atoi(argv[1])
	d, errors[2] = strconv.Atoi(argv[2])
	b, errors[3] = strconv.Atoi(argv[3])
	k, errors[4] = strconv.Atoi(argv[4])
	h, errors[5] = strconv.Atoi(argv[5])
	_maxSleep, errors[6] = strconv.Atoi(argv[6])
	if len(argv) > 7 {
		plundererInterval, errors[7] = strconv.Atoi(argv[7])
	} else {
		plundererInterval = 0
	}

	for _, err := range errors {
		if err != nil {
			println("all arguments need to be integer numbers")
			return
		}
	}

	// increase the max health by one as the first ‘step’ of placing
	// a message on the first node does not count as a ‘step’
	h++

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

	// a list of all entries for the plunderer
	// the plunderer can set up a trap using one of these channels
	// to inform given node of the trap that needs setting up
	plundererPointsOfEntry := make([]chan bool, n)

	// start up all nodes
	for i, node := range vertices {
		// allow the plunderer for setting up traps
		plundererPointsOfEntry[i] = make(chan bool, 1)
		if i != n-1 {
			go NodeRoutine(node, maxSleep, deathLog, plundererPointsOfEntry[i])
		}
	}

	// the first node
	input := vertices[0]

	// generate all messages
	messages := make([]*Message, k)
	for i := 0; i < k; i++ {
		// compose the message
		msg := &Message{
			contents: strconv.Itoa(i + 1),
			visited:  make([]*Node, 0),
			health:   h,
		}
		// add the message
		messages[i] = msg
	}

	// start sending the messages
	go Sender(input, messages, maxSleep)

	// set up the plunderer
	stopPlundering := make(chan bool, 1)
	if plundererInterval != 0 {
		println("\033[3mplunderer active\033[0m\n")
		go PlundererRoutine(plundererPointsOfEntry, stopPlundering, maxSleep*float64(plundererInterval))
	}

	// the last node
	output := vertices[n-1]

	// start receiving the messages
	Receiver(output, k, maxSleep, deathLog)

	// stop the plunderer
	stopPlundering <- true

	// wait for the logger to finish printing all the messages
	<-LoggerDone

	// print the stats
	println("\n\033[1mStats\033[0m (chronological order):")
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
