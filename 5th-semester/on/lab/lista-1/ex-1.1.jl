#!/usr/bin/env julia
#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 1, Zadanie 1.1.
#

# assert the program’s arguments
if length(ARGS) == 0
    println("error: provide the floating point precision (16, 32 or 64 bits)")
    exit(1)
end

fl_precision_string = ARGS[1]

if fl_precision_string == "16"
    fl = Float16
elseif fl_precision_string == "32"
    fl = Float32
elseif fl_precision_string == "64"
    fl = Float64
else
    println("error: provide one of [16, 32, 64]")
    exit(1)
end
# assert end

# start finding the machine epsilon at 0.5
mach_eps = fl(1/2)

# iteratively find the machine epsilon
for i in range(1, length=100)
    # if adding even smaller eps would not change the value break the loop
    if fl(1) + fl(mach_eps/2) == fl(1)
        break
    end
    # otherwise continue
    global mach_eps = fl(mach_eps/2)
end

# print the output
println("iterative method = ", mach_eps, "; eps(fl) = ", eps(fl), "; equal = ", (eps(fl) == mach_eps))
