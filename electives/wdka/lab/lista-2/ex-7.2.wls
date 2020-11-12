#!/usr/bin/env wolframscript

Print[ Sum[ SeriesCoefficient[ Series[ (1+z)^(10) * (1+z^2)^3 * (1+z^7), {z, 0, n} ], n ], {n, 12, 23} ] ]

"wynik = 8192"
