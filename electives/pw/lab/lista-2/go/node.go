package main

// Takes care of all the work being done by a single vertice in the graph.
//
// It is supposed to be run as a go-routine.
func runVertice(node *Node, maxSleep float64, deathLog chan bool) {

	// keep listening for messages
	for {
		select {
		// get the latest message
		case msg := <-node.stash:
			// take a break
			SleepForSomeTime(maxSleep)

			// decrease message’s health
			msg.health--

			// log message’s arrival
			LogMessageInTransit(msg, node)

			// stop message propagation if the message health is equal to zero
			if msg.health == 0 {
				LogMessageDeath(msg, node)
				// inform the receiver as well
				deathLog <- true
				continue
			}

			// pick a random neighbouring vertice to send the message to
			neighbours := node.neighbours
			target := neighbours[RandomInteger(len(neighbours))].stash

			// send the message when it is possible
			target <- msg

		// or sleep for some time
		default:
			SleepForSomeTime(maxSleep)
		}
	}

}
