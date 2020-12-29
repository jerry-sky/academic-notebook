#include "sum.h"

double sum(std::vector<double> x)
{
  double output = 0;
  for(int i = 0; i < 4; i++) {
    output += x[i];
  }
  return output;
}
