#!/usr/bin/env julia
#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 4., Zadanie 3. — podstawowy test (przykład z wykładu)
#

include("interpolation.jl")
using .Interpolation

FL = Interpolation.FL

x = Vector{FL}([3, 1, 5, 6])
f = Vector{FL}([1, -3, 2, 4])

fx = Interpolation.ilorazyRoznicowe(x, f)

a = Interpolation.naturalna(x, fx)

println(a)
