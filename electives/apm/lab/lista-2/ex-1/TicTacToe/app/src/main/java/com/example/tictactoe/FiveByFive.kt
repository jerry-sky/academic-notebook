package com.example.tictactoe

import android.graphics.Point
import android.os.Bundle
import android.widget.TextView
import com.example.tictactoe.gamelogic.GameLogic
import com.example.tictactoe.gamelogic.InvertibleMap
import com.example.tictactoe.databinding.ActivityFiveByFiveBinding

class FiveByFive : BaseGameActivity() {

    override lateinit var turnText: TextView
    lateinit var binding: ActivityFiveByFiveBinding

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_five_by_five)

        this.game = GameLogic(5)

        this.turnText = findViewById(R.id.turnTextFive)

        this.binding = ActivityFiveByFiveBinding.inflate(layoutInflater)
        val b = this.binding

        // map the buttons to the squares (nodes) in the game
        val tmp = HashMap<Point, Int>()
        // tedious — yes, but we’re doing it only once, and it is nice
        // to have a list that explicitly maps coordinates to specific buttons
        tmp[Point(0, 0)] = b.button10.id
        tmp[Point(1, 0)] = b.button11.id
        tmp[Point(2, 0)] = b.button12.id
        tmp[Point(3, 0)] = b.button13.id
        tmp[Point(4, 0)] = b.button14.id
        tmp[Point(0, 1)] = b.button15.id
        tmp[Point(1, 1)] = b.button16.id
        tmp[Point(2, 1)] = b.button17.id
        tmp[Point(3, 1)] = b.button18.id
        tmp[Point(4, 1)] = b.button19.id
        tmp[Point(0, 2)] = b.button20.id
        tmp[Point(1, 2)] = b.button21.id
        tmp[Point(2, 2)] = b.button22.id
        tmp[Point(3, 2)] = b.button23.id
        tmp[Point(4, 2)] = b.button24.id
        tmp[Point(0, 3)] = b.button25.id
        tmp[Point(1, 3)] = b.button26.id
        tmp[Point(2, 3)] = b.button27.id
        tmp[Point(3, 3)] = b.button28.id
        tmp[Point(4, 3)] = b.button29.id
        tmp[Point(0, 4)] = b.button30.id
        tmp[Point(1, 4)] = b.button31.id
        tmp[Point(2, 4)] = b.button32.id
        tmp[Point(3, 4)] = b.button33.id
        tmp[Point(4, 4)] = b.button34.id
        this.buttonMap = InvertibleMap(tmp)
    }
}
