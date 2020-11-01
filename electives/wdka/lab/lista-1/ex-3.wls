#!/usr/bin/env wolframscript

Print[SeriesCoefficient[ ( 1 + z )^(50) * ( 1 + z^5 )^(10) * ( 1 + z^(10) )^(10) * ( 1 + z^(20) )^(20), {z, 0, 200}]]

"wynik: 1209902431363984921974763 = 1.2099024 cdot 10^{24}"
