package main

// PlundererRoutine sets up traps for messages to be captured.
//
// This function is supposed to be run as a go-routine.
func PlundererRoutine(pointsOfEntry []chan bool, stopPlundering chan bool, maxSleep float64) {

	n := len(pointsOfEntry)

	for {
		select {
		case <-stopPlundering:
			break
		default:
			// take a break
			SleepForSomeTime(maxSleep)

			// pick a node
			targetIndex := RandomInteger(n)
			target := pointsOfEntry[targetIndex]

			// set up the trap
			target <- true
		}
	}

}
