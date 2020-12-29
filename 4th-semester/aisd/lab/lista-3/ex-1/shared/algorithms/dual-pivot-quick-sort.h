#pragma once

#include <iostream>
#include "sort.h"

/**
 * Sorts an arbitrary array of integers using the QuickSort algorithm.
 */
class DualPivotQuickSort : Sort
{
private:
  int partition(int left, int right, int pivotLeft, int pivotRight, int *newPivotLeft, int *newPivotRight);

  void rotate3(int *a, int *b, int *c);

  bool assert(int i, int k, int j);

  void internalQuickSort(int left, int right);

public:
  using Sort::Sort;
  int *sort();
};
