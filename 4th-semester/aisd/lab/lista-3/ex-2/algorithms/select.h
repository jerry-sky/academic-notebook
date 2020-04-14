#include <vector>
#include "selection-algorithm.h"

class Select : SelectionAlgorithm
{
private:
  std::vector<int> insertionSort(std::vector<int>);
  int internalSelect(std::vector<int>*, int k);
  std::vector<int> partition(std::vector<int>, int pivotElement, int* newPivotIndex);

public:
  using SelectionAlgorithm::SelectionAlgorithm;
  int Run(int);
};
