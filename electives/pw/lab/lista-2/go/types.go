package main

// Message represents the single piece of information that is sent through the graph.
type Message struct {
	contents string
	visited  []*Node
	health   int
}

// Node holds all information about one vertice in the graph.
type Node struct {
	// The channel where the go-routines send to and receive from the messages.
	stash      chan *Message
	neighbours []*Node
	id         int
	seen       []*Message
}
