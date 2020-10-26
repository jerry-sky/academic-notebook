#!/usr/bin/env julia
#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 1, Zadanie 3.1.
#

fl = Float64

# define the step
δ = fl(2^(-52))

# we can modify where we want to start “counting”
starting_point = fl(0)
x = fl(1)

# print out the consecutive numbers
for i in range(starting_point, stop=2^52)
    println(
        bitstring(
            fl(x + fl(δ * i))
        ),
        " (",
        fl(x + fl(δ * i)),
        ")"
    )
    sleep(1)
end
