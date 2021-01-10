#!/usr/bin/env julia
#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 5.
#

include("utilities.jl")
using .utilities

include("blocksys.jl")
using .blocksys

include("generate-a-test.jl")
using .testdata

global l = 4

global n = parse(Int, ARGS[1])

let A, b
end

# whether to run with classic built-in algorithm
classic = "classic" in ARGS

# whether to run using a custom sparse matrix solution
custom = "custom" in ARGS

# whether to run improved algorithm with pivoting
pivot = "pivot" in ARGS

# whether to run using the LU decomposition
lu = "lu" in ARGS

println(stderr, "loading data...")
if n == 16
    # read the already pregenerated testfiles
    A = utilities.Amatrix("test-data/n16/A.txt", custom)
    b = utilities.bmatrix("test-data/n16/b.txt")
else
    pathA, pathb = testdata.generateTestData(n, l)
    A = utilities.Amatrix(pathA, custom)
    b = utilities.bmatrix(pathb)
end

let x̃
end

println(stderr, "finding solution...")
@time if classic
    println(stderr, "classic algorithm")
    x̃ = A\b
else
    println(stderr, "improved algorithm")
    let pivot
    end

    # by default don’t perform pivoting
    pivot_ = [i for i in 1:n]

    if pivot
        # calculate the pivot row permutation vector
        pivot_ = blocksys.partialPivot(A, n, l, true)
    end

    if lu
        LU, _ = blocksys.decomposeIntoLU(A, b, n, l, pivot_)
        x̃ = blocksys.solveFromLU(LU, b, n, l, pivot_)
    else
        # calculate the `x` vector
        x̃ = blocksys.gaussianElimination(A, b, n, l, pivot_)
    end
end

# print relative error
println("relative error = ", utilities.relativeError(x̃))
