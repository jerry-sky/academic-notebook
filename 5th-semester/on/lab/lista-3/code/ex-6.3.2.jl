#!/usr/bin/env julia
#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 3, Zadanie 6. metoda siecznych, funkcja `f_2`
#

include("iterative-methods.jl")
using .IterativeMethods

fl = IterativeMethods.FL

a = fl(-1)
b = fl(0)

if length(ARGS) > 0
    global a = fl(0.2)
    global b = fl(-0.6)
    println("warning: using different first and second approximation")
end

r, fr, k, err =  IterativeMethods.msiecznych(
    x -> x * exp(-x),
    a,
    b,
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
