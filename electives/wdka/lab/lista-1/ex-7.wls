#!/usr/bin/env wolframscript
(* ::Package:: *)

"definiujemy standardową OGF dla operatorname{CYC}"
A = Sum[ EulerPhi[n]/n * Log[1/(1-4*z^n)], {n, 1, 20}]

"wyświetl wynik"
Print[ SeriesCoefficient[ Series[ A, {z, 0, 20}], 20] ]

"wynik: 54975633976 = 5.4975633976 cdot 10^{10}"
