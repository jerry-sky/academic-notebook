#!/usr/bin/env julia
#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 1, Zadanie 1.2.
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

# start finding the machine eta at 0.5
mach_eta = fl(1/2)

# iteratively find the machine eta
for i in range(1, length=1100)
    # if dividing the \eta even further would bring it to the absolute zero break the loop
    if fl(mach_eta/2) == 0
        break
    end
    # otherwise continue
    global mach_eta = fl(mach_eta/2)
end

# print the output
println("iterative method = ", mach_eta, "; nextfloat(fl(0.0)) = ", nextfloat(fl(0.0)), "; equal = ", (nextfloat(fl(0.0)) == mach_eta))
