#!/usr/bin/env wolframscript

Print[ SeriesCoefficient[ Series[ (1 + z + z^2 + z^3)^4, {z, 0, 5} ], 5 ] * Factorial[5] * Factorial[3] / Factorial[2] ]

"wynik = 14400"
