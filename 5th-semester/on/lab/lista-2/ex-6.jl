#!/usr/bin/env julia
#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 2, Zadanie 6.
#

# to avoid writing `global` wrap the entire program inside of a function
function program()

    # default case
    k = "1"

    # the first argument correlates to the considered case in the exercise
    if length(ARGS) != 1
        println("usage: ./ex-6.jl <number between 1-7>")
        exit(1)
    end
    k = ARGS[1]

    # if k == "1"
    c = -2
    x₀= 1

    if k == "2"
        c = -2
        x₀= 2
    elseif k == "3"
        c = -2
        x₀= 1.99999999999999
    elseif k == "4"
        c = -1
        x₀= 1
    elseif k == "5"
        c = -1
        x₀= -1
    elseif k == "6"
        c = -1
        x₀= 0.75
    elseif k == "7"
        c = -1
        x₀= 0.25
    end

    # iterate and print out the results
    x = x₀
    for n in 1:40

        x = x^2 + c

        print(
            "(", n, ",", x, ") "
        )

    end
    # put a newline at the end of the program
    println()

end

program()
