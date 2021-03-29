package com.example.tictactoe

import android.app.Activity
import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.view.View
import com.example.tictactoe.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    private val GAME_ACTIVITY_RETURN_CODE = 123

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        this.binding = ActivityMainBinding.inflate(layoutInflater)
    }

    fun click(button: View) {
        val intent = if (button.id == this.binding.three.id) {
            Intent(this, ThreeByThree::class.java)
        } else {
            Intent(this, FiveByFive::class.java)
        }
        this.startActivityForResult(intent, this.GAME_ACTIVITY_RETURN_CODE)
    }

    override fun onActivityResult(requestCode: Int, resultCode: Int, data: Intent?) {
        super.onActivityResult(requestCode, resultCode, data)

        if(requestCode == this.GAME_ACTIVITY_RETURN_CODE && resultCode == Activity.RESULT_OK) {
            val winner = data!!.getStringExtra("winner")
            Log.e("MERDAS", winner!!)
            val intent = Intent(this, GameOverActivity::class.java)
            intent.putExtra("winner", winner)
            this.startActivity(intent)
        }
    }
}
