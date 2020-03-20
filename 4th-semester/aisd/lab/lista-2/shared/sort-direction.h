#pragma once

/**
 * Direction in which the output array is supposed to be sorted.
 */
enum SortDirection
{
  /**
   * Given two elements a > b the order would be (b a).
   *
   * Simply put: <=
   */
  Ascending,
  /**
   * Given two elements a > b the order would be (a b).
   *
   * Simply put: >=
   */
  Descending
};
