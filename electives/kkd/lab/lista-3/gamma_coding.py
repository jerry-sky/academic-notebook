from typing import List

from bitwiseio import BitReader, BitWriter


class GammaCoding(object):

    @staticmethod
    def encode_number(input_number: int) -> str:
        binary = bin(input_number)[2:]
        n = len(binary)
        return ("0" * (n-1)) + binary

    @staticmethod
    def decode_number(input_number: str) -> int:
        digit = input_number[0]
        i = 0
        while digit == "0":
            i += 1
            digit = input_number[i]
        x = input_number[i:]
        x = x[:i+1]
        return int(x, 2)

    @staticmethod
    def encode(input_numbers: List[int], output_file: str) -> None:
        with open(output_file, "wb+") as f:
            with BitWriter(f) as writer:
                for number in input_numbers:
                    encoded = GammaCoding.encode_number(number)
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
                    n = 0
                    while bit != 1:
                        n += 1
                        bit = reader.readbits(1)
                    if not reader.read:
                        break
                    output.append(2**n + reader.readbits(n))
                return output
