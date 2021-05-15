package com.example.discorde

const val FIREBASE_REALTIME_REF =
    "https://discorde-uni-assignment-default-rtdb.europe-west1.firebasedatabase.app/"

const val FRB_MESSAGES_REF = "messages"

data class Message(
    val contents: String,
    val author: String,
    val uid: String,
) {
    constructor() : this("", "", "")
}
