#include "insertion-sort.h"

int *InsertionSort::sort()
{
  for (int j = 1; j < inputSize; j++)
  {
    int key = input[j];
    int i = j - 1;
    // while (i > 0 && input[i] > key)
    while (i >= 0 && !snc->compare(input[i], key))
    {
      snc->registerSwap(input[i + 1], input[i]);
      input[i + 1] = input[i];
      i--;
    }
    snc->registerSwap(input[i + 1], key);
    input[i + 1] = key;
  }
  return input;
}
