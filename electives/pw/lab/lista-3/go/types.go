package main

// Offer represents a one offer of improving the cost of the path to some
// other node of ID equal to `id`.
type Offer struct {
	id          int
	currentCost int
}

// Message holds an array of offers coming from a given node.
type Message struct {
	contents []*Offer
	sender   *Node
}

// Routing table containing the currently discovered topology of the network.
type Routing struct {
	cost    []int
	nexthop []*Node
	changed []bool
}

// Node holds all information about one vertice in the graph.
type Node struct {
	// The channel where the go-routines send to and receive from the messages.
	stash      chan *Message
	neighbours []*Node
	id         int
	routing    *Routing
}

// Abs returns the absolute value of an `int`.
func Abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

// Sum reduces a list of booleans to a count of `true` values.
func Sum(arr ...bool) int {
	output := 0
	for _, val := range arr {
		if val {
			output++
		}
	}
	return output
}
