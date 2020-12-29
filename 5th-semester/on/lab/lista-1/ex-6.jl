#!/usr/bin/env julia
#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 1, Zadanie 6.
#

fl = Float64

function f(x::fl)
    return fl(sqrt(fl(fl(x^2) + 1)) - 1)
end

function g(x::fl)
    return fl(fl(x^2) / fl(sqrt(fl(fl(x^2) + 1)) + 1))
end

# print out the results
for i in (-1:-1:-16)
    o1 = f(fl(fl(8)^i))
    o2 = g(fl(fl(8)^i))
    println(
        "f(8^{", i, "}) &= ", o1, "\\\\ \n",
        "g(8^{", i, "}) &= ", o2, "\\\\",
        # "equal? ", (o1 == o2), "\n"
    )
end
