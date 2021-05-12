package com.example.pingouin

import android.graphics.Color
import android.graphics.Point
import androidx.annotation.ColorInt

class Vector2D(var x: Float, var y: Float) {

    companion object {
        fun from(vec: Vector2D): Vector2D {
            return Vector2D(vec.x, vec.y)
        }
    }

    fun translate(dx: Float, dy: Float) {
        this.x += dx
        this.y += dy
    }

    fun invertX() {
        this.x = -this.x
    }

    fun invertY() {
        this.y = -this.y
    }

}

enum class ShapeType {
    Ball,
    Paddle,
}

class Shape(
    val origin: Vector2D,
    var speed: Vector2D,
    val type: ShapeType,
    val size: Int,
    @ColorInt val colour: Int,
) {
    fun move() {
        this.origin.translate(this.speed.x, this.speed.y)
    }
}
