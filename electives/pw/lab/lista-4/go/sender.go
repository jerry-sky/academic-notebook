package main

// Sender sends some RIP topology improvement offers at random times.
//
// This function is supposed to be run as a go-routine.
func Sender(self *Router, n int, maxSleep float64) {

	routing := self.routing

	for {
		SleepForSomeTime(maxSleep)

		// compose a message containing all offers
		message := &RoutingMessage{
			contents: make([]*RoutingOffer, 0),
			sender:   self,
		}

		// based on the current state of the routing table generate some offers
		for j := 0; j < n; j++ {
			if routing.changed[j] {
				routing.changed[j] = false
				offer := &RoutingOffer{
					id:          j,
					currentCost: routing.cost[j],
				}
				message.contents = append(message.contents, offer)
			}
		}

		// broadcast the message to all neighbours
		for _, neighbour := range self.neighbours {
			neighbour.routingStash <- message
		}
	}
}
