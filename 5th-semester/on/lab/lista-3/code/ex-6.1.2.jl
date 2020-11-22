#!/usr/bin/env julia
#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 3, Zadanie 6. metoda bisekcji, funkcja `f_2`
#

include("iterative-methods.jl")
using .IterativeMethods

fl = IterativeMethods.FL

a = fl(-0.5)
b = fl(0.5)

if length(ARGS) > 0
    global a = fl(-0.29)
    global b = fl(1)
    println("warning: using different interval")
end

r, fr, k, err =  IterativeMethods.mbisekcji(
    x -> x * exp(-x),
    a,
    b,
    fl(10^(-5)),
    fl(10^(-5))
)

println(
    "r = ", r, "\n",
    "f(r) = ", fr, "\n",
    "k = ", k, "\n",
    err == 0 ? "" : string("error code: ", err)
)
