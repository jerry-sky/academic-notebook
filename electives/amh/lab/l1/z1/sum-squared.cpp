#include "sum-squared.h"

double sumSquared(std::vector<double> x)
{
  double output = 0;

  for (int i = 0; i < 4; i++)
  {
    output += pow(x[i], 2);
  }
  return output;
}
