#!/usr/bin/env julia
#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 2, Zadanie 4.
#

# imports
using Polynomials
using LinearAlgebra

# the polynomial coefficients
coeffs = [1.0, -210.0, 20615.0,-1256850.0, 53327946.0, -1672280820.0, 40171771630.0, -756111184500.0, 11310276995381.0, -135585182899530.0, 1307535010540395.0, -10142299865511450.0, 63030812099294896.0, -311333643161390640.0, 1206647803780373360.0, -3599979517947607200.0,
 8037811822645051776.0, -12870931245150988800.0,
 13803759753640704000.0, -8752948036761600000.0,
 2432902008176640000.0]

# if given any arguments run the program with a slight modification
if length(ARGS) > 0
    coeffs[2] = coeffs[2] - 2^(-23)
end

# generate the polynomial
reverse!(coeffs)
P = Polynomial(coeffs)

# this is the canonical form of the polynomial
function p(x)
    return (x - 20)*(x - 19)*(x - 18)*(x - 17)*(x - 16)*(x - 15)*(x - 14)*(x - 13)*(x - 12)*(x - 11)*(x - 10)*(x - 9)*(x - 8)*(x - 7)*(x - 6)*(x - 5)*(x - 4)*(x - 3)*(x - 2)*(x - 1)
end

# calculate the roots of the polynomial (given its natural form)
rs = roots(P)

# print out the results
for k in 1:20

    zₖ = rs[k]
    print(
        k, " & ",
        zₖ, " & ",
        norm(P(zₖ)), " & ",
        norm(p(zₖ)), " & ",
        norm(zₖ - k), "\\\\\n"
    )

end
