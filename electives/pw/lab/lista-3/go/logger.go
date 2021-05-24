package main

import "strconv"

var loggerStash = make(chan string)

// LoggerDone indicates whether the logger has done printing all the messages.
var LoggerDone = make(chan bool)

// LogNewOffer logs a new offer of improving given path between two nodes.
func LogNewOffer(offer *Offer, sender *Node) {

	loggerStash <- "new offer from node " + strconv.Itoa(sender.id) + ": potentially better path to node " + strconv.Itoa(offer.id) + " (cost " + strconv.Itoa(offer.currentCost) + ")"
}

// LogOfferAccepted logs a new accepted offer.
func LogOfferAccepted(offer *Offer, sender *Node, receiver *Node) {

	loggerStash <- "\x1b[1moffer from node " + strconv.Itoa(sender.id) + " accepted by node " + strconv.Itoa(receiver.id) + ": found better path to node " + strconv.Itoa(offer.id) + " (cost " + strconv.Itoa(offer.currentCost) + "+1)\x1b[0m"
}

// LoggerPrintMessages starts receiving messages and printing them.
//
// This function is supposed to be run as a go-routine.
func LoggerPrintMessages() {

	isClosed := false

	for {
		if isClosed {
			for msg := range loggerStash {
				println(msg)
			}
			break
		}

		var msg string
		msg, isClosed = <-loggerStash
		println(msg)
	}

	LoggerDone <- true

}

// LoggerClose closes the logger after the last message has been printed.
func LoggerClose() {

	close(loggerStash)

}
