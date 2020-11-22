#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 3, Zadania 1.–3.
#

module IterativeMethods

FL = Float64
MAX_ITERATIONS = 10^9
NEAR_ZERO = 2^(-2.0^32)

"""
### Finds the solution to the equation `f(x) = 0` using the bisection method.

### Arguments
- `f` — the function to find a root of
- `a` — beginning of the interval
- `b` — ending of the interval
- `delta` — the precision of the solution in terms of the X axis
- `epsilon` — the precision of the solution in terms of the Y axis

### Return value: a tuple of four values
- `[0]` — the approximation of the root of the `f` function
- `[1]` — the actual value of the `f` function in `[0]`
- `[2]` — number of iterations performed
- `[3]` — error indicator, possible values:
    - `0` — the method was convergent in this case
    - `1` — the `f` function doesn’t change its sign inside the given interval (doesn’t cut through the X axis)

"""
function mbisekcji(f, a::FL, b::FL, delta::FL, epsilon::FL)

    # begin with the starting values
    u = f(a)
    v = f(b)
    # the length of the section
    e = b - a

    if sign(u) == sign(v)
        # `f` doesn’t change its sign between `a` and `b`
        return (a, u, 0, 1);
    end

    # predefine some variables so they are accessible outside the loop
    k = 0
    c = 0
    w = 0
    # iterate
    for k in 0:MAX_ITERATIONS

        # divide into two sections — divide the length of the section by two
        e = e/2
        # pick the middle point
        c = a + e
        w = f(c)

        # if the solution is sufficient with respect to the given precision parameters terminate this method and return the output values
        if abs(e) < delta || abs(w) < epsilon
            return (c, w, k, 0)
        end

        # choose that section that contains the solution
        if sign(w) != sign(u)
            b = c
            v = w
        else
            a = c
            u = w
        end

    end

    # somehow the function exceeded MAX_ITERATIONS, however it seems so unlikely that a separate error code for this edge case would be an excess
    return (c, w, k, 0)

end

"""
### Finds the solution to the equation `f(x) = 0` using the Newton’s method.

### Arguments
- `f` — the function to find a root of
- `pf` — the derivative of the `f` function
- `x0` — first approximation
- `delta` — the precision of the solution in terms of the X axis
- `epsilon` — the precision of the solution in terms of the Y axis
- `maxint` — maximum iterations this function can perform

### Return value: a tuple of four values
- `[0]` — the approximation of the root of the `f` function
- `[1]` — the actual value of the `f` function in `[0]`
- `[2]` — number of iterations performed
- `[3]` — error indicator, possible values:
    - `0` — the method was convergent in this case
    - `1` — given solution is not within the given precision parameters because of not enough iterations
    - `2` — the derivative function was near zero

"""
function mstycznych(f, pf, x0::FL, delta::FL, epsilon::FL, maxint::Int)

    v = f(x0)

    if abs(v) < epsilon
        # given x₀ is already within given precision
        return (x0, v, 0, 0)
    end

    # iterate until the MAX_ITERATIONS is reached or the precision is satisfied
    xn = x0
    xn1 = x0

    # predefine the iterator so it would be accessible outside the loop
    k = 0
    # iterate
    for k in 1:maxint

        # perform the recursive step
        xn1 = xn - (v/pf(xn))
        v = f(xn1)

        # check the derivative
        if abs(pf(xn)) < NEAR_ZERO || isinf(abs(pf(xn)))
            # the derivative function is near zero which could lead to a not very precise solution
            return (xn, f(xn), k, 2)
        end

        # if the solution is within given precision return the output values
        if abs(xn1 - xn) < delta || abs(v) < epsilon
            return (xn1, v, k, 0)
        end

        # otherwise continue iterating
        xn = xn1

    end

    # not enough iterations to satisfy given precision
    return (xn1, v, k, 1)

end

"""
### Finds the solution to the equation `f(x) = 0` using the secant method.

### Arguments
- `f` — the function to find a root of
- `x0` — the first approximation
- `x1` — the second approximation
- `delta` — the precision of the solution in terms of the X axis
- `epsilon` — the precision of the solution in terms of the Y axis
- `maxint` — maximum iterations this function can perform

### Return value: a tuple of four values
- `[0]` — the approximation of the root of the `f` function
- `[1]` — the actual value of the `f` function in `[0]`
- `[2]` — number of iterations performed
- `[3]` — error indicator, possible values:
    - `0` — the method was convergent in this case
    - `1` — given solution is not within the given precision parameters because of not enough iterations

"""
function msiecznych(f, x0::FL, x1::FL, delta::FL, epsilon::FL, maxint::Int)

    # calc the first values
    v = f(x0)
    w = f(x1)
    a = x0
    b = x1

    # predefine the iterator so it would be accessible outside the loop
    k = 0
    #iterate
    for k in 0:maxint

        if abs(v) > abs(w)
            # swap the values, if necessary to maintain the order such that the latter value (`f(b)`) is equal or bigger than former (`f(a)`)
            # because of that the absolute value of the function will not rise — and that’s what we want since we’re calculating the root of the `f` function
            a,b = b,a
            v,w = w,v
        end

        # calculate the pseudo-derivative
        d = (b-a)/(w-v)
        # shift the values
        b = a
        w = v
        # calc the next value
        a = a - d * v
        v = f(a)

        if abs(v) < epsilon || abs(b-a) < delta
            # given solution is within given precision
            return (a, v, k, 0)
        end

    end

    # not enough iterations to give an accurate solution (not within given precision)
    return (a, v, k, 1)

end

end
