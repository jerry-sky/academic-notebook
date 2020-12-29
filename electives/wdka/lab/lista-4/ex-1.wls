#!/usr/bin/env wolframscript

(* Wynik: 19054894203999260640645120000 *)
Print[ 30! * SeriesCoefficient[ Exp[Sum[(z^n)/n, {n, 1, 5}]], {z, 0, 30} ] ]
