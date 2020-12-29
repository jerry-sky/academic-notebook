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

    def calc_mse(self, colour: str):

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

    def calc_snr(self, colour: str):

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
