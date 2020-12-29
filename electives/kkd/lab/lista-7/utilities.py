
def get_nth_bit(block, n, blocksize=4) -> int:
    """Returns n-th bit in a `blocksize` bit block counting from left,
    bit indexes start at 1.
    """
    return block >> (blocksize-n) & 0b1
