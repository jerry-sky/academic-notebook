#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 4., Zadania 1.–4.
#

module Interpolation

using PyPlot

FL = Float64

"""
### Checks if the provided vectors are of equal length.

### Arguments
- `x` — first vector
- `y` — second vector

### Return value:
- `Nothing` — the function either throws an error if there is a mismatch in the vector lengths or does nothing.

"""
function _assertDimensionError(x, y)
    if length(x) != length(y)
        throw(DimensionMismatch("provided vectors are of not same length"))
    end
end

"""
### Calculates the difference quotients for a given set of nodes and a set of values of a given function in those nodes.

### Arguments
- `x` — vector of nodes
- `f` — vector of values of a given function in those nodes

### Return value:
- a vector of difference quotients

"""
function ilorazyRoznicowe(x::Vector{FL}, f::Vector{FL})

    # assert vector lengths
    _assertDimensionError(x, f)

    len = length(x)

    # copy the values (the first iteration)
    tmp = copy(f)

    # the output vector that contains all the difference quotients
    output = Vector{FL}()
    push!(output, tmp[1])

    # perform the rest of the iterations
    for p in (len-1):-1:1
        # m = len-p

        # calc all the difference quotients in this column
        for k in 1:p
            a = (tmp[k+1] - tmp[k])
            # m = len-p
            b = (x[k + (len-p)] - x[k])
            tmp[k] = a/b
        end

        push!(output, tmp[1])

    end

    return output

end

"""
### Calculates the value of the interpolation polynomial in a given point.

### Arguments
- `x` — vector of nodes
- `fx` — vector of difference quotients
- `t` — the point in which the function will calculate the value of the interpolation polynomial

### Return value:
- value of the interpolation polynomial in the provided point `t`

"""
function warNewton(x::Vector{FL}, fx::Vector{FL}, t::FL)

    # assert vector length
    _assertDimensionError(x, fx)

    # here `n` is actually equal to $n+1$ relative to the algorithm explanation in the attached document
    n = length(x)

    # implement the recursive function
    # special case wₙ(z) = f[x₀,…,xₙ] if k == n
    # otherwise return normal recursive value
    w = (z,k) -> (k == n ?
                  fx[n]
                : fx[k] + (z - x[k]) * w(z,k+1))

    # in Julia we count starting at `1`, so relative to the theory behind this algorithm it’s w₀(t) = Nₙ(t)
    return w(t, 1)

end

"""
### Calculates all the coefficients of the Newton’s interpolation polynomial in its natural polynomial form.

### Arguments
- `x` — vector of nodes
- `fx` — vector of difference quotients

### Return value:
- vector of coefficients of the Newton’s interpolation polynomial

"""
function naturalna(x::Vector{FL}, fx::Vector{FL})

    # assert vector length
    _assertDimensionError(x, fx)

    n = length(x)

    coefficients = [fx[n]]

    for k in (n-1):-1:1

        xₖ = x[k]

        new_b₀ = -coefficients[1] * xₖ + fx[k]

        # when calculating the new coefficients the `m`-th coefficient is copied over to the new `m+1`-th coefficient,
        # whilst the last coefficient is calculated using the previous last coefficient and the difference quotient
        new_coefficients = vcat([new_b₀], coefficients)

        # we iterate over all coefficients except the first one and the last one
        for m in n-k:-1:2

            # b^{(k)}_m = b^{(k+1)}_{m-1} - b^{(k+1)}_m ⋅ xₖ
            new_coefficients[m] = coefficients[m-1] - coefficients[m] * xₖ

        end

        coefficients = new_coefficients

    end

    return coefficients

end


"""
### Draws a graph of a given function and its interpolation.

### Arguments
- `f` — function to examine
- `a` — beginning of the interval to examine
- `b` — ending of the interval to examine
- `n` — the “resolution” (the degree of the interpolation polynomial) of the interpolation

### Return value:
- `Nothing` — the function invokes PyPlot plotting function.

"""
function rysujNnfx(f, a::FL, b::FL, n::Int)

    h = (b-a)/n
    res = h/10
    x = vec([i for i in a:h:b])

    fx = ilorazyRoznicowe(x, vec([f(i) for i in x]))

    XA = a:res:b

    YA_f = [f(i) for i in XA]
    YA_N = [warNewton(x, fx, i) for i in XA]

    plot(XA, YA_N)
    plot(XA, YA_f)

end

end
