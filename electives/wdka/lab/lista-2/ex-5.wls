#!/usr/bin/env wolframscript

Print[ ( SeriesCoefficient[ Series[ (1 + x + x^2)^20, {x, 0, 20} ], 19 ] )/20 ]

"wynik = 18199284"
