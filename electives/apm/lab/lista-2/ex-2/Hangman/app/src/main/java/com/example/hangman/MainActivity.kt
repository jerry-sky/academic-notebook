package com.example.hangman

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.ImageView
import android.widget.TextView
import android.widget.Toast
import com.example.hangman.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    private lateinit var game: GameBase

    private val buttons = HashMap<Int, Char>()

    private lateinit var currentWordView: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        this.binding = ActivityMainBinding.inflate(layoutInflater)

        val b = this.binding
        this.buttons[b.buttonA.id] = 'a'
        this.buttons[b.buttonB.id] = 'b'
        this.buttons[b.buttonC.id] = 'c'
        this.buttons[b.buttonD.id] = 'd'
        this.buttons[b.buttonE.id] = 'e'
        this.buttons[b.buttonF.id] = 'f'
        this.buttons[b.buttonG.id] = 'g'
        this.buttons[b.buttonH.id] = 'h'
        this.buttons[b.buttonI.id] = 'i'
        this.buttons[b.buttonJ.id] = 'j'
        this.buttons[b.buttonK.id] = 'k'
        this.buttons[b.buttonL.id] = 'l'
        this.buttons[b.buttonM.id] = 'm'
        this.buttons[b.buttonN.id] = 'n'
        this.buttons[b.buttonO.id] = 'o'
        this.buttons[b.buttonP.id] = 'p'
        this.buttons[b.buttonQ.id] = 'q'
        this.buttons[b.buttonR.id] = 'r'
        this.buttons[b.buttonS.id] = 's'
        this.buttons[b.buttonT.id] = 't'
        this.buttons[b.buttonU.id] = 'u'
        this.buttons[b.buttonV.id] = 'v'
        this.buttons[b.buttonW.id] = 'w'
        this.buttons[b.buttonX.id] = 'x'
        this.buttons[b.buttonY.id] = 'y'
        this.buttons[b.buttonZ.id] = 'z'

        this.currentWordView = findViewById<TextView>(R.id.currentWordView)

        this.restartGame()
    }

    private fun restartGame() {
        this.game = GameBase(resources.getStringArray(R.array.words), 10)
        this.updateImage(10)
        this.currentWordView.text = this.game.chosenWordState.toString()
    }

    private fun updateImage(wrongGuessesLeft: Int) {
        val imageId = 10 - wrongGuessesLeft
        val imageIdentifier = resources.getIdentifier("hangman$imageId", "drawable", this.packageName)
        findViewById<ImageView>(R.id.hangmanImageView).setImageResource(imageIdentifier)
    }

    fun click(button: View) {

        val letter = this.buttons[(button as Button).id]!!
        val result = this.game.guessLetter(letter)
        if (!result) {
            this.updateImage(this.game.wrongGuessesLeft)
        }

        this.currentWordView.text = this.game.chosenWordState.toString()

        if (this.game.wrongGuessesLeft == 0) {
            Toast.makeText(applicationContext, getString(R.string.lost_message), Toast.LENGTH_SHORT).show()
            this.restartGame()
            return
        }

        if (this.game.evaluate()) {
            Toast.makeText(
                applicationContext,
                getString(R.string.won_message) + " (" + this.game.chosenWordState.toString() + ")", Toast.LENGTH_SHORT
            ).show()
            this.restartGame()
        }

    }
}
