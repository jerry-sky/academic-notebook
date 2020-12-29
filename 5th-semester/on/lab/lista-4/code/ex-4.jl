#!/usr/bin/env -S julia -iq
#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 4., Zadanie 4. — podstawowy test
#

include("interpolation.jl")
using .Interpolation

Interpolation.rysujNnfx(x->sin(x) + cos(x), 0.0, 5.0, 5)

println("end the interactive session to close all plots")
