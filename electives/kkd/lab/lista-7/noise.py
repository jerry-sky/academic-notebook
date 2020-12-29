#!/usr/bin/env python3
from sys import exit, argv
from random import random
from utilities import *

if __name__ == "__main__":

    if len(argv) < 4:
        exit('usage: ./<noise.py|szum> <mutation probability> <input file> <output file>')

    mutation_probability = 0
    try:
        mutation_probability = float(argv[1])
    except ValueError:
        exit('mutation probability has to be a float of format `x.y`')

    input_file = argv[2]
    output_file = argv[3]

    with open(input_file, 'rb+') as fi, open(output_file, 'wb+') as fo:
        # read one byte
        inp = fi.read(1)
        while inp:

            inp = ord(inp)

            for i in range(1, 8+1):
                if random() > 1-mutation_probability:
                    if get_nth_bit(inp, i, blocksize=8) == 1:
                        inp -= (1 << (8-i))
                    else: # == 0
                        inp += (1 << (8-i))

            fo.write(bytes([inp]))


            inp = fi.read(1)

