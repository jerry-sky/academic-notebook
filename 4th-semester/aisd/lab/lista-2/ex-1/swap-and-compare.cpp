#include <iostream>
#include "swap-and-compare.h"

/**
 * Collects data about how many swaps and comparisons were made during the sorting process.
 * Also sets the sorting order.
 */
SortDirection SwapNCompare::parseSortDirection(std::string raw)
{
  if (raw == ">=")
    return Descending;
  else
    return Ascending;
};

SwapNCompare::SwapNCompare(SortDirection direction)
{
  this->direction = direction;
}
SwapNCompare::SwapNCompare(std::string direction)
{
  // has same functionality as regular constructor, but it just parses the sort direction from string
  this->direction = parseSortDirection(direction);
}
int SwapNCompare::getSwapsCounter()
{
  return this->SwapsCounter;
}
int SwapNCompare::getComparisonsCounter()
{
  return this->ComparisonsCounter;
}
/**
   * Swap two elements and increase the swaps counter.
   */
void SwapNCompare::swap(int *a, int *b)
{
  int tmp = *a;
  (*a) = (*b);
  (*b) = tmp;
  registerSwap((*a), (*b));
}
void SwapNCompare::registerSwap(int a, int b)
{
  this->SwapsCounter++;
  std::cerr << "  swapped " << a << " with " << b << std::endl;
}
/**
   * Compare two elements and increase the comparison counter.
   */
bool SwapNCompare::compare(int a, int b, bool propagate)
{
  if (propagate)
    registerComparison(a, b);
  switch (this->direction)
  {
  case Ascending:
    return a <= b;
  case Descending:
    return a >= b;
  }
}
void SwapNCompare::registerComparison(int a, int b)
{
  std::cerr << "  compared " << a << " with " << b << std::endl;
  this->ComparisonsCounter++;
}
