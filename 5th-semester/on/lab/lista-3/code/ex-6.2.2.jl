#!/usr/bin/env julia
#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 3, Zadanie 6. metoda Newtona, funkcja `f_2`
#

include("iterative-methods.jl")
using .IterativeMethods

fl = IterativeMethods.FL

a = fl(0)

if length(ARGS) > 0
    global a = fl(-0.29)
    println("warning: using different first approximation")
end

r, fr, k, err =  IterativeMethods.mstycznych(
    x -> x * exp(-x),
    x -> -1.0 * exp(-1.0 * x) * (x-1),
    a,
    fl(10^(-5)),
    fl(10^(-5)),
    100
)

println(
    "r = ", r, "\n",
    "f(r) = ", fr, "\n",
    "k = ", k, "\n",
    err == 0 ? "" : string("error code: ", err)
)
