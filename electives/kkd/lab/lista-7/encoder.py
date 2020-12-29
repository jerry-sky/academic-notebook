#!/usr/bin/env python3
from sys import exit, argv
from utilities import *

# define the basic (meaning like in Humming's (7,4) code) parity bits indicies
BASIC_PARITY_DEFINITION = [
    [1, 2, 4],
    [1, 3, 4],
    [2, 3, 4]
]


def encode(block: int) -> int:
    """Encodes a single 4 bit block into a Humming coded 8 bit block.
    """
    output = 0

    # calc all the basic parity bits
    basic_parity = [
        sum([get_nth_bit(block, n) for n in parity_def]) % 2
        for parity_def in BASIC_PARITY_DEFINITION
    ]

    # assemble the first seven bits
    # p_1 through p_2
    for i in range(0, 2):
        output += basic_parity[i]
        output <<= 1
    # i_1
    output += get_nth_bit(block, 1)
    output <<= 1
    # p_3
    output += basic_parity[2]
    output <<= 1
    # i_2 through i_4
    for i in range(2, 4+1):
        output += get_nth_bit(block, i)
        output <<= 1

    # calc the last parity bit
    output += sum([
        get_nth_bit(output, n, blocksize=8)
        for n in range(1, 7+1)]
    ) % 2

    return output


if __name__ == "__main__":

    if len(argv) < 3:
        exit('usage: ./<encoder.py|koder> <input file> <output file>')

    input_file = argv[1]
    output_file = argv[2]

    with open(input_file, 'rb+') as fi, open(output_file, 'wb+') as fo:
        # read one byte
        inp = fi.read(1)
        while inp:

            inp = ord(inp)

            # split said byte into two 4 bit parts
            part_one = inp >> 4
            part_two = inp & 0b1111

            # encode the two blocks and save them
            fo.write(bytes([encode(part_one)]))
            fo.write(bytes([encode(part_two)]))

            inp = fi.read(1)
