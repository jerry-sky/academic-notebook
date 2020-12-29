#!/usr/bin/env julia
#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 1, Zadanie 7.
#

fl = Float64

function f(x::fl)::fl
    return fl(sin(x) + cos(3*x))
end

function f_derivative(x::fl)::fl
    return fl(cos(x) - 3 * sin(3*x))
end

# break out this part of the approximate function for later use
function _approximate_derivative_internal(func, x::fl, h::fl)::fl
    return fl(func(x + h) - func(x))
end
function approximate_derivative_at_given_point(func, x::fl, h::fl)::fl
    return fl( _approximate_derivative_internal(func, x, h) / h )
end

# calculate the results and print them out
for n in -25:-1:-32
    h = fl(2.0^n)
    x = fl(1.0)
    appr = approximate_derivative_at_given_point(f, x, h)
    exact = f_derivative(x)

    println(
        "n = ", n, "\n",
        "h                         = ", h, "\n",
        "f(x + h) - f(x)           = ", _approximate_derivative_internal(f, x, h), "\n",
        "\\tilde{f’}(x)             = ", appr, "\n",
        "f’(x)                     = ", exact, "\n",
        "|f’(x) - \\tilde{f’}(x)|   = ", abs( fl(exact - appr) ),
        "\n"
    )
end
