from math import log2
from typing import List


class Entropy(object):
    """Calculates entropy for the original file and the LZW-encoded
    output number list.
    """

    def original_file_entropy(file_path: str) -> float:
        with open(file_path, "rb") as f:
            chars = dict()
            total_count = 0
            b = f.read(1)
            while b:
                if chars.get(b) is None:
                    chars[b] = 1
                else:
                    chars[b] += 1
                total_count += 1
                b = f.read(1)

            entropy = 0
            for c in list(chars.values()):
                entropy += c * (-log2(c))
            entropy /= total_count
            return entropy + log2(total_count)

    def encoded_file_entropy(encoded: List[int]) -> float:
        numbers = dict()
        total_count = 0
        for n in encoded:
            if numbers.get(n) is None:
                numbers[n] = 1
            else:
                numbers[n] += 1
            total_count += 1

        entropy = 0
        for n in list(numbers.values()):
            entropy += n * (-log2(n))
        entropy /= total_count
        return entropy + log2(total_count)

