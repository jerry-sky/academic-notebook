from typing import List

from gamma_coding import GammaCoding
from bitwiseio import BitReader, BitWriter


class DeltaCoding(object):

    @staticmethod
    def encode_number(input_number: int) -> str:
        """Encode a single number
        """
        binary = bin(input_number)[2:]
        n = len(binary)
        return GammaCoding.encode_number(n) + binary[1:]

    @staticmethod
    def decode_number(input_number: str) -> int:
        n = GammaCoding.decode_number(input_number)
        n -= 1
        print("n", n)
        x = input_number[-n:]
        print("x", x)
        return int(x, 2) + (2**(n) if n > 0 else 0)

    @staticmethod
    def encode(input_numbers: List[int], output_file: str) -> None:
        with open(output_file, "wb+") as f:
            with BitWriter(f) as writer:
                for number in input_numbers:
                    encoded = DeltaCoding.encode_number(number)
                    for bit in encoded:
                        if bit == "1":
                            writer.writebits(1, 1)
                        else:
                            writer.writebits(0, 1)

    @staticmethod
    def decode(input_file: str) -> List[int]:
        with open(input_file, "rb") as f:
            with BitReader(f) as reader:
                output = []
                while True:
                    bit = reader.readbits(1)
                    i = 0
                    while bit != 1:
                        i += 1
                        bit = reader.readbits(1)
                    if not reader.read:
                        break
                    n = 2**i + reader.readbits(i)
                    n -= 1
                    output.append(2**n + reader.readbits(n))
                return output
