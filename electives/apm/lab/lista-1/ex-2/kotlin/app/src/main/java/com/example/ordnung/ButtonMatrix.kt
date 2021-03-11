package com.example.ordnung

import java.util.*

enum class ButtonMatrix {
    NW, N, NE, W, C, E, SW, S, SE;

    companion object {
        private val VALUES = values()
        private val SIZE = VALUES.size
        private val RANDOM = Random()
        fun GetRandom(): ButtonMatrix {
            return VALUES[RANDOM.nextInt(
                SIZE
            )]
        }
    }
}
