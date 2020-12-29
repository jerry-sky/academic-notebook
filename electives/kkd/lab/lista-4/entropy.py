from copy import deepcopy
from typing import Iterable
from math import log2
from decimal import Decimal
from sys import exit

# define all methods
JPEG_LS_METHODS = [
    'normal',  # original image
    'W',
    'N',
    'NW',
    'N + W - NW',
    'N + (W - NW)/2',
    'W + (N - NW)/2',
    '(N + W)/2',
    'new standard'
]


def rgb_hexify(rgb: Iterable[int]) -> str:
    """Convert a list of RGB numbers to a hex format.
    """
    return ''.join(
        list(map(
            lambda x: hex(abs(x))[2:].zfill(2),
            rgb
        ))[::-1]
    )


class Entropy(object):

    def __init__(self):
        # define a base object for counting how many times stuff occurred
        base_counter = {
            'pixels': dict(),
            'red': dict(),
            'green': dict(),
            'blue': dict()
        }
        # initialize all counters
        self.all_counters = dict()
        for method in JPEG_LS_METHODS:
            self.all_counters[method] = deepcopy(base_counter)

    def register_char(self, method: str, pixel) -> None:
        """Add the pixel to the method's counter.
        """
        # register the whole pixel
        red = pixel[2]
        green = pixel[1]
        blue = pixel[0]

        tmp = self.all_counters[method]

        # register the occurrence in all the counters

        for c in pixel:
            if tmp['pixels'].get(c) is None:
                tmp['pixels'][c] = 1
            else:
                tmp['pixels'][c] += 1

        if tmp['red'].get(red) is None:
            tmp['red'][red] = 1
        else:
            tmp['red'][red] += 1

        if tmp['green'].get(green) is None:
            tmp['green'][green] = 1
        else:
            tmp['green'][green] += 1

        if tmp['blue'].get(blue) is None:
            tmp['blue'][blue] = 1
        else:
            tmp['blue'][blue] += 1

    def calc_entropy(self, method, mode='pixels') -> float:
        """Calculate the entropy.

        Args:
            `method`: Calc entropy of the results of the `method` method.
            `mode`: Calc entropy of all whole 'pixels', or only for 'red,
                'green', 'blue'.
        """

        # output = 0
        output = Decimal(0)

        data = self.all_counters[method][mode].values()

        # total_count = sum(data)
        total_count = Decimal(sum(data))

        for x in data:
            # output += x * (-1 * log2(x))
            output += Decimal(x) * Decimal(-1 *
                                           Decimal(x).ln() / Decimal(2).ln())

        output /= total_count

        # return output + log2(total_count)
        return float(output + total_count.ln() / Decimal(2).ln())
