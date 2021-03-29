package com.example.hangman

import android.util.Log
import kotlin.random.Random

class GameBase {

    private var chosenWord: String
    var chosenWordState: StringBuilder
        private set
    var wrongGuessesLeft: Int
        private set

    constructor(words: Array<String>, maxWrongGuesses: Int) {
        this.wrongGuessesLeft = maxWrongGuesses
        // pick a word
        val index = Random.nextInt(0, words.size)
        this.chosenWord = words[index]

        // populate the public version of the word
        this.chosenWordState = StringBuilder("")
        for (i in this.chosenWord.indices) {
            this.chosenWordState.append("?")
        }
    }

    fun guessLetter(letter: Char): Boolean {
        var guessed = false
        for (i in this.chosenWord.indices) {
            if (this.chosenWord[i] == letter) {
                this.chosenWordState[i] = this.chosenWord[i]
                guessed = true
            }
        }
        if (!guessed) {
            this.wrongGuessesLeft--
        }
        return guessed
    }

    fun evaluate(): Boolean {
        if (this.chosenWord == this.chosenWordState.toString()) {
            return true
        }
        return false
    }

}
