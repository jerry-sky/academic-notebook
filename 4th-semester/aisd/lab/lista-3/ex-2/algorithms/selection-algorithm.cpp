#include "selection-algorithm.h"

SelectionAlgorithm::SelectionAlgorithm(std::vector<int> input)
{
  this->input = input;
  this->snc = new SwapNCompare(Ascending);
};
