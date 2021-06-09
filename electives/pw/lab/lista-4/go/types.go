package main

import "strconv"

// RoutingOffer represents a one offer of improving the cost of the path to some
// other node of ID equal to `id`.
type RoutingOffer struct {
	id          int
	currentCost int
}

// RoutingMessage holds an array of offers coming from a given node.
type RoutingMessage struct {
	contents []*RoutingOffer
	sender   *Router
}

// RoutingTable table containing the currently discovered topology of the network.
type RoutingTable struct {
	cost    []int
	nexthop []*Router
	changed []bool
}

// StandardMessage is a ping message sent between two hosts (clients).
type StandardMessage struct {
	sender         *Host
	receiver       *Host
	visited        []*Router
	lastPathLength int
	id             int
}

// Host is a client that uses one Node as a router to send messages.
type Host struct {
	router        *Router
	id            int
	standardStash chan *StandardMessage
}

// Router holds all information about one vertice in the graph.
type Router struct {
	// The channel where the go-routines send to and receive from the messages.
	routingStash  chan *RoutingMessage
	standardStash chan *StandardMessage
	neighbours    []*Router
	id            int
	routing       *RoutingTable
	clients       []*Host
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

func Str(i int) string {
	return strconv.Itoa(i)
}
