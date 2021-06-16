package main

// Forwarder passes along all standard messages.
//
// This function is supposed to be run as a go-routine.
func Forwarder(self *Router) {

	for {
		message := <-self.standardStash.output
		message.visited = append(message.visited, self)
		target := message.receiver

		if self == target.router {
			// the message has arrived at its destination router
			// now send the message over to the final recipient
			self.clients[target.id].standardStash <- message
		} else {
			// the message needs to be transmitted to another router
			self.routing.nexthop[target.router.id].standardStash.input <- message
		}
	}
}
