#include <iostream>
#include <vector>
#include <time.h>
#include "selection-algorithm.h"

class RandomizedSelect : SelectionAlgorithm
{
private:
  int internalRandomizedSelect(int left, int right, int i);
  int randomizedPartition(int left, int right);
  int partition(int left, int right);

public:
  using SelectionAlgorithm::SelectionAlgorithm;
  using SelectionAlgorithm::getList;
  int Run(int);
};
