package com.example.pingouin

import android.content.Context
import android.graphics.Canvas
import android.graphics.Paint
import android.util.AttributeSet
import android.util.Log
import android.view.MotionEvent
import android.view.SurfaceHolder
import android.view.SurfaceView

class MyCanvas(
    context: Context,
    attributeSet: AttributeSet,
) :
    SurfaceView(context, attributeSet), SurfaceHolder.Callback {

    val shapes: MutableList<Shape> = mutableListOf()
    private lateinit var thread: MyCanvasThread
    var onUpdate: () -> Unit = {}
    var onSurfaceCreated: () -> Unit = {}
    var onTouch: (points: List<Vector2D>) -> Unit = {}
    var paddleThickness: Int = 30

    private var onSurfaceChanged: (() -> Unit)? = {}

    private var surfaceAlreadyCreated: Boolean = false

    init {
        holder.addCallback(this)
    }

    fun addShape(shape: Shape) {
        this.shapes.add(shape)
    }

    override fun surfaceCreated(holder: SurfaceHolder) {
        thread = MyCanvasThread(holder, this)
        thread.start()
        onSurfaceCreated()
        surfaceAlreadyCreated = true
    }

    fun surfaceResume(onResumed: () -> Unit = {}) {
        if(!surfaceAlreadyCreated) {
            surfaceCreated(holder)
            onSurfaceChanged = onResumed
        }
    }

    override fun surfaceChanged(holder: SurfaceHolder, format: Int, width: Int, height: Int) {
        if(onSurfaceChanged != null) {
            onSurfaceChanged?.let { it() }
            onSurfaceChanged = null
        }
    }

    override fun surfaceDestroyed(holder: SurfaceHolder) {
        thread.shutdown()
        surfaceAlreadyCreated = false
    }

    fun update() {
        this.onUpdate()
    }

    override fun draw(canvas: Canvas?) {
        super.draw(canvas)

        if (canvas == null) return

        // draw all shapes
        for (shape in this.shapes) {
            this.drawShape(canvas, shape)
        }
    }

    private fun drawShape(canvas: Canvas, shape: Shape) {
        val paint = Paint().apply {
            color = shape.colour
        }

        when (shape.type) {
            ShapeType.Ball -> canvas.drawOval(
                shape.origin.x,
                shape.origin.y,
                shape.origin.x + shape.size,
                shape.origin.y + shape.size,
                paint
            )
            ShapeType.Paddle -> canvas.drawRect(
                shape.origin.x - paddleThickness/2,
                shape.origin.y,
                shape.origin.x + paddleThickness/2,
                shape.origin.y + shape.size,
                paint
            )
        }
    }

    override fun onTouchEvent(event: MotionEvent?): Boolean {
        if(event == null) return true

        val touchesCount = event.pointerCount

        val touches = List(touchesCount) {
            Vector2D(event.getX(it), event.getY(it))
        }

        this.onTouch(touches)

        return true
    }
}
