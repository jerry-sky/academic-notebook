#!/usr/bin/python3
import statistics


comparisons_select = [
    693,
    636,
    741,
    772,
    809,
    659,
    840,
    825,
    748,
    795
]

print("comparisons SELECT max =", max(comparisons_select))
print("comparisons SELECT min =", min(comparisons_select))
print("comparisons SELECT avg =", sum(
    comparisons_select)/len(comparisons_select))
print("comparisons SELECT standard deviation =",
      statistics.stdev(comparisons_select))

comparisons_randomized_select = [
    548,
    189,
    219,
    353,
    549,
    391,
    244,
    401,
    300,
    606
]

print("comparisons RANDOMIZED SELECT max =",
      max(comparisons_randomized_select))
print("comparisons RANDOMIZED SELECT min =",
      min(comparisons_randomized_select))
print("comparisons RANDOMIZED SELECT avg =", sum(
    comparisons_randomized_select)/len(comparisons_randomized_select))
print("comparisons RANDOMIZED SELECT standard deviation =",
      statistics.stdev(comparisons_randomized_select))
