#!/usr/bin/env wolframscript

Print[ SeriesCoefficient[ Series[ Sum[ 1/(n+1) * Binomial[2n, n] * z^n, {n, 0, 20} ], {z, 0, 20} ], 20 ] ]

"wynik = 6564120420"
