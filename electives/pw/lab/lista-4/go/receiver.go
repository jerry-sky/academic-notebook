package main

// Receiver awaits for any messages containing RIP topology upgrades offers.
//
// This function is supposed to be run as a go-routine.
func Receiver(self *Router, n int) {

	routing := self.routing

	for {
		message := <-self.routingStash

		// apply all offers
		for _, offer := range message.contents {
			newcost := 1 + offer.currentCost
			id := offer.id

			if newcost < routing.cost[id] {
				LogOfferAccepted(offer, message.sender, self)
				routing.cost[id] = newcost
				routing.nexthop[id] = message.sender
				routing.changed[id] = true
			}
		}
	}

}
