package com.example.w01b

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Toast
import com.example.w01b.databinding.ActivityMainBinding
import kotlin.random.Random

class MainActivity : AppCompatActivity() {

    private lateinit var binding: ActivityMainBinding

    private var r1 = 0;
    private var r2 = 0;
    private var score = 0;

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityMainBinding.inflate(layoutInflater)
        val view = binding.root
        setContentView(view)
        // setContentView(R.layout.activity_main)
        roll();
    }

    private fun roll() {
        this.binding.points.text = "Punkty:" + score;
        this.r1 = Random.nextInt(10);
        this.r2 = Random.nextInt(10);
        this.binding.buttonLeft.text = "" + r1;
        this.binding.buttonRight.text = "" + r2;
    }


    fun leftButton(view: View) {
        if (r1 >= r2) {
            Toast.makeText(this, "Dobrze!", Toast.LENGTH_SHORT).show();
            score++;
        }
        else
        {
            Toast.makeText(this, "Źle!", Toast.LENGTH_SHORT).show();
            score--;
        }
        roll();

    }
    fun rightButton(view: View) {
        if (r1 <= r2) {
            Toast.makeText(this, "Dobrze!", Toast.LENGTH_SHORT).show();
            score++;
        }
        else
        {
            Toast.makeText(this, "Źle!", Toast.LENGTH_SHORT).show();
            score--;
        }
        roll();
    }
}
