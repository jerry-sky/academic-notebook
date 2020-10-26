#!/usr/bin/env julia
#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 1, Zadanie 4.
#

fl = Float64

# define the step
δ = fl(2^(-52))

x = fl(1 + δ)

# go through all the consecutive numbers
for i in range(1, length=2^52-1)
    if fl(x * fl(1/x)) != 1
        # if the condition is fulfilled print out the number in question and break the loop
        println(
            bitstring(x), "\n",
            bitstring(fl(1/x)), "\n",
            fl(x * fl(1/x)) != 1, "\n",
            x, "\n",
            fl(1/x), "\n",
            )
        break
    end
    # otherwise continue
    global x = fl(x + fl(δ * i))
end
