#!/usr/bin/env wolframscript

S = Sum[ Coefficient[ Sum[z^k, {k, 0, 10}]^{n+1}, z^(100-n) ]
         - Coefficient[ Sum[z^k, {k, 0, 9}]^{n+1}, z^(100-n)], {n, 1, 90} ]

Print[ N[ S / 2^(100) ] ]

"wynik = 0.022107962880719877"
