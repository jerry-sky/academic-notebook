#include "norm.h"

double norm(std::vector<double> x)
{
  return sqrt(sumSquared(x));
}
