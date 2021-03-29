package com.example.tictactoe.gamelogic

import java.util.*

class InvertibleMap<T, S> {

    private val primary = HashMap<T, S>()
    private val inverted = HashMap<S, T>()
    fun getObj(key: T): S? {
        return primary[key]
    }

    fun getObjs(): List<S> {
        return this.primary.values.toList()
    }

    fun getKey(obj: S): T? {
        return inverted[obj]
    }

    fun forEach(action: (Map.Entry<T, S>) -> Unit) {
        primary.forEach(action)
    }

    fun size(): Int {
        return primary.size
    }

    constructor(first: HashMap<T, S>) {
        first.forEach { (t: T, s: S) ->
            primary[t] = s
            inverted[s] = t
        }
    }
}
