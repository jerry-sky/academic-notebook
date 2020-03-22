#pragma once

#include "sort.h"

/**
 * Sorts an arbitrary array of integers using the MergeSort algorithm.
 */
class MergeSort : Sort
{
private:
  void merge(int left, int middle, int right);
  int *internalMergeSort(int left, int right);

public:
  using Sort::Sort;
  int *sort();
};
