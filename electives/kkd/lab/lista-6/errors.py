#!/usr/bin/env python3
from tga_utility import *
from bitpack_utility import *
from sys import exit, argv
from math import log10

COLOURS = ['blue', 'green', 'red']


class Errors(object):
    """Calculates the mean squared error (MSE) and
    signal-to-noise ratio (SNR) of an image.
    """

    def __init__(self):
        self._mse = dict()
        self._snr = dict()
        self._count = dict()
        for colour in COLOURS:
            self._mse[colour] = 0
            self._snr[colour] = 0
            self._count[colour] = 0

    def register_val(self, original_value: int, quantized_value: int, colour: str):
        """While quantizing an image, this method accumulates all summation components.
        """
        self._mse[colour] += (original_value - quantized_value) ** 2
        self._snr[colour] += original_value ** 2
        self._count[colour] += 1

    def calc_mse(self, colour: str = ''):

        if colour in COLOURS:
            return self._mse[colour] / self._count[colour]
        else:
            # calc as a whole pixel
            top = 0
            bottom = 0
            for c in COLOURS:
                top += self._mse[c]
                bottom += self._count[c]
            return top / bottom

    def calc_snr(self, colour: str = ''):

        top = 0
        bottom = 0
        if colour in COLOURS:
            # (1/N) / (1/N) = 1
            top = self._snr[colour]
            bottom = self._mse[colour]
        else:
            # calc as a whole pixel
            for c in COLOURS:
                top += self._snr[c]
                bottom += self._mse[c]
        if bottom > 0:
            return top / bottom
        else:
            return float('inf')


if __name__ == '__main__':

    if len(argv) < 3:
        exit('usage: ./errors.py <first image> <second image>')

    first_image = argv[1]
    second_image = argv[2]

    err = Errors()

    with open(first_image, 'rb+') as f1:
        with BitReader(f1) as reader1:
            with open(second_image, 'rb+') as f2:
                with BitReader(f2) as reader2:

                    # read files' headers
                    first_image_width, first_image_height = read_and_write_tga_header(
                        reader1, None)
                    image_width, image_height = read_and_write_tga_header(
                        reader2, None)

                    if image_width != first_image_width or image_height != first_image_height:
                        exit('images do not have the same sizes')

                    # iterate over all pixels in both files
                    for _ in range(image_width * image_height):
                        # read a pixel from the first file
                        pixel1 = bitpack_list(reader1, 3)
                        # read a pixel from the second file
                        pixel2 = bitpack_list(reader2, 3)
                        # register for every colour
                        i = 0
                        for c in COLOURS:
                            err.register_val(pixel1[i], pixel2[i], c)
                            i += 1

    # print the error measurements
    print('MSE   =', err.calc_mse())
    for colour in COLOURS[::-1]:
        print('MSE(' + colour[0] + ')=', err.calc_mse(colour))

    print('SNR   =', err.calc_snr(),
          '(' + str(10 * log10(err.calc_snr(''))) + ' dB)')
    for colour in COLOURS[::-1]:
        print('SNR(' + colour[0] + ')=', err.calc_snr(colour),
              '(' + str(10 * log10(err.calc_snr(colour))) + ' dB)')
