#include "selection-algorithm.h"

SelectionAlgorithm::SelectionAlgorithm(std::vector<int> input, SwapNCompare* snc)
{
  this->input = input;
  this->snc = snc;
};

std::vector<int> SelectionAlgorithm::getList()
{
  return this->input;
}
