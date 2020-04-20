#!/usr/bin/env python3
from typing import List
from sys import exit, argv
from getopt import getopt

from bitwiseio import BitReader, BitWriter

from fibonacci_coding import FibonacciCoding
from gamma_coding import GammaCoding
from delta_coding import DeltaCoding
from omega_coding import OmegaCoding

from lzw import LZW

from entropy import Entropy
import os


if __name__ == "__main__":

    raw_args = argv[1:]

    optlist, args = getopt(raw_args, "", ["coding=", "mode="])

    usage_help = "usage: ./main.py --coding <fib|omega|gamma|delta> --mode <encoding|decoding> input_file output_file"

    if len(args) < 2:
        exit(usage_help)

    input_file = args[0]
    output_file = args[1]

    coding = OmegaCoding
    mode = None
    for opt, arg in optlist:
        if opt == "--coding":
            if arg == "fib":
                coding = FibonacciCoding
            elif arg == "delta":
                coding = DeltaCoding
            elif arg == "gamma":
                coding = GammaCoding
            else:
                coding = OmegaCoding
        elif opt == "--mode":
            if arg == "encoding":
                mode = "e"
            elif arg == "decoding":
                mode = "d"
            else:
                print("invalid --mode")
                exit(usage_help)

    if mode == "e":
        encoded = list(
            map(
                # offsetting the numbers by one because of universal coding limitations
                lambda x: x+1,
                LZW.encode(input_file)
            )
        )

        coding.encode(encoded, output_file)

        # print the stats
        print("encoded number list entropy:",
              Entropy.encoded_file_entropy(encoded))
        print("original file entropy      :",
              Entropy.original_file_entropy(input_file))

        original_size = os.path.getsize(input_file)
        encoded_size = os.path.getsize(output_file)
        print("original file size         :",
              original_size)
        print("encoded file size          :",
              encoded_size)
        print("compression rate           :",
              str(round(encoded_size/original_size * 100)) + r"% size of the original file")

    elif mode == "d":
        decoded = list(
            map(
                # offsetting the numbers by one because of universal coding limitations
                lambda x: x-1,
                coding.decode(input_file)
            )
        )

        decoded_original_bytes = LZW.decode(decoded)

        with open(output_file, "wb+") as f:
            for t in decoded_original_bytes:
                f.write(t)
