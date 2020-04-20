from typing import List
from math import ceil


class LZW(object):
    """Implements the Lempel–Ziv–Welch algorithm for data compression.
    """

    @staticmethod
    def encode(input_file: str) -> List[int]:
        """Encodes a whole file into a binary file using LZW algorithm.
        """
        output = []

        dictionary = dict()
        for i in range(0, 256):
            dictionary[bytes([i])] = i

        # next codeword to be inserted into the `_dict` will get this index
        new_codeword_index = 256

        with open(input_file, "rb") as f:
            # first byte
            cur = f.read(1)
            while True:
                nex = f.read(1)
                if dictionary.get(cur + nex) is not None:
                    cur += nex
                else:
                    output.append(dictionary.get(cur))
                    dictionary[cur + nex] = new_codeword_index
                    new_codeword_index += 1
                    cur = nex

                if not nex:
                    break
            output.append(dictionary.get(cur))

        return output

    @staticmethod
    def decode(encoded: List[int]) -> List[str]:
        """Decodes list of LZW-encoded numbers back to original bytes.
        """
        output = []

        dictionary = dict()
        for i in range(0, 256):
            dictionary[i] = bytes([i])

        # next codeword to be inserted into the `_dict` will get this index
        new_codeword_index = 256
        # first number
        prev = encoded[0]
        prev_value = dictionary.get(prev)
        single = prev_value[0]
        output.append(prev_value)

        for curr in encoded[1:]:
            prev_value = b""
            if curr not in dictionary:
                prev_value = dictionary.get(prev)
                prev_value += single
            else:
                prev_value = dictionary.get(curr)
            output.append(prev_value)
            single = b""
            single += bytes([prev_value[0]])
            dictionary[new_codeword_index] = dictionary.get(prev) + single
            new_codeword_index += 1
            prev = curr

        return output
