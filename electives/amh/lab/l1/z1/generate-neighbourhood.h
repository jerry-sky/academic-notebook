#include <vector>
#include <math.h>
#include <iostream>

/**
 * Generates a vector of all neighbouring points around the 4-dimensional point (0,0,0,0) so it can be later used to generate a neighbourhood of any arbitrary point in 4-dimensional space.
 */
class NeighbourhoodOffsetVectorsGenerator
{
private:
  /**
   * All collected offset vectors.
   */
  std::vector<std::vector<double>> all;
  /**
   * Counts how many vectors have been collected so far. Also indicates where to put the next found offset vector.
   */
  int allCounter = 0;
  /**
   * Radius of the neighbourhood.
   */
  double radius = 0.5;
  /**
   * Possible values to apply to all paramters of a vector.
   */
  std::vector<double> dict = {0, radius, -radius};
  /**
   * Internal recursive function generating the neighbourhood.
   */
  void recursive(std::vector<double>, int);

public:
  NeighbourhoodOffsetVectorsGenerator(double radius);
  /**
   * Returns the generated neighbourhood around the point (0,0,0,0).
   */
  std::vector<std::vector<double>> generate();
};
