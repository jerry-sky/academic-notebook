#include "happy-cat.h"

double HappyCat(std::vector<double> x)
{

  double output = 0;

  output = sumSquared(x) - 4;
  output = sqrt(sqrt(abs(output)));

  double tmp = sumSquared(x) / 2 + sum(x);
  tmp /= 4.0;

  output += tmp + 1.0 / 2.0;

  return output;
}
