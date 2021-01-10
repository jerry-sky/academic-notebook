
module types

FL = Float64

CustomSquareSparseMatrixRawPairs = Array{Pair{String, FL}}

mutable struct SquareSparseMatrix

    dict::Dict

    """
    ### Initializes new `CustomSquareSparseMatrix` object from an array of pairs.

    """
    function SquareSparseMatrix(init::CustomSquareSparseMatrixRawPairs)
        return new(Dict(init))
    end

    function SquareSparseMatrix(init::Dict)
        return new(init)
    end

end

# define some utility methods for this new type
function Base.getindex(obj::SquareSparseMatrix, i, j)
    return get(obj.dict, string(i, " ", j), 0)
end

function Base.setindex!(obj::SquareSparseMatrix, v, i, j)
    key = string(i, " ", j)
    # if v == 0
    #     delete!(obj.dict, key)
    # else
        obj.dict[key] = v
    # end
end

function Base.copy(obj::SquareSparseMatrix)
    dict = copy(obj.dict)
    return SquareSparseMatrix(dict)
end

export FL, SquareSparseMatrix, CustomSquareSparseMatrixRawPairs

end
