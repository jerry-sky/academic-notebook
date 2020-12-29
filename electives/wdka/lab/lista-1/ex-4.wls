#!/usr/bin/env wolframscript

"określamy funkcję tworzącą"
S = (Sum[ z^(10*i), {i, 0, 100} ]) * (Sum[ z^(100*i), {i, 0, 10} ]) * (Sum[ z^(200*i), {i, 0, 5} ]) * (Sum[ z^(500*i), {i, 0, 3}])

"wyświetlamy żądany współczynnik \(1600 groszy = 16 zł\)"
Print[SeriesCoefficient[Series[S, {z,0, 1600}], 1600]]

"wynik: 116612759 = 106"
