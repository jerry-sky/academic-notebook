package com.example.ordnung

import android.os.Bundle
import android.os.Handler
import android.os.Looper
import android.view.View
import android.widget.Button
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity
import androidx.core.content.ContextCompat
import com.example.ordnung.databinding.ActivityMainBinding
import java.util.*

class MainActivity : AppCompatActivity() {
    private var binding: ActivityMainBinding? = null
    private var buttonsList: InvertibleMap<ButtonMatrix, Button>? = null

    /**
     * The current combination.
     */
    private var currentOrdnung: MutableList<ButtonMatrix> = mutableListOf<ButtonMatrix>()

    /**
     * The ID of what the user should input next.
     */
    private var expectedOrdnungElement = 0
    private var blinkColour = 0
    private var defaultColour = 0

    /**
     * Duration of each color blink.
     */
    private val blinkDuration = 750L
    private var highScore = -1
    private val handler: Handler? = Handler(Looper.getMainLooper())
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        val view: View = binding!!.root
        setContentView(view)
        blinkColour = ContextCompat.getColor(baseContext, R.color.teal_200)
        defaultColour = ContextCompat.getColor(baseContext, R.color.purple_200)
        val b = binding!!
        val tmp: HashMap<ButtonMatrix, Button> = HashMap<ButtonMatrix, Button>()
        tmp[ButtonMatrix.SE] = b.buttonSouthEast
        tmp[ButtonMatrix.S] = b.buttonSouth
        tmp[ButtonMatrix.SW] = b.buttonSouthWest
        tmp[ButtonMatrix.E] = b.buttonEast
        tmp[ButtonMatrix.C] = b.buttonCenter
        tmp[ButtonMatrix.W] = b.buttonWest
        tmp[ButtonMatrix.NE] = b.buttonNorthEast
        tmp[ButtonMatrix.N] = b.buttonNorth
        tmp[ButtonMatrix.NW] = b.buttonNorthWest
        buttonsList = InvertibleMap(tmp)

        // get the first random combination
        startOver()
    }

    /**
     * Reset the state of the game and begin with a new sequence.
     */
    private fun startOver() {
        // disable the buttons before the game (re)starts
        disableButtons()
        if (highScore != -1) {
            // score at the end of the round
            var roundScore = currentOrdnung.size - 1
            if (roundScore == 2) {
                // the Ordnung length was three, witch means the user did not score anything
                roundScore = 0
            }
            // this is at least the second game
            // `this.highScore` equal to negative one means that this is the first game, so no toasts should show up
            if (roundScore > highScore) {
                // save the new high score
                highScore = currentOrdnung.size - 1
                val toast = Toast.makeText(
                    applicationContext,
                    "You beat the high score! ($highScore)",
                    Toast.LENGTH_SHORT
                )
                toast!!.show()
            } else {
                // notify the user he failed to beat the high score
                val toast = Toast.makeText(
                    applicationContext,
                    "You did not beat the high score of $highScore. Your score was $roundScore.",
                    Toast.LENGTH_SHORT
                )
                toast!!.show()
            }
        } else {
            highScore = 0
        }

        // (re)populate die Ordnung
        currentOrdnung = mutableListOf<ButtonMatrix>()
        currentOrdnung.add(ButtonMatrix.GetRandom())
        currentOrdnung.add(ButtonMatrix.GetRandom())
        currentOrdnung.add(ButtonMatrix.GetRandom())
        // reset
        expectedOrdnungElement = 0
        // show the Ordnung
        handler!!.postDelayed(
            { showCurrentOrdnung() },  // for some reason `this::showCurrentOrdnung` breaks the program
            2000
        )
    }

    private fun expandOrdnung() {
        currentOrdnung.add(ButtonMatrix.GetRandom())
        showCurrentOrdnung()
        expectedOrdnungElement = 0
    }

    private fun showCurrentOrdnung() {
        // turn off all the buttons
        disableButtons()
        // blink each of the buttons for a second
        for (i in currentOrdnung.indices) {
            val el: ButtonMatrix = currentOrdnung[i]
            val button: Button? = buttonsList!!.getObj(el)
            handler!!.postDelayed({
                // blink
                button!!.setBackgroundColor(blinkColour)
            }, blinkDuration * i.toLong())
            handler.postDelayed({
                    // get back to the original colour
                    button!!.setBackgroundColor(defaultColour)
                },
                blinkDuration * (i + 1) - (0.2 * blinkDuration).toLong()
            )
        }
        handler!!.postDelayed({
            // turn back on all the buttons
            enableButtons()
        }, blinkDuration * currentOrdnung.size.toLong())
    }

    private fun handleUserInput(input: ButtonMatrix?) {
        if (input === currentOrdnung[expectedOrdnungElement]) {
            // correct
            // get next
            expectedOrdnungElement++
            // and if the user has reached the end of the current Ordnung, expand it
            if (expectedOrdnungElement == currentOrdnung.size) {
                expandOrdnung()
            }
        } else {
            // incorrect
            // start over
            startOver()
        }
    }

    fun button(view: View?) {
        handleUserInput(buttonsList!!.getKey(view as Button))
    }

    private fun disableButtons() {
        buttonsList!!.forEach { (_, button) -> button.isClickable = false }
    }

    private fun enableButtons() {
        buttonsList!!.forEach { (_, button) -> button.isClickable = true }
    }
}
