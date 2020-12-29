#!/usr/bin/env python3
from sys import argv, exit
from zlib import crc32
from math import ceil
import re

FRAME_BORDER = '01111110'


def str_to_bytes(data: str) -> bytes:
    """Converts a string of 1s and 0s to a list of bytes.
    """

    data = data.ljust(ceil(len(data)/8) * 8, '0')
    output = []

    for i in range(0, int(len(data)/8)):
        b = 0
        for j in range(0, 8):
            if data[i*8+j] == '1':
                b += 2**(7-j)
        output.append(b)

    return bytes(output)


def bytes_to_str(data: bytes) -> str:
    """Converts a list bytes to a string of 1s and 0s.
    """
    output = ''

    for b in data:
        bb = bin(b)[2:].ljust(8, '0')
        output += bb

    return output

def crc_wrapper(data: str) -> str:
    """Performs crc32 method and returns the output in an appropriate
    format for this exercise.
    """

    crc = crc32(str_to_bytes(data))

    return bytes_to_str(crc.to_bytes(4, 'big'))

def encode(data: str) -> str:

    # attach the CRC checksum
    data += crc_wrapper(data)

    # perform bit stuffing
    data = re.sub(r'11111', '111110', data)

    return FRAME_BORDER + data + FRAME_BORDER

def decode(data: str) -> str:

    # remove frame borders
    data = re.sub(FRAME_BORDER, '', data)

    # perform reverse bit stuffing
    data = re.sub(r'111110', '11111', data)

    # verify the CRC
    crc = data[-32:]

    if crc != crc_wrapper(data[:-32]):
        raise Exception('invalid CRC => invalid frame')

    return data[:-32]

if __name__ == '__main__':

    if len(argv) < 4:
        exit('usage: ./ex-1.py <--encode|--decode> input_file output_file')

    mode = argv[1]
    if mode not in ['--encode', '--decode']:
        exit('invalid parameters')
    input_file = argv[2]
    output_file = argv[3]

    with open(input_file, 'r') as fin:
        data = fin.readline().replace('\n', '')
        parsed = encode(data) if mode == '--encode' else decode(data)
        with open(output_file, 'w+') as fout:
            fout.write(parsed)
            fout.write('\n')
