package main

// Awaits for a given number of messages.
//
// This function is supposed to be run as a go-routine.
func receiver(output *Node, quantity int, maxSleep float64, deathLog chan bool) []*Message {

	receivedSoFar := 0

	messages := make([]*Message, 0)

	for {
		select {
		case <-deathLog:
			// count every death as ‘received’ for simplicity’s sake
			receivedSoFar++
		case msg := <-output.stash:
			// receive the message
			LogMessageInTransit(msg, output)
			LogReceivingMessage(msg, output)

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
			// by default just sleep
			SleepForSomeTime(maxSleep)
		}
	}

}
