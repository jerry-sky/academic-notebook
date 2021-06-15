package main

// HostTask sends standard messages addressed to other hosts using the router network.
//
// This function is supposed to be run as a go-routine.
func HostTask(self *Host, nodes []*Router, maxSleep float64, possibleIDs chan int) {

	// pick a random router
	c := nodes[RandomInteger(len(nodes))].clients
	cc := len(c)
	// with at least one host
	for cc == 0 {
		c = nodes[RandomInteger(len(nodes))].clients
		cc = len(c)
	}
	// pick a random host
	target := c[RandomInteger(cc)]

	// generate a new standard message
	message := &StandardMessage{
		sender:         self,
		receiver:       target,
		visited:        make([]*Router, 0),
		lastPathLength: -1,
		// pick an ID from the ID pool
		id: <-possibleIDs,
	}

	// send the message out
	self.router.standardStash.input <- message

	for {
		// now listen for any incoming messages and pong back
		incoming := <-self.standardStash

		// acknowledge the message
		LogStandardMessageArrival(incoming)

		// prepare a pong message
		outgoing := &StandardMessage{
			sender:         self,
			receiver:       incoming.sender,
			visited:        make([]*Router, 0),
			lastPathLength: len(incoming.visited),
			id:             incoming.id,
		}

		// hang on for a bit
		SleepForSomeTime(maxSleep)

		// send it out
		self.router.standardStash.input <- outgoing
	}

}
