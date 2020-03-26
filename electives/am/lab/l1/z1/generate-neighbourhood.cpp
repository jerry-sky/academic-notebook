#include "generate-neighbourhood.h"

void NeighbourhoodOffsetVectorsGenerator::recursive(std::vector<double> x, int index)
{
  for (int i = 0; i < 3; i++)
  {
    x[index] = dict[i];

    if (index == 3)
    {
      all[allCounter] = x;
      allCounter++;
    }
    else
    {
      recursive(x, index + 1);
    }
  }
}

NeighbourhoodOffsetVectorsGenerator::NeighbourhoodOffsetVectorsGenerator()
{
  std::vector<std::vector<double>> output(pow(3, 4));
  for (int i = 0; i < pow(3, 4); i++)
    output[i].resize(4);

  all = output;
}

std::vector<std::vector<double>> NeighbourhoodOffsetVectorsGenerator::generate()
{
  std::vector<double> tmp = {0, 0, 0, 0};
  recursive(tmp, 0);
  return all;
}
