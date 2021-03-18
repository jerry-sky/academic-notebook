package com.example.ordnung;

import java.util.Random;

public enum ButtonMatrix {
    NW,
    N,
    NE,
    W,
    C,
    E,
    SW,
    S,
    SE;

    private static final ButtonMatrix[] VALUES = values();
    private static final int SIZE = VALUES.length;
    private static final Random RANDOM = new Random();

    public static ButtonMatrix GetRandom()  {
        return VALUES[RANDOM.nextInt(SIZE)];
    }

}
