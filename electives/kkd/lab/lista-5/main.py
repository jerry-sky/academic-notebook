#!/usr/bin/env python3
from typing import List, Tuple, Iterable
from sys import argv, exit, stderr
from errors import Errors, COLOURS
from math import log10
import os


def one_byte(f) -> int:
    """Read one byte and return it as an integer.
    """
    return ord(f.read(1))


def byte_list(f, count: int) -> Tuple[int]:
    """Read `count` bytes and return it as a tuple of integers.
    """
    return tuple(int(x) for x in f.read(count))


def int_from_bytes(bytes_) -> int:
    """Calculates an integer from provided bytes.
    """
    output = 0
    for i in range(0, len(bytes_)):
        output += bytes_[i] * (2**(8*i))
    return output


def quantize(input_image: str, output_image: str, r_bits: int, g_bits: int, b_bits: int):

    err = Errors()

    with open(input_image, 'rb+') as fi:
        # read the the first part of the header
        header_header = byte_list(fi, 12)
        image_width_raw = byte_list(fi, 2)
        image_width = int_from_bytes(image_width_raw)
        image_height_raw = byte_list(fi, 2)
        image_height = int_from_bytes(image_height_raw)
        # read the rest of the header
        pixel_depth = one_byte(fi)
        image_descriptor = one_byte(fi)

        with open(output_image, 'wb') as fo:

            # copy the header over
            fo.write(bytes(header_header))
            fo.write(bytes(image_width_raw))
            fo.write(bytes(image_height_raw))
            fo.write(bytes([pixel_depth]))
            fo.write(bytes([image_descriptor]))
            # wrap the bits counts inside a convienient list
            colour_bits_count = [b_bits, g_bits, r_bits]

            # process the pixels
            for _ in range(0, image_height):
                for __ in range(0, image_width):
                    # take three bytes for each pixel (BGR *not* RGB)
                    pixel = byte_list(fi, 3)
                    quantized_pixel = []
                    for colour in [0, 1, 2]:
                        # how many bits have to be striped off
                        shift = 8 - colour_bits_count[colour]
                        q = pixel[colour]
                        if shift > 0:
                            # strip off unnecessary bits
                            q = q >> shift
                            # to make sure we've got a middle value of the range that comes from
                            # quantizing the pixel add a one and then fill out the rest with zeroes
                            q = q << 1
                            q += 1
                            if shift > 1:
                                q = q << shift-1
                        fo.write(bytes([q]))
                        # add appropriate values to SNR and MSE
                        err.register_val(pixel[colour], q, COLOURS[colour])

            # copy the footer over
            x = fi.read(1)
            while x:
                fo.write(x)
                x = fi.read(1)

    return err


def generate_all_RGB_combinations(pixel_bits_count: int):
    """Generates all possible combinations of bit spread across all colour channels.
    """
    for r in range(0, pixel_bits_count+1):
        for g in range(0, pixel_bits_count+1):
            for b in range(0, pixel_bits_count+1):
                if r + g + b == pixel_bits_count:
                    yield (r, g, b)


if __name__ == '__main__':

    if len(argv) < 5:
        exit('usage: ./main.py <input file> <output file> <bit depth (bits per pixel)> <bit spread measure: MSE|SNR>')

    input_image = argv[1]
    output_image = argv[2]
    pixel_depth = int(argv[3])
    bit_spread_measure = argv[4]

    tmp_output_image = '__tmp__' + output_image

    if bit_spread_measure not in ['MSE', 'SNR']:
        exit('invalid option for bit spread measure; only „MSE” or „SNR” are allowed')

    # go through all possible RGB spread combinations
    rgb_combinations = generate_all_RGB_combinations(pixel_depth)

    # run the first time so we have something to compare with
    best_bit_spread = next(rgb_combinations)
    best_results = quantize(input_image, output_image, *best_bit_spread)


    # go through the rest of the generated bit spreads
    for bit_spread in rgb_combinations:
        # store it in a separate file not to overwrite the best output image found so far
        results = quantize(input_image, tmp_output_image, *bit_spread)
        # if it is in fact better, replace the image with the newly generated one
        better = False
        if bit_spread_measure == 'MSE':
            # compare the highest MSE
            if max(results.calc_mse(c) for c in COLOURS) < max(best_results.calc_mse(c) for c in COLOURS):
                better = True
        else: # bit_spread_measure == 'SNR'
            # compare the lowest SNR
            if min(results.calc_snr(c) for c in COLOURS) > min(best_results.calc_snr(c) for c in COLOURS):
                better = True

        if better:
            best_results = results
            best_bit_spread = bit_spread
            # overwrite the existing best result file
            os.remove(output_image)
            os.rename(tmp_output_image, output_image)
            # report
            print('found a better bit spread!', str(best_bit_spread), file=stderr)

    # clean up
    if os.path.exists(tmp_output_image):
        os.remove(tmp_output_image)

    # print best bit spread
    print('RGB bit spread:', str(best_bit_spread))

    # print the error measurements
    print('MSE   =', best_results.calc_mse(''))
    for colour in COLOURS[::-1]:
        print('MSE(' + colour[0] + ')=', best_results.calc_mse(colour))

    print('SNR   =', best_results.calc_snr(''),
          '(' + str(10 * log10(best_results.calc_snr(''))) + ' dB)')
    for colour in COLOURS[::-1]:
        print('SNR(' + colour[0] + ')=', best_results.calc_snr(colour),
              '(' + str(10 * log10(best_results.calc_snr(colour))) + ' dB)')
