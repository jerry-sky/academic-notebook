#!/usr/bin/env wolframscript

Print[ SeriesCoefficient[ Series[ Sum[ 1/(n+1) * Binomial[2n, n] * z^n, {n, 0, 18} ], {z, 0, 18} ], 18 ] ]

"wynik = 477638700"
