package main

// Awaits for a given number of messages.
//
// This function is supposed to be run as a go-routine.
func receiver(output *Node, quantity int) []*Message {

	receivedSoFar := 0

	messages := make([]*Message, 0)

	for {
		// finish after all the messages have arrived
		if receivedSoFar == quantity {
			// close the logger
			LoggerClose()
			return messages
		}
		// receive the message
		msg := <-output.stash
		LogMessageInTransit(msg, output)
		LogReceivingMessage(msg, output)

		messages = append(messages, msg)

		// count the messages
		receivedSoFar++
	}

}
