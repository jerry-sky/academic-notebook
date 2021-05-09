package main

// Sender sends given list of messages one by one.
//
// This function is supposed to be run as a go-routine.
func Sender(input *Node, messages []*Message, maxSleep float64) {

	stash := input.stash

	quantity := len(messages)

	i := 0
	for {
		if i == quantity {
			break
		} else if len(stash) == 0 {
			// the channel is empty — we can input a new message
			stash <- messages[i]
			i++
		} else {
			// otherwise wait
			SleepForSomeTime(maxSleep)
		}
	}

}
