#include "swap-and-compare.h"
/**
 * A base class that defines basic administratory functionalities of provided sorting algorithms.
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
  virtual int *sort() = 0;
  bool checkIfSorted();
};
