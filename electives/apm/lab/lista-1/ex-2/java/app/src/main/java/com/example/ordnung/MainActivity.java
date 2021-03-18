package com.example.ordnung;

import androidx.appcompat.app.AppCompatActivity;
import androidx.core.content.ContextCompat;

import android.content.Context;
import android.os.Bundle;
import android.os.Handler;
import android.os.Looper;
import android.view.View;
import android.widget.Button;
import android.widget.Toast;

import com.example.ordnung.databinding.ActivityMainBinding;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class MainActivity extends AppCompatActivity {

    private ActivityMainBinding binding;
    private InvertibleMap<ButtonMatrix, Button> buttonsList;

    /**
     * The current combination.
     */
    private List<ButtonMatrix> currentOrdnung;

    /**
     * The ID of what the user should input next.
     */
    private int expectedOrdnungElement;

    private int blinkColour;
    private int defaultColour;

    /**
     * Duration of each color blink.
     */
    private final int blinkDuration = 750;

    private int highScore = -1;

    private final Handler handler = new Handler(Looper.getMainLooper());

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        this.binding = ActivityMainBinding.inflate(getLayoutInflater());
        View view = this.binding.getRoot();
        setContentView(view);

        this.blinkColour = ContextCompat.getColor(getBaseContext(), R.color.teal_200);
        this.defaultColour = ContextCompat.getColor(getBaseContext(), R.color.purple_200);

        ActivityMainBinding b = this.binding;
        HashMap<ButtonMatrix, Button> tmp = new HashMap<>();
        tmp.put(ButtonMatrix.SE, b.buttonSouthEast);
        tmp.put(ButtonMatrix.S, b.buttonSouth);
        tmp.put(ButtonMatrix.SW, b.buttonSouthWest);
        tmp.put(ButtonMatrix.E, b.buttonEast);
        tmp.put(ButtonMatrix.C, b.buttonCenter);
        tmp.put(ButtonMatrix.W, b.buttonWest);
        tmp.put(ButtonMatrix.NE, b.buttonNorthEast);
        tmp.put(ButtonMatrix.N, b.buttonNorth);
        tmp.put(ButtonMatrix.NW, b.buttonNorthWest);
        this.buttonsList = new InvertibleMap<>(tmp);

        // get the first random combination
        this.startOver();
    }

    /**
     * Reset the state of the game and begin with a new sequence.
     */
    private void startOver() {
        // disable the buttons before the game (re)starts
        this.disableButtons();

        if (this.highScore != -1) {
            // score at the end of the round
            int roundScore = this.currentOrdnung.size() - 1;
            if (roundScore == 2) {
                // the Ordnung length was three, witch means the user did not score anything
                roundScore = 0;
            }
            // this is at least the second game
            // `this.highScore` equal to negative one means that this is the first game, so no toasts should show up
            if (roundScore > this.highScore) {
                // save the new high score
                this.highScore = this.currentOrdnung.size() - 1;
                Toast toast = Toast.makeText(
                    getApplicationContext(),
                    "You beat the high score! (" + this.highScore + ")",
                    Toast.LENGTH_SHORT
                );
                toast.show();
            } else {
                // notify the user he failed to beat the high score
                Toast toast = Toast.makeText(
                    getApplicationContext(),
                    "You did not beat the high score of " + this.highScore + ". Your score was " + roundScore + ".",
                    Toast.LENGTH_SHORT
                );
                toast.show();
            }
        } else {
            this.highScore = 0;
        }

        // (re)populate die Ordnung
        this.currentOrdnung = new ArrayList<>();
        this.currentOrdnung.add(ButtonMatrix.GetRandom());
        this.currentOrdnung.add(ButtonMatrix.GetRandom());
        this.currentOrdnung.add(ButtonMatrix.GetRandom());
        // reset
        this.expectedOrdnungElement = 0;
        // show the Ordnung
        handler.postDelayed(
            () -> this.showCurrentOrdnung(), // for some reason `this::showCurrentOrdnung` breaks the program
            2000
        );
    }

    private void expandOrdnung() {
        this.currentOrdnung.add(ButtonMatrix.GetRandom());
        this.showCurrentOrdnung();
        this.expectedOrdnungElement = 0;
    }

    private void showCurrentOrdnung() {
        // turn off all the buttons
        this.disableButtons();
        // blink each of the buttons for a second
        for (int i = 0; i < this.currentOrdnung.size(); i++) {
            ButtonMatrix el = this.currentOrdnung.get(i);
            Button button = this.buttonsList.getObj(el);
            this.handler.postDelayed(() -> {
                // blink
                button.setBackgroundColor(this.blinkColour);
            }, this.blinkDuration * i);
            this.handler.postDelayed(() -> {
                // get back to the original colour
                button.setBackgroundColor(this.defaultColour);
            }, this.blinkDuration * (i + 1) - (int) (0.2 * this.blinkDuration));
        }

        this.handler.postDelayed(() -> {
            // turn back on all the buttons
            this.enableButtons();
        }, this.blinkDuration * this.currentOrdnung.size());
    }

    private void handleUserInput(ButtonMatrix input) {
        if (input == this.currentOrdnung.get(this.expectedOrdnungElement)) {
            // correct
            // get next
            this.expectedOrdnungElement++;
            // and if the user has reached the end of the current Ordnung, expand it
            if (this.expectedOrdnungElement == this.currentOrdnung.size()) {
                this.expandOrdnung();
            }
        } else {
            // incorrect
            // start over
            this.startOver();
        }
    }

    public void button(View view) {
        this.handleUserInput(this.buttonsList.getKey((Button) view));
    }

    public void disableButtons() {
        this.buttonsList.forEach((key, button) -> button.setClickable(false));
    }

    public void enableButtons() {
        this.buttonsList.forEach((key, button) -> button.setClickable(true));
    }

}
