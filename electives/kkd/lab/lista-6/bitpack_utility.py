from bitwiseio import BitReader
from typing import Tuple

def one_bitpack(f: BitReader, size: int = 8) -> int:
    """Reads a series of `size` bits and returns it as an integer.
    Defaults to bitpack of size 8 bits (one byte).
    This function expects a `BitReader` that reads individual bits not bytes.
    """
    return f.readbits(size)


def bitpack_list(f: BitReader, count: int, size: int = 8) -> Tuple[int]:
    """Reads `count` bit packs and returns it as a tuple of integers.
    Defaults to bytes.
    This function expects a `BitReader` that reads individual bits not bytes.
    """
    return tuple(one_bitpack(f, size=size) for _ in range(count))


def int_from_bytes(bytes_) -> int:
    """Calculates an integer from provided bytes.
    """
    output = 0
    for i in range(0, len(bytes_)):
        output += bytes_[i] * (2**(8*i))
    return output
