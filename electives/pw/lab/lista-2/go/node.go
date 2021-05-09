package main

// NodeRoutine takes care of all the work being done by a single vertice in the graph.
//
// Arguments:
//
// `node *Node`: the node that this function is operating on
//
// `maxSleep float64`: maximum number of milliseconds of sleep
//
// `deathLog chan bool`: if a message dies either of exhaustion (health = 0) or trap death
// the node send a notification about its death
//
// `plundererPointOfEntry chan bool`: plunderer can setup a trap sending a notification using this channel
//
// `output chan *Message`: last node only — the output channel to notify the receiver about message’s arrival
//
// It is supposed to be run as a go-routine.
func NodeRoutine(node *Node, maxSleep float64, deathLog chan bool, plundererPointOfEntry chan bool, output chan *Message) {

	trapActive := false

	// keep listening for messages
	for {
		select {
		// get the latest message
		case msg := <-node.stash:

			// log message’s arrival
			LogMessageInTransit(msg, node)

			if trapActive {
				// the message has been captured by the plunderer’s trap
				LogMessageTrapDeath(msg, node)
				deathLog <- true
				// deactivate the trap back
				trapActive = false
				// destroy the message
				continue
			}

			// take a break
			SleepForSomeTime(maxSleep)

			if output != nil {
				// special case — this node is the last node
				// receive the message
				LogReceivingMessage(msg, node)
				output <- msg
				// message has been passed to the receiver
				continue
			}

			// decrease message’s health
			msg.health--

			if msg.health == 0 {
				// stop message propagation if the message health is equal to zero
				LogMessageExhaustion(msg, node)
				// inform the receiver as well
				deathLog <- true
				// message has exhausted its health
				continue
			}

			// pick a random neighbouring vertice to send the message to
			neighbours := node.neighbours
			target := neighbours[RandomInteger(len(neighbours))].stash
			// send the message when it is possible
			target <- msg

		case <-plundererPointOfEntry:
			// the plunderer wants to setup a trap for the next message that arrives
			trapActive = true
		default:
			// or sleep for some time
			SleepForSomeTime(maxSleep)
		}
	}

}
