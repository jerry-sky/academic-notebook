#include <vector>
#include "selection-algorithm.h"

class Select : SelectionAlgorithm
{
private:
  std::vector<int> insertionSort(std::vector<int>);
  int internalSelect(std::vector<int>, int k);
  int partition(std::vector<int>, int pivotElement);

public:
  using SelectionAlgorithm::SelectionAlgorithm;
  std::vector<int> Run(int k);
};
