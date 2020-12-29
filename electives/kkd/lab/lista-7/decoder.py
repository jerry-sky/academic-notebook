#!/usr/bin/env python3
from sys import exit, argv
from utilities import *

# define the basic (meaning like in Humming's (7,4) code) parity bits indicies
INTEGRITY_BITS_DEFINITION = [
    [1, 3, 5, 7],
    [2, 3, 6, 7],
    [4, 5, 6, 7]
]
# please note: the columns are represented horizontally here rather than vertically
PARITY_CHECK_MATRIX = [
    [],  # dummy column to maintain the global rule of starting indexes at 1
    [1, 0, 0, 1],
    [0, 1, 0, 1],
    [1, 1, 0, 1],
    [0, 0, 1, 1],
    [1, 0, 1, 1],
    [0, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 1]
]


def decode(block: int) -> (int, bool):
    """Encodes a single 8 bit block of a Humming codeword back to
    the original 4 bit block. Returns the original block and boolean
    equal to True if there were two uncorrectable errors.
    """
    # calc the basic syndrome
    basic_syndrome = [
        sum([get_nth_bit(block, n, blocksize=8) for n in integrity_def]) % 2
        for integrity_def in INTEGRITY_BITS_DEFINITION
    ]

    # calc the parity syndrome
    parity_syndrome = sum([get_nth_bit(block, n, blocksize=8)
                           for n in range(1, 8+1)]) % 2

    bit_to_fix_index = 0
    uncorrectable_error = False

    if sum(basic_syndrome) != 0 and parity_syndrome == 1:
        # codeword is incorrect - fix based on the outcome of the basic syndrome
        bit_to_fix_index = PARITY_CHECK_MATRIX.index(basic_syndrome + [parity_syndrome])
    elif sum(basic_syndrome) == 0 and parity_syndrome == 1:
        # codeword is incorrect - fix based on the outcome of the parity syndrome
        # (the last bit needs to be fixed)
        bit_to_fix_index = 8
    elif sum(basic_syndrome) != 0 and parity_syndrome == 0:
        # codeword is incorrect - uncorrectable error
        uncorrectable_error = True

    # first, fix the codeword if necessary
    if bit_to_fix_index > 0:
        if get_nth_bit(block, bit_to_fix_index, blocksize=8) == 1:
            block -= (1 << (8-bit_to_fix_index))
        else: # == 0
            block += (1 << (8-bit_to_fix_index))

    # take out the actual 4 bit block that contains sent information
    indicies = [3, 5, 6, 7]
    output = 0
    for index in indicies:
        output += get_nth_bit(block, index, blocksize=8)
        output <<= 1

    return output >> 1, uncorrectable_error


if __name__ == "__main__":

    if len(argv) < 3:
        exit('usage: ./<decoder.py|dekoder> <input file> <output file>')

    input_file = argv[1]
    output_file = argv[2]

    uncorrectable_errors = 0

    with open(input_file, 'rb+') as fi, open(output_file, 'wb+') as fo:
        # read two bytes to decode
        inp = fi.read(2)
        while inp:
            # decode the two bytes
            inp = list(inp)
            one, error_one = decode(inp[0])
            two, error_two = decode(inp[1])
            fo.write(bytes([(one << 4) + two]))
            # collect all the errors
            uncorrectable_errors += int(error_one) + int(error_two)

            inp = fi.read(2)

    print('uncorrectable errors:', uncorrectable_errors)
