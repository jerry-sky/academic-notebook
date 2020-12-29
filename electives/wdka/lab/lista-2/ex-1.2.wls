#!/usr/bin/env wolframscript

Print[ SeriesCoefficient[ Series[ (1/(1-z)) * (1/(1-z^2)) * (1/(1-z^(20))) * (1/(1-z^(21))), {z, 0, 50} ], 44 ] ]

"wynik = 55"
