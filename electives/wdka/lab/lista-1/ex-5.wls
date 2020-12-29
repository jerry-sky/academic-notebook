#!/usr/bin/env wolframscript
(* ::Package:: *)

"OGF dla klasy pomocniczej (określa liczby jakich możemy użyć)"
B = z + z^2 + z^3 + z^4 + z^5 + z^(10) + z^(50) + z^(100)

"OGF dla sekwencji 30 liczb z klasy mathcal{B}"
A = B^30

"obliczamy żądaną wartość"
Print[SeriesCoefficient[ Series[ A, {z,0,200}], 200]]

"wynik: 59115949907090587181520 = 5.9115949907 cdot 10^{22}"
