#!/usr/bin/env julia
#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 3, Zadanie 4.2.
#

include("iterative-methods.jl")
using .IterativeMethods

fl = IterativeMethods.FL

r, fr, k, err =  IterativeMethods.mstycznych(
    x -> sin(x) - (x/2)^2,
    x -> cos(x) - x/2,
    fl(1.5),
    fl((10^(-5))/2),
    fl((10^(-5))/2),
    200
)

println(
    "r = ", r, "\n",
    "f(r) = ", fr, "\n",
    "k = ", k, "\n",
    err == 0 ? "" : string("error code: ", err)
)
