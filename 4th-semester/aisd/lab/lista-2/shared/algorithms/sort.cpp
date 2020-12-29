#include "sort.h"

/**
 * A base class that defines basic administratory functionalities of provided sorting algorithms.
 */
Sort::Sort(int *input, int size, SwapNCompare *snc)
{
  this->input = input;
  this->inputSize = size;

  this->snc = snc;
}
bool Sort::checkIfSorted()
{
  for (int i = 0; i < inputSize - 1; i++)
  {
    if (!snc->compare(input[i], input[i + 1], false))
      return false;
  }
  return true;
}
