#include "griewank.h"

double Griewank(std::vector<double> x)
{
  double output = 0;

  for (int i = 0; i < 4; i++)
  {
    output += pow(x[i], 2) * 1.0;
  }

  output /= 4000;
  output += 1;

  double tmp = 1;
  for (int i = 0; i < 4; i++)
  {
    tmp *= cos(x[i] / sqrt(i + 1));
  }

  output -= tmp;

  return output;
}
