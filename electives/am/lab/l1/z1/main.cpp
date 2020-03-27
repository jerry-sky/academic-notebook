#include <iostream>
#include <time.h>
#include "happy-cat.h"
#include "griewank.h"
#include "generate-neighbourhood.h"

using namespace std;

double chooseFunction(int b, vector<double> x)
{
  if (b == 0)
  {
    return HappyCat(x);
  }
  else
  {
    return Griewank(x);
  }
}

vector<double> getRandomPoint(int radius = 10)
{
  vector<double> output = {0, 0, 0, 0};
  for (int i = 0; i < 4; i++)
  {
    output[i] = (rand() % (2 * radius)) - radius;
  }
  return output;
}

int main(int argc, char const *argv[])
{
  double t = 1;
  int b = 0;
  for (int i = 1; i < argc; i++)
  {
    if (i == 1)
      t = atof(argv[i]);
    else if (i == 2)
      b = stoi(argv[i]);
  }

  srand(time(NULL));

  NeighbourhoodOffsetVectorsGenerator *generator = new NeighbourhoodOffsetVectorsGenerator(b == 0 ? 0.5 : 0.1);

  vector<vector<double>> neighbourhood = generator->generate();

  /**
   * Starting point of the search for the minimum of selected function.
   */
  vector<double> current = getRandomPoint(5);
  /**
   * Computed value from the current vector.
   */
  double currentValue = chooseFunction(b, current);

  double jumpSize = b == 0 ? 2 : 5.7;
  int failedAttempts = 0;
  clock_t begin = clock();
  clock_t now = clock();
  while ((now - begin) * 1.0 / CLOCKS_PER_SEC <= t)
  {
    bool foundBetter = false;
    // loop through the neighbouring points
    for (int k = 0; k < pow(3, 4); k++)
    {
      vector<double> candidate = {0, 0, 0, 0};
      if (failedAttempts > 300)
      {
        candidate = getRandomPoint();
      }
      else
      {
        for (int i = 0; i < 4; i++)
        {
          candidate[i] = current[i] + neighbourhood[k][i] + (failedAttempts > 100 ? jumpSize : 0);
        }
      }

      double candidateValue = chooseFunction(b, candidate);
      if (candidateValue < currentValue)
      {
        // found a better solution
        current = candidate;
        currentValue = candidateValue;
        // cout << "found " << candidateValue << endl;
        foundBetter = true;
        // don't jump
        jumpSize = 0;
        failedAttempts = 0;
      }
      else if (currentValue < 0.03)
      {
        // cout << candidate[0] << " " << candidate[1] << " " << candidate[2] << " " << candidate[3] << endl;
      }
    }
    if (!foundBetter)
    {
      failedAttempts++;
    }
    now = clock();
  }

  cout << current[0] << " " << current[1] << " " << current[2] << " " << current[3] << " " << currentValue << endl;

  return 0;
}
