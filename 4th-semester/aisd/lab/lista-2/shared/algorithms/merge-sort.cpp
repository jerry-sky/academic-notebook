#include "merge-sort.h"

void MergeSort::merge(int left, int middle, int right)
{
  int leftSize = middle - left + 1;
  // int rightSize = right -(middle+1)+1;
  int rightSize = right - middle;
  int *merged = (int *)malloc(sizeof(int) * (leftSize + rightSize));

  int minSize = leftSize > rightSize ? rightSize : leftSize;

  int mergedIndex = 0;
  int leftIndex = 0;
  int rightIndex = 0;
  while (leftIndex < leftSize && rightIndex < rightSize)
  {
    if (snc->compare(input[left + leftIndex], input[(middle + 1) + rightIndex]))
    {
      merged[mergedIndex] = input[left + leftIndex];
      leftIndex++;
    }
    else
    {
      merged[mergedIndex] = input[(middle + 1) + rightIndex];
      rightIndex++;
    }
    mergedIndex++;
  }

  while (leftIndex < leftSize)
  {
    merged[mergedIndex] = input[left + leftIndex];
    leftIndex++;
    mergedIndex++;
  }
  while (rightIndex < rightSize)
  {
    merged[mergedIndex] = input[(middle + 1) + rightIndex];
    rightIndex++;
    mergedIndex++;
  }

  // commit changes
  for (int k = 0; k < leftSize + rightSize; k++)
  {
    snc->registerSwap(input[left + k], merged[k]);
    input[left + k] = merged[k];
  }
}
int *MergeSort::internalMergeSort(int left, int right)
{
  if (left < right)
  {
    int middle = left + (right - left) / 2;
    internalMergeSort(left, middle);
    internalMergeSort(middle + 1, right);

    merge(left, middle, right);
  }
}
int *MergeSort::sort()
{
  internalMergeSort(0, inputSize - 1);
  return input;
}
