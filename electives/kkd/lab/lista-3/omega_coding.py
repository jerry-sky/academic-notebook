from typing import List
from bitwiseio import BitWriter, BitReader

class OmegaCoding(object):

    @staticmethod
    def encode_number(input_number: int) -> str:
        output = "0"
        k = input_number
        while k > 1:
            binary = bin(k)[2:]
            output = binary + output
            k = len(binary) - 1
        return output

    @staticmethod
    def decode_number(input_number: str) -> int:
        n = 1
        bit = input_number[0]
        while bit != "0":
            new_n = int(input_number[:n+1], 2)
            input_number = input_number[n+1:]
            n = new_n
            bit = input_number[0]
        return n

    @staticmethod
    def encode(input_numbers: List[int], output_file: str) -> None:
        with open(output_file, "wb+") as f:
            with BitWriter(f) as writer:
                offset = 0
                total_length = 0
                for number in input_numbers:
                    encoded = OmegaCoding.encode_number(number)
                    total_length += len(encoded)
                    for bit in encoded:
                        if bit == "1":
                            writer.writebits(1, 1)
                        else:
                            writer.writebits(0, 1)
                        offset += 1
                        offset %= 8
                # EOF is just padding made out of ones
                if offset > 0:
                    writer.writebits(255 >> offset, 8-offset)


    @staticmethod
    def decode(input_file: str) -> List[int]:
        with open(input_file, "rb") as f:
            with BitReader(f) as reader:
                output = []
                break_main_while = False
                while True:
                    n = 1
                    bit = reader.readbits(1)
                    while bit != 0:
                        n = (2 ** n) + reader.readbits(n)
                        bit = reader.readbits(1)
                        if not reader.read:
                            break_main_while = True
                            break
                    if break_main_while or not reader.read:
                        break
                    output.append(n)
                return output


