from typing import Tuple
from math import sqrt


def subtract_pixels(one, two) -> Tuple[int]:
    """Subtracts RGB values of two pixels.
    """
    return tuple((one[i] - two[i]) % 256 for i in range(0, 3))


def add_pixels(one, two) -> Tuple[int]:
    """Adds RGB values of two pixels.
    """
    return tuple((one[i] + two[i]) % 256 for i in range(0, 3))


def scale_pixel(one, factor) -> Tuple[int]:
    """Multiplies the pixel vector by a given factor.
    """
    return tuple(int(one[i] * factor) % 256 for i in range(0, 3))
