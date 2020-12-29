#!/usr/bin/env julia
#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 2, Zadanie 1.
#

# assert ARGS
err_mess = "provide two arguments: [64, 32] [up, down, max_to_min, min_to_max]"
if length(ARGS) != 2
    println(err_mess)
    exit(1)
end

# name the arguments
fl_str = ARGS[1]
mode = ARGS[2]

# parse the arguments
if !in(fl_str, ["64", "32"]) || !in(mode, ["up", "down", "max_to_min", "min_to_max"])
    println(err_mess)
    exit(1)
end

fl = Float64

# apply the first argument
if fl_str== "32"
    global fl = Float32
end
# end assert

# x₄ and x₅ were altered
x = [2.718281828, -3.141592654, 1.414213562, 0.577215664, 0.301029995]
y = [1486.2497, 878366.9879, -22.37492, 4773714.647, 0.000185049]

function calc_scalar_product(x, y)
    S = fl(0)
    # (a), (b)
    if in(mode, ["up", "down"])
        # change the direction of the range depending on the provided program argument
        for i in (mode == "down" ? (5:-1:1) : (1:5))
            S = fl(S + fl(x[i] * y[i]))
        end
    # (c), (d)
    elseif in(mode, ["max_to_min", "min_to_max"])
        # save partial products
        mid_positive::Array{fl} = []
        mid_negative::Array{fl} = []
        # iterate over the vectors
        for i in (1:5)
            out = fl(x[i] * y[i])
            if out < fl(0)
                push!(mid_negative, out)
            else
                push!(mid_positive, out)
            end
        end

        # sort the partial products
        sort!(mid_negative, rev=(mode == "max_to_min"))
        sort!(mid_positive, rev=(mode == "max_to_min"))

        # add the partial products
        S_positive = fl(0)
        S_negative = fl(0)
        for i in (1:length(mid_negative))
            S_negative = fl(S_negative + mid_negative[i])
        end
        for i in (1:length(mid_positive))
            S_positive = fl(S_positive + mid_positive[i])
        end
        # finally, add the partial sums
        S = fl(S_positive + S_negative)
    end
    return S
end

# print out the results
println(calc_scalar_product(x,y))
