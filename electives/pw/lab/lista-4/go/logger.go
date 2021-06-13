package main

var loggerStash = make(chan string)

// LoggerDone indicates whether the logger has done printing all the messages.
var LoggerDone = make(chan bool)

var isClosed bool

// LogOfferAccepted logs a new accepted offer.
func LogOfferAccepted(offer *RoutingOffer, sender *Router, receiver *Router) {

	loggerStash <- "offer from node " + Str(sender.id) + " accepted by node " + Str(receiver.id) + ": found better path to node " + Str(offer.id) + " (cost " + Str(offer.currentCost) + "+1)"
}

// LogStandardMessageArrival logs arrival of a new standard message.
func LogStandardMessageArrival(message *StandardMessage) {

	l := "message " + Str(message.id) + " arrival: (" + Str(message.sender.router.id) + "," + Str(message.sender.id) + ")"
	l += " → (" + Str(message.receiver.router.id) + "," + Str(message.receiver.id) + ")"

	currentPathLength := len(message.visited)
	lastPathLength := message.lastPathLength
	if lastPathLength == -1 {
		// this is the first time this message was sent (there was no previous path)
		lastPathLength = currentPathLength
	}
	l += " visited " + Str(currentPathLength) + " routers: "
	for _, r := range message.visited {
		l += Str(r.id) + ","
	}

	if lastPathLength > currentPathLength {
		// the message used a shorter route
		l += "\n\x1b[1m  this is a shorter route than before (" + Str(lastPathLength) + ">" + Str(currentPathLength) + ")\x1b[0m"
	}

	loggerStash <- l
}

// LoggerPrintMessages starts receiving messages and printing them.
//
// This function is supposed to be run as a go-routine.
func LoggerPrintMessages() {

	isClosed = false

	for {
		if isClosed {
			pendingMessagesCount := len(loggerStash)
			for i := 0; i < pendingMessagesCount; i++ {
				msg := <-loggerStash
				println(msg)
			}
			break
		}

		var msg string
		msg = <-loggerStash
		println(msg)
	}

	LoggerDone <- true

}

// LoggerClose closes the logger after the last message has been printed.
func LoggerClose() {

	isClosed = true

}
