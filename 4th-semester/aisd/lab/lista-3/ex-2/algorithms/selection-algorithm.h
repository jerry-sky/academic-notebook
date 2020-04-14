#pragma once
#include <vector>
#include "swap-and-compare.h"

class SelectionAlgorithm
{
protected:
  std::vector<int> input;
  SwapNCompare* snc;
public:
  SelectionAlgorithm(std::vector<int>);
  int virtual Run(int) = 0;
};
