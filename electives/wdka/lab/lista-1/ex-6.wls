#!/usr/bin/env wolframscript
(* ::Package:: *)

"definiujemy standardową OGF dla operatorname{CYC}"
A = Sum[ EulerPhi[n]/n * Log[1/(1-3*z^n)], {n, 1, 5}]

"wyświetl wynik"
Print[ SeriesCoefficient[ Series[ A, {z, 0, 5}], 5] ]

"wynik: 51"
