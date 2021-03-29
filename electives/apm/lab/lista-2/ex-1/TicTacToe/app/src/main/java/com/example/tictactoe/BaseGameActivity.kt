package com.example.tictactoe

import android.app.Activity
import android.content.Intent
import android.graphics.Point
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import com.example.tictactoe.gamelogic.GameLogic
import com.example.tictactoe.gamelogic.InvertibleMap
import com.example.tictactoe.gamelogic.Turn

abstract class BaseGameActivity : AppCompatActivity() {

    protected lateinit var game: GameLogic

    protected lateinit var buttonMap: InvertibleMap<Point, Int>

    protected abstract var turnText: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
    }

    fun click(button: View) {

        val turnBeforeClick = this.game.CurrentTurn

        val coordinates = this.buttonMap.getKey(button.id)
        val result = this.game.makeTurn(coordinates!!)

        if (!result) {
            return
        }

        if (turnBeforeClick == Turn.X) {
            (button as Button).text = getString(R.string.button_x)
        } else {
            (button as Button).text = getString(R.string.button_o)
        }

        val turn = this.game.CurrentTurn
        val winner = this.game.Winner

        if (winner == null) {
            if (turn == Turn.X) {
                this.turnText.text = getString(R.string.turn_x)
            } else {
                this.turnText.text = getString(R.string.turn_o)
            }
        } else {
            val intent = Intent()
            intent.putExtra("winner", winner.toString())
            this.setResult(Activity.RESULT_OK, intent)
            finish()
        }
    }
}
