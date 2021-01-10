
module testdata

# types
include("types.jl")
import .types.FL, .types.SquareSparseMatrix, .types.CustomSquareSparseMatrixRawPairs

include("test-data/external.jl")
using .matrixgen

include("utilities.jl")
using .utilities

include("blocksys.jl")
using .blocksys

"""
### Generates a set of test data
— two files containing the `A` matrix and the `b` vector. Generated files are contained in directory of name `test-data/n‹n›/` with filenames `A.txt` and `b.txt`.

### Arguments:
- `n` size of the matrix
- `l` size of each chunk (submatrix)

### Returns a tuple of paths to the testfiles:
- `[1]` — path to the `A` matrix file
- `[2]` — path to the `b` vector file

"""
function generateTestData(n::Int, l::Int)::Tuple{String, String}

    # first check if there are no files
    outputdirectory = string("test-data/n", string(n), "/")
    outputfile_A = string(outputdirectory, "A.txt")
    outputfile_b = string(outputdirectory, "b.txt")

    if isfile(outputfile_A) && isfile(outputfile_b)
        # there are already some testfiles generated
        return outputfile_A, outputfile_b
    end

    # generate a new directory for these testfiles
    mkpath(outputdirectory)

    # first generate the main matrix using an external script by D.Phil. hab. Paweł Zieliński
    matrixgen.blockmat(n, l, 16.0, outputfile_A)

    # read the `A` matrix
    A = utilities.Amatrix(outputfile_A)

    # generate the `b` vector
    # b = blocksys.generateB(A, n, l)


    # write the `b` vector to another file
    open(outputfile_b, "w") do f

        # print the header
        println(f, n)

        for k in 1:Int(n/l)
            for p in (k-1)*l+1 : k*l
                b = 0
                for j in k : k*l + l
                    if j > n
                        break
                    end
                    b += A[p, j]
                end

                println(f, b)

            end
        end

        # write the contents of the `b` vector in `n` following lines
        # for i in 1:n
        #     println(f, b[i])
        # end

    end

    return outputfile_A, outputfile_b

end

end
