#include "dual-pivot-quick-sort.h"

void DualPivotQuickSort::rotate3(int *a, int *b, int *c)
{
  snc->registerSwap(*a, *c);
  snc->registerSwap(*b, *a);
  snc->registerSwap(*c, *b);

  int tmp = *a;
  (*a) = (*b);
  (*b) = (*c);
  (*c) = tmp;
};

bool DualPivotQuickSort::assert(int i, int k, int j)
{
  return true;
  // return i >= 0 && k >= 0 && j >= 0 && i < inputSize && k < inputSize && j < inputSize;
};

int DualPivotQuickSort::partition(int left, int right, int pivotLeft, int pivotRight, int *newPivotLeft, int *newPivotRight)
{
  int i = left + 1;
  int k = right - 1;
  int j = i;
  int d = 0;

  while (j <= k && assert(i, k, j))
  {
    if (d > 0)
    {
      // if (input[j] < pivotLeft)
      if (snc->compare(input[j], pivotLeft))
      {
        snc->swap(&(input[i]), &(input[j]));
        i++;
        j++;
        d++;
      }
      else
      {
        if (snc->compare(input[j], pivotRight))
        {
          j++;
        }
        else
        {
          snc->swap(&(input[j]), &(input[k]));
          k--;
          d--;
        }
      }
    }
    else
    {
      while (assert(i, k, j) && !snc->compare(input[k], pivotRight))
      {
        k--;
        d--;
      }
      if (j <= k && assert(i, k, j))
      {
        if (snc->compare(input[k], pivotLeft))
        {
          rotate3(&(input[k]), &(input[j]), &(input[i]));
          i++;
          d++;
        }
        else
        {
          snc->swap(&(input[j]), &(input[k]));
        }
        j++;
      }
    }
  }
  snc->swap(&(input[left]), &(input[i - 1]));
  snc->swap(&(input[right]), &(input[k + 1]));
  (*newPivotLeft) = i - 1;
  (*newPivotRight) = k + 1;
}

void DualPivotQuickSort::internalQuickSort(int left, int right)
{
  if (left < right)
  {
    if (snc->compare(input[right], input[left]))
    {
      snc->swap(&(input[left]), &(input[right]));
    }
    int leftPivot = input[left];
    int rightPivot = input[right];
    int newLeftPivot;
    int newRightPivot;
    partition(left, right, leftPivot, rightPivot, &newLeftPivot, &newRightPivot);
    internalQuickSort(left, newLeftPivot - 1);
    internalQuickSort(newLeftPivot + 1, newRightPivot - 1);
    internalQuickSort(newRightPivot + 1, right);
  }
}

int *DualPivotQuickSort::sort()
{
  internalQuickSort(0, inputSize - 1);
  return input;
};
