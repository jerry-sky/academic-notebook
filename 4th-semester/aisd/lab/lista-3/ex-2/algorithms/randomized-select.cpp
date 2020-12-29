#include "randomized-select.h"

int RandomizedSelect::partition(int left, int right)
{
  int pivotElement = this->input[right];
  int i = left - 1;
  for (int j = left; j <= right - 1; j++)
  {
    if (snc->compare(input[j], pivotElement))
    {
      // increment the index of „smaller” element
      i++;
      snc->swap(&(input[i]), &(input[j]));
    }
  }
  snc->swap(&(input[i + 1]), &(input[right]));
  // return the current position of the pivot element
  return i + 1;
};

int RandomizedSelect::randomizedPartition(int left, int right)
{
  srand(time(NULL));

  int r = rand() % (right - left) + left;

  this->snc->swap(&(this->input[right]), &(this->input[r]));

  return this->partition(left, right);
};

int RandomizedSelect::internalRandomizedSelect(int left, int right, int i)
{
  if (left == right)
  {
    return this->input[left];
  }

  int pivotIndex = this->randomizedPartition(left, right);
  int k = pivotIndex - left;

  if (i == k)
  {
    return this->input[pivotIndex];
  }
  else if (i < k)
  {
    return this->internalRandomizedSelect(left, pivotIndex - 1, i);
  }
  else // i > k
  {
    return this->internalRandomizedSelect(pivotIndex + 1, right, i - k - 1);
  }
};

int RandomizedSelect::Run(int k)
{
  return this->internalRandomizedSelect(0, this->input.size() - 1, k);
};
