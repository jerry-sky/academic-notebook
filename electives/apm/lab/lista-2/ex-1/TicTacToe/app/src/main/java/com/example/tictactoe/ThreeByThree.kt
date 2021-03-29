package com.example.tictactoe

import android.graphics.Point
import android.os.Bundle
import android.widget.TextView
import com.example.tictactoe.gamelogic.GameLogic
import com.example.tictactoe.gamelogic.InvertibleMap
import com.example.tictactoe.databinding.ActivityThreeByThreeBinding

class ThreeByThree : BaseGameActivity() {

    override lateinit var turnText: TextView
    lateinit var binding: ActivityThreeByThreeBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_three_by_three)

        this.game = GameLogic(3)

        this.turnText = findViewById(R.id.turnTextThree)

        this.binding = ActivityThreeByThreeBinding.inflate(layoutInflater)
        val b = this.binding

        // map the buttons to the squares (nodes) in the game
        val tmp = HashMap<Point, Int>()
        // tedious — yes, but we’re doing it only once, and it is nice
        // to have a list that explicitly maps coordinates to specific buttons
        tmp[Point(0, 0)] = b.button1.id
        tmp[Point(1, 0)] = b.button2.id
        tmp[Point(2, 0)] = b.button3.id
        tmp[Point(0, 1)] = b.button4.id
        tmp[Point(1, 1)] = b.button5.id
        tmp[Point(2, 1)] = b.button6.id
        tmp[Point(0, 2)] = b.button7.id
        tmp[Point(1, 2)] = b.button8.id
        tmp[Point(2, 2)] = b.button9.id
        this.buttonMap = InvertibleMap(tmp)
    }

}
