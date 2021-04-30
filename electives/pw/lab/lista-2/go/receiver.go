package main

// Receiver awaits for a given number of messages.
//
// Arguments:
//
// `output chan *Message`: the channel that is the output of the final node
//
// `quantity int`: expected number of messages (actual number of messages may differ, see below)
//
// `maxSleep float64`: the maximum number of milliseconds of sleep
//
// `deathLog chan bool`: channel used to get information about messages’ deaths
//
// Returns all received messages that have made it to the `output *Node`.
//
// This function is supposed to be run as a go-routine.
func Receiver(output chan *Message, quantity int, maxSleep float64, deathLog chan bool) []*Message {

	receivedSoFar := 0

	messages := make([]*Message, 0)

	for {
		select {
		case <-deathLog:
			// count every death as ‘received’ for simplicity’s sake
			receivedSoFar++
		case msg := <-output:
			// receive the message
			messages = append(messages, msg)
			// count the messages
			receivedSoFar++
		default:
			// finish after all the messages have arrived
			if receivedSoFar == quantity {
				// close the logger
				LoggerClose()
				return messages
			}
		}
	}

}
