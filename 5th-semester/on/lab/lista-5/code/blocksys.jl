#
# Jerzy Wroczyński (nr. indeksu 250075)
# Obliczenia Naukowe, Laboratorium
# Lista 5.
#

module blocksys

include("types.jl")
import .types.FL, .types.SquareSparseMatrix

using SparseArrays

# constants
macheps = eps(FL)

"""
### Asserts provided arguments match in size.

### Arguments:
- `A` — the `A` matrix
- `n` — the size of the matrix
- `b` — the `b` vector

### Returns: `Nothing`

"""
function assertMatrixSize(A, n::Int, b::Vector=[0 for _ in 1:n])::Nothing

    # if size(A, 1) == size(A, 2) == n == length(b)
    if n == length(b)
        return
    end

    throw(ErrorException("provided arguments do not match in sizes"))

end

"""
### Asserts `n` is divisible by `l`.

### Arguments:
- `A` — the `A` matrix
- `n` — the size of the matrix
- `b` — the `b` vector

### Returns: `Nothing`

"""
function assertBlockSize(n::Int, l::Int)::Nothing

    if n%l != 0
        throw(ErrorException("n is not divisible by l"))
    end

end

"""
### Calculates the permutation vector of given matrix.
This function implements the *partial pivoting* algorithm that assures that the diagonal of the matrix contains numbers that are not near zero or equal to zero.

### Arguments:
- `A` — the `A` matrix
- `n` — size of the matrix
- `l` — size of each chunk (submatrix)
- `limited` — this flag limits the bounds of the searching loop; it may be used when the function gives a permutation that leads to having a value near zero on the diagonal of the matrix; default value is set to `false`

### Returns
— the pivot vector that simulates all the matrix rows swaps that would have occurred

"""
function partialPivot(A, n::Int, l::Int, limited::Bool = false)::Vector

    assertMatrixSize(A, n)
    assertBlockSize(n, l)

    # save the new order of the rows
    pivot = [x for x in 1 : n]

    for k in 1:Int(n/l)

        for p in (k-1)*l+1 : k*l
            # get current value
            curr = abs(A[pivot[p], p])

            # check if it’s the biggest value
            max_value = curr
            max_index = pivot[p]
            search_end = limited ? k*l : k*l + l
            for i in (p+1) : search_end

                # special case for k=n/l
                # because this is the last submatrix there are no submatrices underneath;
                # thus,the internal loop used for searching max value needs to step earlier
                if i > n
                    break
                end
                # get another value from that column
                potential = A[pivot[i], p]
                if abs(potential) > max_value
                    # its absolute value is bigger — mark as ready for swap
                    max_value = abs(potential)
                    max_index = pivot[i]
                end
            end
            if max_value < macheps
                throw(ErrorException("a value near or equal zero was selected as the main value (diagonal value) — try to run `partialPivot` with `limited` set to `true` or do not use pivoting for this particular case at all"))
            end
            # swap the rows if needed
            if max_value > curr
                pivot[p], pivot[max_index] = pivot[max_index], pivot[p]
            end

        end

    end

    return pivot

end

"""
### Gives LU decomposition of given matrix.

### Arguments:
- `A` — the matrix to decompose
- `b` — the `b` vector (the vector that is on the right side of the `Ax = b` equation)
- `n` — the size of the matrix
- `l` — size of each chunk (submatrix)
- `pivot` — optional pivoting vector that simulates matrix row swap (can be generated using the `partialPivot` function); default value is set to a linear vector [1,…,n]

### Returns a tuple:
- `[1]` — matrices `L` and `U` contained in one matrix for optimization
- `[2]` — altered `b' = b^{(k)}` vector

"""
function decomposeIntoLU(A, b::Vector, n::Int, l::Int, pivot::Vector = [x for x in 1:n])#::Tuple{types.SquareSparseMatrix, Vector}

    assertMatrixSize(A, n)
    assertBlockSize(n, l)

    # this a more optimized way of storing both L and U matrices
    # we copy `A` at the beginning because that’s the start of the sequence:
    # A^{(1)} → A^{(2)} → … → A^{(n)} = U
    # in the end both matrices are triangular, so there is no problem with storing them this way
    # and the `L` matrix does not store any information on the diagonal of the matrix so there is no collision between `U` and `L`
    LU = copy(A)

    bprime = copy(b)

    # these two adjacent `for` loops are just one loop split into `l`-sized chunks
    # — its time complexity is still O(n)
    for k in 1:Int(n/l)
        for p in (k-1)*l+1 : k*l

            # update all rows beneath
            for i in (p+1) : k*l + l
                # special case k = n/l
                if i > n
                    break
                end

                lᵢₚ = LU[pivot[i], p] / LU[pivot[p], p]

                # process the row with new coefficients
                for j in p : k*l + l
                    if j > n
                        break
                    end
                    LU[pivot[i], j] = LU[pivot[i], j] - lᵢₚ * LU[pivot[p], j]
                end

                # adjust the `b` matrix accordingly
                bprime[pivot[i]] = bprime[pivot[i]] - lᵢₚ * bprime[pivot[p]]

                # save the `L` matrix part
                LU[pivot[i], p] = lᵢₚ
            end
        end
    end

    return LU, bprime

