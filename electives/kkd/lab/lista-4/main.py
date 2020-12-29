#!/usr/bin/env python3
from typing import List, Tuple, Iterable
from entropy import Entropy, JPEG_LS_METHODS
from pixel import *
from sys import argv, exit


def one_byte(f) -> int:
    """Read one byte and return it as an integer.
    """
    return ord(f.read(1))


def byte_list(f, count: int) -> Tuple[int]:
    """Read `count` bytes and return it as a tuple of integers.
    """
    return tuple(int(x) for x in f.read(count))


def int_from_bytes(bytes_) -> int:
    """Calculates
    """
    output = 0
    for i in range(0, len(bytes_)):
        output += bytes_[i] * (2**(8*i))
    return output


def img_analysis(image_path: str):

    counter = Entropy()

    with open(image_path, 'rb+') as f:
        # read the header
        id_length = one_byte(f)
        colour_map_type = one_byte(f)
        image_type = one_byte(f)
        # colour map specification
        first_entry_index = byte_list(f, 2)
        colour_map_length = byte_list(f, 2)
        colour_map_entry_size = ord(f.read(1))
        # image specification
        x_origin = byte_list(f, 2)
        y_origin = byte_list(f, 2)
        image_width = int_from_bytes(byte_list(f, 2))
        image_height = int_from_bytes(byte_list(f, 2))
        pixel_depth = one_byte(f)
        image_descriptor = one_byte(f)

        # create a two-line pixel buffer
        # the pixel on the most left is always black
        # 0 -> top row
        # 1 -> current row
        buffer = [
            [(0, 0, 0) for _ in range(0, image_width+1)]
            for _ in [1, 2]
        ]
        # load the first row of pixels
        for pixel in range(1, image_width+1):
            # for every pixel load three bytes represeting BGR colours
            buffer[0][pixel] = byte_list(f, 3)

        for line in range(0, image_height):
            # take the top row as the current one
            # (use switching as a hackaround, because of pointers)
            buffer[1], buffer[0] = buffer[0], buffer[1]
            # and load another row on top
            if line != image_height-1:
                for pixel in range(1, image_width+1):
                    buffer[0][pixel] = byte_list(f, 3)
            else:
                # if this is the last row, the top row needs to be
                # a row of black pixels
                for pixel in range(1, image_width+1):
                    buffer[0][pixel] = (0, 0, 0)

            # loop through the loaded pixels
            for i in range(1, image_width+1):
                pixel = buffer[1][i]
                west = buffer[1][i-1]
                north = buffer[0][i]
                northwest = buffer[0][i-1]

                # do all the predictions

                # \hat{X} = (0,0,0)
                counter.register_char('normal', pixel)
                # \hat{X} = W
                hat_x = west
                counter.register_char('W', subtract_pixels(pixel, hat_x))
                # \hat{X} = N
                hat_x = north
                counter.register_char('N', subtract_pixels(pixel, hat_x))
                # \hat{X} = NW
                hat_x = northwest
                counter.register_char('NW', subtract_pixels(pixel, hat_x))
                # \hat{X} = N + W - NW
                hat_x = subtract_pixels(
                    add_pixels(
                        north,
                        west
                    ),
                    northwest
                )
                counter.register_char(
                    'N + W - NW', subtract_pixels(pixel, hat_x))
                # \hat{X} = N + (W - NW)/2
                hat_x = add_pixels(
                    north,
                    scale_pixel(
                        subtract_pixels(west, northwest),
                        0.5
                    )
                )
                counter.register_char(
                    'N + (W - NW)/2', subtract_pixels(pixel, hat_x))
                # \hat{X} = W + (N - NW)/2
                hat_x = add_pixels(
                    west,
                    scale_pixel(
                        subtract_pixels(north, northwest),
                        0.5
                    )
                )
                counter.register_char(
                    'W + (N - NW)/2', subtract_pixels(pixel, hat_x))
                # \hat{X} = (N + W)/2
                hat_x = scale_pixel(
                    add_pixels(north, west),
                    0.5
                )
                counter.register_char(
                    '(N + W)/2', subtract_pixels(pixel, hat_x))
                # new standard
                hat_x = [0, 0, 0]
                # perform the algorithm for every colour discretely
                for i in range(0, 3):
                    if northwest[i] >= max(west[i], north[i]):
                        hat_x[i] = max(west[i], north[i])
                    elif northwest[i] <= min(west[i], north[i]):
                        hat_x[i] = min(west[i], north[i])
                    else:
                        hat_x[i] = west[i] + north[i] - northwest[i]
                hat_x = tuple(hat_x)
                counter.register_char(
                    'new standard', subtract_pixels(pixel, hat_x))

    return counter


if __name__ == '__main__':

    if len(argv) < 2:
        exit('usage: ./main.py <input file>')

    img_path = argv[1]

    results = img_analysis(img_path)

    modes = ['pixels', 'red', 'green', 'blue']

    lowest_entropy = dict()
    lowest_entropy_method = dict()

    # initialize
    for mode in modes:
        lowest_entropy[mode] = float('inf')
        lowest_entropy_method[mode] = 'normal'

    for method in JPEG_LS_METHODS:
        print(method + ':')
        for mode in modes:
            r = results.calc_entropy(method, mode)
            if r < lowest_entropy[mode]:
                lowest_entropy[mode] = r
                lowest_entropy_method[mode] = method
            print(mode.rjust(8) + ':', r)
        print()
    print('best predicate:')
    for mode in modes:
        print(mode.rjust(8) + ':', lowest_entropy_method[mode])

    print()
