#include "quick-sort.h"

int QuickSort::partition(int left, int right, int PivotIndex)
{
  // take the pivot
  int pivot = input[PivotIndex];
  /**
     * Index of „smaller” than pivot element.
     */
  int i = left - 1;
  for (int j = left; j <= right - 1; j++)
  {
    // if (input[j] < pivot)
    if (snc->compare(input[j], pivot))
    {
      // increment the index of „smaller” element
      i++;
      snc->swap(&(input[i]), &(input[j]));
    }
  }
  snc->swap(&(input[i + 1]), &(input[right]));
  // return the current position of the pivot element
  return i + 1;
}

void QuickSort::internalQuickSort(int left, int right)
{
  if (left < right)
  {
    int PivotIndex = right;
    int pivotNewIndex = partition(left, right, PivotIndex);

    internalQuickSort(left, pivotNewIndex - 1);
    internalQuickSort(pivotNewIndex + 1, right);
  }
}

int *QuickSort::sort()
{
  internalQuickSort(0, inputSize - 1);
  return input;
}
