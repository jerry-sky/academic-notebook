#pragma once

#include "sort.h"

/**
 * Sorts an arbitrary array of integers using the InsertionSort algorithm.
 */
class InsertionSort : Sort
{
public:
  using Sort::Sort;
  int *sort();
};
