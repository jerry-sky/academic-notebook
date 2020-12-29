#!/usr/bin/env wolframscript

Print[ SeriesCoefficient[ Series[ (1+z)^(10) * (1+z^2)^3 * (1+z^7), {z, 0, 12} ], 12 ] ]

"wynik = 990"
