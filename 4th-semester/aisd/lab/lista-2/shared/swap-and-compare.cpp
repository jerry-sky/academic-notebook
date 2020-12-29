#include <iostream>
#include "swap-and-compare.h"

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
void SwapNCompare::reset()
{
  this->SwapsCounter = 0;
  this->ComparisonsCounter = 0;
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
 * Swap two elements and register this action.
 */
void SwapNCompare::swap(int *a, int *b)
{
  int tmp = *a;
  (*a) = (*b);
  (*b) = tmp;
  registerSwap((*a), (*b));
}
/**
 * Increase the SwapsCounter and print to `stderr`.
 */
void SwapNCompare::registerSwap(int a, int b)
{
  this->SwapsCounter++;
  std::cerr << "  swapped " << a << " with " << b << std::endl;
}
/**
   * Compare two elements and register this action if `propagate` is set to true.
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
/**
 * Increase the ComparisonsCounter and print to `stderr`.
 */
void SwapNCompare::registerComparison(int a, int b)
{
  std::cerr << "  compared " << a << " with " << b << std::endl;
  this->ComparisonsCounter++;
}
