package main

import "strconv"

var loggerStash = make(chan string)

// LoggerDone will be notified when the logger is done with printing all pending messages.
var LoggerDone = make(chan bool)

func registerVisit(msg *Message, node *Node) {
	msg.visited = append(msg.visited, node)
	node.seen = append(node.seen, msg)
}

// LogReceivingMessage logs the event of receiving a new message.
func LogReceivingMessage(msg *Message, receiver *Node) {

	loggerStash <- "\033[1mreceived message ‘" + msg.contents + "’\033[0m"

}

// LogMessageInTransit logs the event of a message arriving to a given node.
func LogMessageInTransit(msg *Message, receiver *Node) {

	loggerStash <- "message ‘" +
		msg.contents +
		"’ arrived at node ‘" +
		strconv.Itoa(receiver.id) +
		"’"

	registerVisit(msg, receiver)

}

// LogMessageDeath logs the event of a message running out of health.
func LogMessageDeath(msg *Message, receiver *Node) {

	loggerStash <- "\033[1mmessage ‘" +
		msg.contents +
		"’ was pronounced \033[3mdead\033[0;1m at node ‘" +
		strconv.Itoa(receiver.id) +
		"’\033[0m"

}

// LoggerPrintMessages prints every message it receives immediately.
//
// This function should be run as a Go routine.
func LoggerPrintMessages() {

	for {
		if loggerStash == nil {
			break
		}

		msg := <-loggerStash
		println(msg)
	}

	LoggerDone <- true

}

// LoggerClose closes the logger stash and causes the logger to shut down.
func LoggerClose() {

	close(loggerStash)
	loggerStash = nil

}
