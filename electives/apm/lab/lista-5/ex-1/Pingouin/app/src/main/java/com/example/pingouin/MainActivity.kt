package com.example.pingouin

import android.graphics.Color
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.TextView
import androidx.appcompat.app.AlertDialog
import androidx.room.Room
import com.example.pingouin.model.GameDatabase
import com.example.pingouin.model.GameState
import java.util.*
import kotlin.concurrent.schedule

const val LT = "pingouin2021"

const val DATABASE_NAME = "database"

enum class Player {
    Left,
    Right
}

class MainActivity : AppCompatActivity() {

    private lateinit var myCanvas: MyCanvas
    private var cWidth: Int = 0
    private var cHeight: Int = 0

    private lateinit var scoreView: TextView

    private lateinit var ball: Shape
    private lateinit var paddleLeft: Shape
    private lateinit var paddleRight: Shape

    private var scoreLeft = 0
    private var scoreRight = 0

    private val paddleSize: Int = 250
    private val ballSize: Int = 24
    private var ballSpeed = Vector2D(10f, 0f)

    private lateinit var database: GameDatabase

    private var isActivityCreating = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        isActivityCreating = true

        scoreView = this.findViewById(R.id.score_view)

        myCanvas = this.findViewById(R.id.my_canvas)
        // once the surface is created, apply the game logic
        myCanvas.onSurfaceCreated = this::setupGame

    }

    override fun onResume() {
        super.onResume()
        if (!isActivityCreating) {
            myCanvas.surfaceResume {
                pauseGameFor(5)
            }
        }
    }

    override fun onPause() {
        super.onPause()
        isActivityCreating = false
        if(interval != null) interval!!.cancel()
        if(timeout != null) timeout!!.cancel()
    }

    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)

        Thread {
            database.gameState().saveState(GameState(scoreLeft, scoreRight))
        }.start()
    }

    /**
     * Asks the user if they want to resume the game that has been restored from the Room database.
     */
    private fun resumeGame(state: GameState) {
        runOnUiThread {
            // build dialog prompt
            val builder = this.let {
                AlertDialog.Builder(it)
            }
            builder
                .setMessage(R.string.resume_game_prompt_message)
                .setTitle(R.string.resume_game_prompt_message)
                .setPositiveButton(R.string.resume_game_prompt_yes_button) { _, _ ->
                    // reset the game
                    resetGame(true)
                    scoreLeft = state.scoreLeft
                    scoreRight = state.scoreRight
                    updateScoreboard()
                    startGame()
                }
                .setNegativeButton(R.string.resume_game_prompt_no_button) { _, _ ->
                    startGame()
                }
                .setCancelable(false)
            // show the dialog prompt
            val dialog = builder.create()
            dialog.show()
        }
    }

    private fun setupGame() {
        cWidth = myCanvas.width
        cHeight = myCanvas.height

        if (myCanvas.shapes.size == 0) {

            ball = Shape(
                Vector2D(0f, 0f),
                Vector2D.from(ballSpeed),
                ShapeType.Ball,
                ballSize,
                Color.WHITE
            )

            paddleLeft = Shape(
                Vector2D(0f, 0f),
                Vector2D(0f, 0f),
                ShapeType.Paddle,
                paddleSize,
                Color.WHITE
            )
            paddleRight = Shape(
                Vector2D(cWidth.toFloat(), 0f),
                Vector2D(0f, 0f),
                ShapeType.Paddle,
                paddleSize,
                Color.WHITE
            )

            this.resetGame()

            myCanvas.addShape(ball)
            myCanvas.addShape(paddleLeft)
            myCanvas.addShape(paddleRight)
        }

        // setup the database
        Thread {
            database = Room.databaseBuilder(
                applicationContext,
                GameDatabase::class.java, DATABASE_NAME
            ).build()
//            database.gameState().reset()
            if(isActivityCreating) {
                val state = database.gameState().getState()
                if (state != null) {
                    // there is a saved game
                    resumeGame(state)
                } else {
                    startGame()
                }
            }
        }.start()
    }

    private fun startGame() {
        pauseGameFor(5)
        // main game loop
        myCanvas.onUpdate = {
            // check for paddle hit
            var potentialPaddleHit: Shape? = null
            if (ball.origin.x <= 0 + myCanvas.paddleThickness) {
                // ball at the left edge
                potentialPaddleHit = paddleLeft
            } else if (ball.origin.x >= cWidth - myCanvas.paddleThickness) {
                // ball at the right edge
                potentialPaddleHit = paddleRight
            }
            if (potentialPaddleHit != null) {
                // normalize hit position
                val hitPosition = ball.origin.y - potentialPaddleHit.origin.y
                if (hitPosition in 0.0..paddleSize.toDouble()) {
                    // ball collided with a paddle
                    // invert horizontal speed
                    ball.speed.invertX()
                    // calculate new vertical speed
                    val kick = hitPosition - paddleSize / 2
                    ball.speed.y = kick * 0.1f
                } else {
                    // ball did not collide with a paddle
                    when (potentialPaddleHit) {
                        paddleLeft -> registerScore(Player.Right)
                        paddleRight -> registerScore(Player.Left)
                    }
                }
            }

            // check for ceiling or floor hit
            if (ball.origin.y <= 0 || ball.origin.y >= cHeight) {
                ball.speed.invertY()
            }

            ball.move()
        }

        myCanvas.onTouch = {
            for (touch in it) {
                if (touch.x < cWidth / 2) {
                    // left paddle
                    paddleLeft.origin.y = touch.y - paddleSize / 2
                } else {
                    // right paddle
                    paddleRight.origin.y = touch.y - paddleSize / 2
                }
            }
        }
    }

    private fun registerScore(winner: Player) {
        when (winner) {
            Player.Left -> scoreLeft++
            Player.Right -> scoreRight++
        }
        resetGame()
        updateScoreboard()
    }

    private fun resetGame(fullWipeDown: Boolean = false) {
        ball.origin.x = cWidth.toFloat() / 2 - ballSize / 2
        ball.origin.y = cHeight.toFloat() / 2 - ballSize / 2
        ball.speed.y = 0f
        ball.speed.invertX()

        if (fullWipeDown) {
            scoreLeft = 0
            scoreRight = 0
        }
    }

    private fun updateScoreboard() {
        runOnUiThread {
            scoreView.text = "$scoreLeft | $scoreRight"
        }
    }

    private var interval: Timer? = null
    private var timeout: Timer? = null
    private fun pauseGameFor(time: Int) {
        if(interval != null) interval!!.cancel()
        if(timeout != null) timeout!!.cancel()

        if(ball.speed.x != 0f) {
            // keep the original ball speed
            ballSpeed = Vector2D.from(ball.speed)
        }
        ball.speed = Vector2D(0f, 0f)
        var ticks = time
        interval = Timer("i", false)
        interval!!.schedule(0, 1000) {
            runOnUiThread {
                scoreView.text = getString(R.string.resuming_message) + " " + ticks.toString()
                ticks--
                if (ticks == 0) {
                    this.cancel()
                }
            }
        }
        timeout = Timer("t", false)
        timeout!!.schedule(time.toLong() * 1000) {
            ball.speed = ballSpeed
            updateScoreboard()
        }
    }

}
