#pragma once

#include "sort.h"

/**
 * Sorts an arbitrary array of integers using the RadixSort algorithm.
 */
class RadixSort : Sort
{
private:
  int radix = 10;
  /**
   * Elect the biggest number out of the input array.
   */
  int max();
  /**
   * Modified CountSort algorithm for partial sorting numbers by their digits.
   */
  void countingSort(int expOffset);

public:
  using Sort::Sort;
  int *sort();
};
