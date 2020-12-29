#include "radix-sort.h"

int RadixSort::max()
{
  int max = this->input[0];
  for (int i = 1; i < this->inputSize; i++)
  {
    // this->snc->registerComparison(this->input[i], max);
    if (this->input[i] > max)
    {
      max = this->input[i];
    }
  }
  return max;
}

/**
 * Uses CountingSort as algorithm to partially sort the numbers by one of their
 * digit at the time.
 * As this algorithm isn't using comparison model the `SwapNCompare` object won't
 * register any comparisons and will register a linear number of swaps
 */
void RadixSort::countingSort(int expOffset)
{
  // temporary output array
  int *tmp = (int *)malloc(sizeof(int) * this->inputSize);
  // „how many times that number's digit has appeared” index array
  int count[radix] = {0};

  // map how many times that number's digit has appeared in the array
  for (int i = 0; i < this->inputSize; i++)
  {
    count[(this->input[i] / expOffset) % radix]++;
  }

  // convert this count array to be more index-y
  for (int i = 1; i < radix; i++)
  {
    count[i] += count[i - 1];
  }

  // generate the partially sorted array
  for (int i = this->inputSize - 1; i >= 0; i--)
  {
    tmp[count[(this->input[i] / expOffset) % radix] - 1] = this->input[i];
    count[(this->input[i] / expOffset) % radix]--;
  }

  // commit changes
  for (int i = 0; i < this->inputSize; i++)
  {
    this->snc->registerSwap(input[i], tmp[i]);
    this->input[i] = tmp[i];
  }
}

int *RadixSort::sort()
{
  int max = this->max();
  for (int e = 1; max / e > 0; e *= radix)
  {
    this->countingSort(e);
  }

  // apply the sorting direction if chosen the descending order
  if (this->snc->getSortDirection() == SortDirection::Descending)
  {
    for (int i = 0; i < this->inputSize / 2; i++)
    {
      this->snc->swap(&(this->input[i]), &(this->input[this->inputSize - 1 - i]));
    }
  }

  return input;
}
