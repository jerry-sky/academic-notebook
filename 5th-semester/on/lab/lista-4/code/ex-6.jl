#!/usr/bin/env -S julia -iq
#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 4., Zadanie 6.
#

include("interpolation.jl")
using .Interpolation

f = x -> abs(x)
a = -1.0
b = 1.0
n = 5

if length(ARGS) > 0
    ns = ARGS[1]
    n = parse(Int64, ns)
end

if length(ARGS) > 1
    fn = ARGS[2]
    if fn == "x"
        f = x -> 1 / (1+x^2)
        a = -5.0
        b = 5.0
    end
end

Interpolation.rysujNnfx(f, a, b, n)

println("end the interactive session to close all plots")
