#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 5.
#
module utilities

include("types.jl")
import .types.FL, .types.SquareSparseMatrix, .types.CustomSquareSparseMatrixRawPairs

using SparseArrays
using LinearAlgebra

"""
### Reads the `A` matrix from a given file.

### Arguments:
- `filename` — a string containing a path to the file

### Returns
— a sparse matrix containing contents of the provided file

"""
function Amatrix(filename::String, useCustomSparseMatrixSolution::Bool=true)

    lines = (x for x in eachline(filename))
    header = iterate(lines)[1]

    # read the header containing the size of the matrix and the size of submatrices
    n, l = [parse(Int, x) for x in split(header)]

    if n % l != 0
        throw(ErrorException("`n` is not divisible by `l`"))
    end

    let matrix
    end

    # initiate the matrix
    if useCustomSparseMatrixSolution
        v = Int(n/l)
        _size = (v-1) * l * 2 + l^2 * v
        matrix = CustomSquareSparseMatrixRawPairs(undef, _size)
    else
        matrix = spzeros(n, n)
    end

    # load the data into a sparse matrix
    i = 1
    for line in lines

        # parse
        x, y, v = [parse(FL, i) for i in split(line)]
        x = Int(x)
        y = Int(y)

        # save read value
        if useCustomSparseMatrixSolution
            matrix[i] = string(x, " ", y) => v
        else
            matrix[x,y] = v
        end

        i += 1
    end

    if useCustomSparseMatrixSolution
        return SquareSparseMatrix(matrix)
    else
        return matrix
    end

end

function bmatrix(filename::String)::Vector{FL}

    lines = (x for x in eachline(filename))
    header = iterate(lines)[1]

    n = parse(Int, header)

    b = []

    for line in lines

        append!(b, [parse(FL, line)])

    end

    return b

end

function relativeError(x̃::Vector)
    n = length(x̃)
    return (norm(ones(n) - x̃)/norm(ones(n)))
end

function writexvector(x̃::Vector, filename::String, attachRelativeError::Bool = false)::Nothing

    n = length(x̃)

    open(filename, "w") do f

        if attachRelativeError
            println(f, relativeError(x̃))
        end

        # write the contents of the `x` vector in `n` following lines
        for i in 1:n
            println(f, x̃[i])
        end

    end

end

end
