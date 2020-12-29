#!/usr/bin/env wolframscript

(* Wynik: 222444420953341570876847086387200 *)
Print[ 30! * SeriesCoefficient[ Sum[((Log[1/(1-z)])^n)/(n!), {n, 0, 5}], {z, 0, 30} ] ]
