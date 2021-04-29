package main

import "strconv"

// Sends a given number of messages.
//
// This function is supposed to be run as a go-routine.
func sender(input *Node, quantity int, maxSleep float64, maxHealth int) {

	sentMessages := 0

	stash := input.stash

	for {
		// end the loop when all messages have been sent
		if sentMessages == quantity {
			break
		}

		if len(stash) == 0 {
			// the channel is empty — we can input a new message

			// compose the message
			msg := &Message{
				contents: strconv.Itoa(sentMessages + 1),
				visited:  make([]*Node, 0),
				health:   maxHealth,
			}

			// send the message
			stash <- msg

			sentMessages++

		} else {
			// otherwise wait
			SleepForSomeTime(maxSleep)
		}
	}

}
