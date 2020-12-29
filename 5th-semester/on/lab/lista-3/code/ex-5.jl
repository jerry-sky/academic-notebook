#!/usr/bin/env julia
#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 3, Zadanie 5.
#

include("iterative-methods.jl")
using .IterativeMethods

fl = IterativeMethods.FL

r1, fr1, k1, err1 =  IterativeMethods.mbisekcji(
    x -> 3x - exp(x),
    fl(0),
    fl(1),
    fl(10^(-4)),
    fl(10^(-4))
)

println(
    "first root:\n",
    "  r = ", r1, "\n",
    "  f(r) = ", fr1, "\n",
    "  k = ", k1, "\n",
    err1 == 0 ? "" : string("  error code: ", err1)
)

r2, fr2, k2, err2 =  IterativeMethods.mbisekcji(
    x -> 3x - exp(x),
    fl(1),
    fl(2),
    fl(10^(-4)),
    fl(10^(-4))
)

println(
    "\nsecond root:\n",
    "  r = ", r2, "\n",
    "  f(r) = ", fr2, "\n",
    "  k = ", k2, "\n",
    err2 == 0 ? "" : string("  error code: ", err2)
)
