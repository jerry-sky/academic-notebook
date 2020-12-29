#!/usr/bin/env python3
from typing import List, Tuple, Iterable
from sys import argv, exit, stderr
from getopt import getopt
from bitwiseio import BitReader, BitWriter
from bitpack_utility import *
from tga_utility import *


def add_pixels_mod(one: Tuple[int], two: Tuple[int]):
    """Adds two pixels' values together and keeps them in range of [0,255].
    """
    return tuple(
        (one[i] + two[i]) % 256 for i in range(0, 3)
    )


def encode(input_image: str, output_file: str, bitdepth: int) -> None:
    """Encodes given image to a propriatory format file with a specialized
    header on top of the original file's TGA header.
    """

    with open(input_image, 'rb+') as fi:
        with BitReader(fi) as reader:
            with open(output_file, "wb+") as fo:
                with BitWriter(fo) as writer:
                    # copy the original header over and read image dimensions
                    image_width, image_height = read_and_write_tga_header(
                        reader, writer)

                    # write a propriatory header that contains the bitdepth
                    writer.writebits(bitdepth, 8)

                    # start encoding from \vec0
                    previous_pixel = (0, 0, 0)

                    for _ in range(image_width * image_height):
                        current_pixel = bitpack_list(reader, 3)
                        # iterate over all colours
                        quantized_difference = [0 for _ in range(3)]
                        for c in range(0, 3):
                            # calculate the difference and quantize it
                            quantized_difference[c] = \
                                (current_pixel[c] - previous_pixel[c])\
                                % 256\
                                >> (8-bitdepth)
                            # save the quantized difference
                            writer.writebits(quantized_difference[c], bitdepth)
                            # revert back to its original bit size
                            # (now without unnecessary bits)
                            quantized_difference[c] = quantized_difference[c] << (
                                8-bitdepth)

                        # replace the old pixel with the current one
                        previous_pixel = add_pixels_mod(
                            previous_pixel, quantized_difference)

                    # copy the original footer over
                    read_and_write_tga_footer(reader, writer)


def decode(input_file: str, output_image: str) -> None:
    """Decodes given binary file back to the original TGA image.
    Input file needs to be a binary file generated by the `encode` function.
    """

    with open(input_file, 'rb+') as fi:
        with BitReader(fi) as reader:
            with open(output_file, "wb+") as fo:
                with BitWriter(fo) as writer:

                    # copy the original header over and read image dimensions
                    image_width, image_height = read_and_write_tga_header(
                        reader, writer)

                    # read the propriatory header
                    bitdepth = one_bitpack(reader)

                    # start from a \vec0
                    previous_pixel = (0, 0, 0)

                    for _ in range(image_height * image_width):
                        # read the offset and bring back its original bitsize
                        current_offset = tuple(map(
                            lambda x: x << (8-bitdepth),
                            bitpack_list(reader, 3, size=bitdepth)
                        ))
                        # recreate a quantized pixel
                        previous_pixel = add_pixels_mod(
                            previous_pixel, current_offset)
                        # save recovered pixel
                        for c in range(0, 3):
                            t = previous_pixel[c]
                            writer.writebits(t, 8)

                    # recover the original file footer
                    read_and_write_tga_footer(reader, writer)


if __name__ == "__main__":

    raw_args = argv[1:]
    optlist, args = getopt(raw_args, '', ['mode='])

    usage_help = 'usage: ./main.py --mode <encode|decode> <input file> <output file> [bit depth]'

    if len(args) < 2 and len(optlist) < 1:
        exit(usage_help)

    input_file = args[0]
    output_file = args[1]
    bitdepth = None
    if len(args) >= 3:
        bitdepth = int(args[2])

    mode = None
    for opt, arg in optlist:
        if opt == '--mode':
            if arg == 'encode' and bitdepth is None:
                print('encode mode requires bit depth option')
                exit()
            elif arg == 'encode':
                mode = 'e'
            elif arg == 'decode':
                mode = 'd'
            else:
                print('invalid --mode')
                exit(usage_help)

    if mode == 'e':
        encode(input_file, output_file, bitdepth)
    else:  # mode == 'd'
        decode(input_file, output_file)
