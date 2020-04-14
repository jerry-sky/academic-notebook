#pragma once

#include <string>
#include "sort-direction.h"
/**
 * Collects data about how many swaps and comparisons were made during the sorting process.
 * Also sets the sorting order.
 */
class SwapNCompare
{
private:
  /**
   * How many swaps have occurred.
   */
  int SwapsCounter = 0;
  /**
   * How many comparisons have occurred.
   */
  int ComparisonsCounter = 0;
  /**
   * In what direction should the array be sorted.
   */
  SortDirection direction;
  /**
   * Parse from string to SortDirection.
   */
  SortDirection parseSortDirection(std::string raw);

public:
  SwapNCompare(SortDirection direction);
  SwapNCompare(std::string direction);
  void reset();
  int getSwapsCounter();
  int getComparisonsCounter();
  /**
   * Returns the sorting direction that was chosen.
   * Useful when dealing with CountingSort as it isn't using the comparison model
   * and can't take advantage of the compare() method.
   */
  SortDirection getSortDirection();
  /**
   * Swap two elements and increase the swaps counter.
   */
  void swap(int *a, int *b);
  void registerSwap(int a, int b);
  /**
   * Compare two elements and increase the comparison counter.
   */
  bool compare(int a, int b, bool propagate = true);
  void registerComparison(int a, int b);
};
