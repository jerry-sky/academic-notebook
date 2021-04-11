package main

import "strconv"

var loggerStash = make(chan string)

var LoggerDone = make(chan bool)

func registerVisit(msg *Message, node *Node) {
	msg.visited = append(msg.visited, node)
	node.seen = append(node.seen, msg)
}

// Logs the event of receiving a new message.
func LogReceivingMessage(msg *Message, receiver *Node) {

	loggerStash <- "\033[1mreceived message ‘" + msg.contents + "’\033[0m"

}

// Logs the event of a message arriving to a given node.
func LogMessageInTransit(msg *Message, receiver *Node) {

	loggerStash <- "message ‘" + msg.contents + "’ arrived at node ‘" + strconv.Itoa(receiver.id) + "’"
	registerVisit(msg, receiver)

}

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

func LoggerClose() {

	close(loggerStash)
	loggerStash = nil

}
