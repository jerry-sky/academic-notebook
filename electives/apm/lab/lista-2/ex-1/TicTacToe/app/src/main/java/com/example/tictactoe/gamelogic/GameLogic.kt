package com.example.tictactoe.gamelogic

import android.graphics.Point

class GameLogic {

    private val nodes: MutableList<Node?>
    private val size: Int

    var CurrentTurn: Turn
        private set
    var Winner: Turn?
        private set

    constructor(size: Int) {
        this.size = size
        // prepare the list of all nodes
        this.nodes = ArrayList(size * size)
        for (x in 0 until size * size) {
            this.nodes.add(null)
        }

        // begin game
        this.CurrentTurn = Turn.X
        this.Winner = null
    }

    fun makeTurn(point: Point): Boolean {
        return this.makeTurn(point.x, point.y)
    }

    fun makeTurn(x: Int, y: Int): Boolean {

        if (this.CurrentTurn == Turn.Done) {
            return false
        }

        val index = this.size * y + x

        if (this.nodes[index] == null) {
            this.nodes[index] = if (this.CurrentTurn == Turn.X) Node.X else Node.O
        } else {
            return false
        }

        val isDone = this.evaluate()

        if (isDone != null) {
            this.Winner = this.CurrentTurn
            this.CurrentTurn = Turn.Done
            return true
        }

        if (this.CurrentTurn == Turn.X) {
            this.CurrentTurn = Turn.O
        } else {
            this.CurrentTurn = Turn.X
        }

        return true

    }

    private fun evaluate(): Node? {
        // check columns
        for (x in 0 until this.size) {
            var target: Node? = this.nodes[x]
            for (y in 0 until this.size) {
                if (target != this.nodes[this.size * y + x]) {
                    target = null
                }
            }
            if (target != null) {
                return target
            }
        }

        // check rows
        for (y in 0 until this.size) {
            var target: Node? = this.nodes[y * this.size]
            for (x in 0 until this.size) {
                if (target != this.nodes[this.size * y + x]) {
                    target = null
                }
            }
            if (target != null) {
                return target
            }
        }

        // check diagonals
        var target: Node? = this.nodes[0]
        for (i in 0 until this.size) {
            if (target != this.nodes[this.size * i + i]) {
                target = null
            }
        }
        if (target != null) {
            return target
        }

        target = this.nodes[this.size * (this.size - 1)]
        for (i in 0 until this.size) {
            if (target != this.nodes[this.size * (this.size - 1 - i) + i]) {
                target = null
            }
        }

        return target
    }
}
