#include "sort.h"

/**
 * Sorts an arbitrary array of integers using the QuickSort algorithm.
 */
class QuickSort : Sort
{
private:
  int partition(int left, int right, int PivotIndex);

  void internalQuickSort(int left, int right);

public:
  using Sort::Sort;
  int *sort();
};
