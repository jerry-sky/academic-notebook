package com.example.ordnung

import java.util.*
import java.util.function.BiConsumer

class InvertibleMap<T, S>(first: HashMap<T, S>) {
    private val primary = HashMap<T, S>()
    private val inverted = HashMap<S, T>()
    fun getObj(key: T): S? {
        return primary[key]
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

    init {
        first.forEach { (t: T, s: S) ->
            primary[t] = s
            inverted[s] = t
        }
    }
}
