from typing import List
from sys import exit

from bitwiseio import BitReader, BitWriter


class FibonacciCoding(object):

    @staticmethod
    def nth_fib_number(n):
        if n < 2:
            return n
        return FibonacciCoding.nth_fib_number(n-1) + FibonacciCoding.nth_fib_number(n-2)

    @staticmethod
    def encode_number(input_number: int) -> str:
        """Encodes a single number into Fibonacci code.
        """
        # find the first number and set the output's length
        n = 2
        f_curr = FibonacciCoding.nth_fib_number(n)
        f_prev = f_curr
        while f_curr <= input_number:
            n += 1
            f_prev = f_curr
            f_curr = FibonacciCoding.nth_fib_number(n)
        output = 2**((n-1)-2)
        input_number -= f_prev

        # encode the rest of the number
        while input_number > 0:
            n = 2
            f_curr = FibonacciCoding.nth_fib_number(n)
            f_prev = f_curr
            while f_curr <= input_number:
                n += 1
                f_prev = f_curr
                f_curr = FibonacciCoding.nth_fib_number(n)
            output += 2**((n-1)-2)
            input_number -= f_prev

        return bin(output)[2:][::-1] + "1"

    def decode_number(input_number: str) -> int:
        """Decodes a single number back into int from Fibonacci code.
        """
        actual_number = input_number[:-1]
        output = 0
        i = 2
        for digit in list(actual_number):
            if digit == "1":
                output += FibonacciCoding.nth_fib_number(i)
            i += 1
        return output

    @staticmethod
    def encode(input_numbers: List[int], output_file: str) -> None:
        with open(output_file, "wb+") as f:
            with BitWriter(f) as writer:
                for number in input_numbers:
                    encoded = FibonacciCoding.encode_number(number)
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
                    n = 0
                    bit = reader.readbits(1)
                    double_one_flag = False
                    i = 2
                    while not double_one_flag or not bit == 1:
                        if bit == 1:
                            n += FibonacciCoding.nth_fib_number(i)
                            double_one_flag = True
                        else:
                            double_one_flag = False
                        i += 1
                        bit = reader.readbits(1)
                    if not reader.read:
                        break
                    output.append(n)

                return output

