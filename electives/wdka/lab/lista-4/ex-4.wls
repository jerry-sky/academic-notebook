#!/usr/bin/env wolframscript

CC = Exp[Sum[(z^n)/n, {n, 1, Infinity}] - (z^3)/3 + (u * z^3)/3]

CCu1 = 1/(1-z)

(* delimiter *)
deli = SeriesCoefficient[ CCu1, {z, 0, n} ]

(* E(\chi) *)
Echi = (SeriesCoefficient[ D[CC, u] /. u->1, {z, 0, n}]) / deli

(* E(\chi^2) *)
Echi2 = (SeriesCoefficient[ D[D[CC, u], u] /. u->1, {z, 0, n}]) / deli + Echi

(* wynik (wartość oczekiwana) = Piecewise[{{1/3, n > 2}}, 0] *)
(* czyli dla n ≤ 2 E(\chi) = 0 (oczywiste bo mamy mniej niż trzy elementy) *)
(* za to dla n ≥ 3 E(\chi) = 1/3 *)
Print[ "expected value:  ", PiecewiseExpand[Echi, n>0] ]

(* wynik (wariancja) = Piecewise[{{2/9, Inequality[2, Less, n, LessEqual, 5]}, {1/3, n > 5}}, 0] *)
(* czyli dla n ≤ 2 Var(\chi) = 0, dla n \in [3; 5] Var(\chi) = 2/9, za to dla n > 5 Var(\chi) = 1/3 *)
X = PiecewiseExpand[Echi2 - Echi^2, n>0]
Print[ "variance:        ", X ]

(* wynik: 1/3 *)
n=30
Print[ "variance(n=30):  ", X ]
