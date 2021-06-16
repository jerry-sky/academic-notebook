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
	standardStash *UnboundedChannelSM
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

// Str converts an integer to a string.
func Str(i int) string {
	return strconv.Itoa(i)
}

// UnboundedChannelSM is a `chan` with unlimited buffer.
type UnboundedChannelSM struct {
	input  chan *StandardMessage
	output chan *StandardMessage
}

// UnboundedChannelSMTask is a utility function for the UnboundedChannelSM struct
// — see UnboundedChannelSM struct.
//
// This function is supposed to be run as a go-routine.
func unboundedChannelSMTask(self *UnboundedChannelSM) {

	stash := make([]*StandardMessage, 0)
	var awaiting *StandardMessage
	awaiting = nil

	for {
		ls := len(stash)
		if awaiting == nil && ls > 0 {
			awaiting, stash = stash[ls-1], stash[:ls-1]
		}
		select {
		case incoming := <-self.input:
			stash = append(stash, incoming)
		default:
			if awaiting != nil {
				select {
				case self.output <- awaiting:
					awaiting = nil
				default:
				}
			}
		}
	}
}

// MakeUnboundedChannelSM creates a new unbounded channel that can receive (theoretically) unlimited quantity
// of `*StandardMessage`–s.
func MakeUnboundedChannelSM() *UnboundedChannelSM {

	self := &UnboundedChannelSM{
		input:  make(chan *StandardMessage, 1),
		output: make(chan *StandardMessage, 1),
	}

	go unboundedChannelSMTask(self)

	return self
}
