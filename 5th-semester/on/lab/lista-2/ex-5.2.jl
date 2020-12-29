#!/usr/bin/env julia
#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 2, Zadanie 5.2.
#

fl1 = Float32
fl2 = Float64

# starting points
p = fl1(0.01)
pp = fl2(0.01)

r = 3

# calculate the next sequence member
function calc(x, fl)
    return fl(x + fl(r*fl(x*fl(1 - x))))
end

# print out the consecutive members of the sequences
for n in 1:40

    global p = calc(p, fl1)
    global pp = calc(pp, fl2)
    println(n, " & ", p, " & ", pp, "\\\\")

end
