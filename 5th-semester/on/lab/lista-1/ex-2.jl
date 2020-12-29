#!/usr/bin/env julia
#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 1, Zadanie 2.
#

# Kahan’s ϵ finding method
function kahans_eps(fl)
    return abs(fl( 3 * fl(fl(4/3) - 1) - 1 ))
end

# print out the results for different float arithmetic types
for fl in [Float16, Float32, Float64]
    println(fl)
    println("  - Kahan’s method = ", kahans_eps(fl), "; actual ϵ = ", eps(fl), "; equal = ", (kahans_eps(fl) == eps(fl)))
end