end

"""
### Solves the standard equation `Ux = y` where `L` is an upper-triangular matrix.

### Arguments:
- `U` — the upper-triangular matrix
- `y` — the right side of the equation
- `n` — the size of the matrix
- `l` — size of each chunk (submatrix)
- `pivot` — optional pivoting vector that simulates matrix row swap (can be generated using the `partialPivot` function); default value is set to a linear vector [1,…,n]

### Returns
— the `x` output vector (solution to the `Ux = y` equation)

"""
function solveUpperTriangularMatrix(U, y::Vector, n::Int, l::Int, pivot::Vector = [x for x in 1:n])::Array

    # init the output vector
    x = [0.0 for _ in 1:n]

    # calc the values of the output vector
    for k in Int(n/l) : -1 : 1
        for p in k*l : -1 : (k-1)*l+1

            tmp = y[pivot[p]]
            for i in (p+1) : (k*l + l)
                if i > n
                    break
                end
                tmp -= x[pivot[i]] * U[pivot[p], i]
            end
            x[pivot[p]] = tmp/U[pivot[p], p]

        end
    end

    return x

end

"""
### Solves the `LUx = b` equation.

### Arguments:
- `LU` — LU decomposition of a given matrix
- `b` — the `b` vector (the right side of the `LUx = b` equation)
- `n` — the size of the matrix
- `l` — size of each chunk (submatrix)
- `pivot` — optional pivoting vector that simulates matrix row swap (can be generated using the `partialPivot` function); default value is set to a linear vector [1,…,n]

### Returns
— the `x` output vector (solution to the `LUx = b` equation)

"""
function solveFromLU(LU, b::Vector, n::Int, l::Int, pivot::Vector = [x for x in 1:n])::Array

    # Ly = b

    y = zeros(n)

    # calc the values of the intermediary vector
    for k in 1:Int(n/l)
        for p in (k-1)*l+1 : k*l

            tmp = b[pivot[p]]
            for i in (p-1) : -1 : (k-1)*l - l
                if i <= 0
                    break
                end
                tmp -= y[pivot[i]] * LU[pivot[p], i]
            end

            y[pivot[p]] = tmp#/1

        end
    end

    # Ux = y
    return solveUpperTriangularMatrix(LU, y, n, l, pivot)

end

"""
### Solves the `Ax = b` equation.

### Arguments:
- `A` — the input matrix
- `b` — the `b` vector (the right side of the `LUx = b` equation)
- `n` — the size of the matrix
- `l` — size of each chunk (submatrix)
- `pivot` — optional pivoting vector that simulates matrix row swap (can be generated using the `partialPivot` function); default value is set to a linear vector [1,…,n]

### Returns
— the `x` output vector (solution to the `Ax = b` equation)

"""
function gaussianElimination(A, b::Vector, n::Int, l::Int, pivot::Vector = [x for x in 1:n])::Array

    # get the `U` matrix and `b'`
    # here we don’t actually need the `L` matrix, but it is generated either way — but that doesn’t affect performance
    LU, bprime = decomposeIntoLU(A, b, n, l, pivot)

    return solveUpperTriangularMatrix(LU, bprime, n, l, pivot)

end

"""
### Generates the `b` vector with respect to given `A` matrix.
*(Assuming `x` is a vector of ones.)*

### Arguments:
- `A` — the input matrix
- `n` — the size of the matrix
- `l` — size of each chunk (submatrix)

### Returns
— the `b` vector

"""
function generateB(A, n::Int, l::Int)::Vector

    b = zeros(n)

    for k in 1:Int(n/l)
        for p in (k-1)*l+1 : k*l

            for j in k : k*l + l
                if j > n
                    break
                end
                b[p] += A[p, j]
            end

        end
    end

    return b

end

end
