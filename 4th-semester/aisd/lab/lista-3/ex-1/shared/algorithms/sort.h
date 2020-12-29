#pragma once

#include "../swap-and-compare.h"

/**
 * A base class that defines basic administratory functionalities of a given sorting algorithm.
 */
class Sort
{
protected:
  /**
   * The array to sort.
   */
  int *input;
  /**
   * How many elements inside `input`.
   */
  int inputSize;
  /**
   * Counts how many times elements were swapped or compared. Also defines the sorting order.
   */
  SwapNCompare *snc;

public:
  Sort(int *input, int size, SwapNCompare *snc);
  /**
   * Sort the provided `input` array.
   */
  virtual int *sort() = 0;
  /**
   * Check if the array was appropriately sorted.
   */
  bool checkIfSorted();
};
