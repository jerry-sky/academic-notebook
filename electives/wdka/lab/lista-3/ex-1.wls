#!/usr/bin/env wolframscript

Print[ N[(SeriesCoefficient[ (1/(1-z))^6 * z^6 / (1-2z), {z, 0, 30} ]) / 2^(30)] ]

"Wynik: 0.9998375428840517997741699218750"
