#!/usr/bin/env python3

import matplotlib.pyplot as plt
from sys import stdin, argv

title = 'Graph'

if len(argv) > 1:
    title = argv[1]

# read bits
bits = []
for line in stdin:
    bit = int(line)
    bits.append(bit)

# assert bits count to be 8*const
assert len(bits)/8 == int(len(bits)/8)

# group bits into bytes
bytes_ = []
bytes_count = int(len(bits)/8)
for i in range(0, bytes_count):
    x = [bits[i*8 + j] * (2**(7-j)) for j in range(0, 8)]
    bytes_.append(
        sum(x)
    )

# setup graph
x = range(0, bytes_count)
y = bytes_

plt.plot(x, y)

plt.xlabel('bytes')
plt.ylabel('bytes’ values')

plt.title(title)

plt.show()
