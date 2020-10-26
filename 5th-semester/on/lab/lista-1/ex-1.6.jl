#!/usr/bin/env julia
#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 1, Zadanie 1.5.
#

# this utility function fills up the mantissa
function sum_(bits)
    # start at 0
    output = fl(0)
    # add 1, 2, 4, \dots
    for i in range(0, length=bits)
        output += fl(2^i)
    end
    return output
end

# assert the program’s arguments
if length(ARGS) == 0
    println("error: provide the floating point precision (16, 32 or 64 bits)")
    exit(1)
end

fl_precision_string = ARGS[1]

if fl_precision_string == "16"
    fl = Float16
    # fill up the mantissa
    mach_max = sum_(11)
elseif fl_precision_string == "32"
    fl = Float32
    # fill up the mantissa
    mach_max = sum_(24)
elseif fl_precision_string == "64"
    fl = Float64
    # fill up the mantissa
    mach_max = sum_(53)
else
    println("error: provide one of [16, 32, 64]")
    exit(1)
end
# assert end

# iteratively find the max value
for i in range(1, length=2500)
    # if the next value would be considered ∞ break the loop
    if isinf(fl(mach_max * 2))
        break
    end
    # otherwise continue
    global mach_max = fl(mach_max * 2)
end

# print out the results
o1, o2 = mach_max, floatmax(fl)

println("iterative method = ", o1, "; floatmax(fl) = ", o2, "; equal = ", (o1 == o2))
