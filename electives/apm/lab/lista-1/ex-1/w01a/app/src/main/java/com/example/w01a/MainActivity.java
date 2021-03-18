package com.example.w01a;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import java.util.Random;

public class MainActivity extends AppCompatActivity {

    private int score;
    private int r1;
    private int r2;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        score = 0;
        roll();
    }

    private void roll()
    {
        TextView pt = (TextView)findViewById(R.id.points);
        pt.setText("Punkty: " + Integer.toString(score));
        Random rand = new Random();
        r1 = rand.nextInt(10);
        r2 = rand.nextInt(10);
        Button b1 = (Button)findViewById(R.id.buttonLeft);
        b1.setText(Integer.toString(r1));
        Button b2 = (Button)findViewById(R.id.buttonRight);
        b2.setText(Integer.toString(r2));
    }

    public void leftButton(View view) {
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

    public void rightButton(View view) {
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
