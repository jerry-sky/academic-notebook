package com.example.tictactoe

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView
import com.example.tictactoe.gamelogic.Turn

class GameOverActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_game_over)

        val winner = intent.getStringExtra("winner")

        val textView = findViewById<TextView>(R.id.gameOverTextView)

        if(winner == Turn.X.toString()){
            textView.text = getString(R.string.winner_x)
        } else {
            textView.text = getString(R.string.winner_o)
        }
    }
}
