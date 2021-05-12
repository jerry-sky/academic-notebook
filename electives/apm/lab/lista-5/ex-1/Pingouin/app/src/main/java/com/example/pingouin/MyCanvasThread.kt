package com.example.pingouin

import android.graphics.Canvas
import android.view.SurfaceHolder

class MyCanvasThread(
    private val surfaceHolder: SurfaceHolder,
    private val myCanvas: MyCanvas,
    targetFPS: Int = 60
) : Thread() {

    private var running = false
    private var canvas: Canvas? = null
    private val targetTime = (1000 / targetFPS).toLong()

    override fun start() {
        this.running = true
        super.start()
    }

    fun shutdown() {
        this.running = false
        super.join()
    }

    override fun run() {
        var startTime: Long
        var timeMillis: Long
        var waitTime: Long

        while (running) {
            startTime = System.nanoTime()
            canvas = surfaceHolder.lockCanvas()
            if (canvas == null) continue
            myCanvas.draw(canvas)
            myCanvas.update()
            surfaceHolder.unlockCanvasAndPost(canvas)
            timeMillis = (System.nanoTime() - startTime) / 1000000
            waitTime = targetTime - timeMillis

            if (waitTime >= 0)
                sleep(waitTime)
        }
    }

}
