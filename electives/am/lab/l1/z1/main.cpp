#include <iostream>
#include <time.h>
#include "happy-cat.h"
#include "generate-neighbourhood.h"

using namespace std;

int main(int argc, char const *argv[])
{

  srand(time(NULL));

  NeighbourhoodOffsetVectorsGenerator *generator = new NeighbourhoodOffsetVectorsGenerator();

  vector<vector<double>> neighbourhood = generator->generate();

  /**
   * Starting point of the search for the minimum of selected function.
   */
  vector<double> current = {6, 6, 6, 6};
  /**
   * Computed value from the current vector.
   */
  double currentValue = HappyCat(current);

  double jumpSize = 0;
  for (int i = 0; i < 10000; i++)
  {
    bool foundBetter = false;
    // loop through the neighbouring points
    // starting from k=1 to skip zero-offset vector
    for (int k = 1; k < pow(3, 4); k++)
    {
      vector<double> candidate = {
          current[0] + neighbourhood[k][0] * jumpSize,
          current[1] + neighbourhood[k][1] * jumpSize,
          current[2] + neighbourhood[k][2] * jumpSize,
          current[3] + neighbourhood[k][3] * jumpSize};

      double candidateValue = HappyCat(candidate);
      if (candidateValue < currentValue)
      {
        // found a better solution
        current = candidate;
        currentValue = candidateValue;
        cout << "found " << candidateValue << endl;
        foundBetter = true;
        // don't jump
        jumpSize = 0;
      }
    }
    if (!foundBetter)
    {
      jumpSize = 2;
    }
  }

  cout << currentValue << endl;

  return 0;
}
