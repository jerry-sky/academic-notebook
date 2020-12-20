#!/usr/bin/env wolframscript

A = Sum[z^n * (2 + u)^n, {n, 0, Infinity}]

Au1 = Sum[z^n * 3^n, {n, 0, Infinity}]

(* delimiter *)
deli = SeriesCoefficient[ Au1, {z, 0, n} ]

(* E(\chi) *)
Echi = (SeriesCoefficient[ D[A, u] /. u->1, {z, 0, n}]) / deli

(* E(chi^2) *)
Echi2 = (SeriesCoefficient[ D[D[A, u], u] /. u->1, {z, 0, n}]) / deli + Echi

(* wynik (wartość oczekiwana) = n/3 *)
Print[ "expected value: ", PiecewiseExpand[Echi, n>=0] ]

(* wynik (wariancja) = n/3 + ((n - 1)*n)/9 - n^2/9 = 2n/9 *)
Print[ "variance: ", PiecewiseExpand[Echi2 - Echi^2, n>=0] ]
