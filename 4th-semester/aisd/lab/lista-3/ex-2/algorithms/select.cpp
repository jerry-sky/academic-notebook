#include "select.h"

std::vector<int> Select::insertionSort(std::vector<int> group)
{
  if (group.size() == 1)
    return group;

  for (int j = 1; j < group.size(); j++)
  {
    int key = group[j];
    int i = j - 1;
    while (i >= 0 && !snc->compare(group[i], key))
    {
      snc->registerSwap(group[i + 1], group[i]);
      group[i + 1] = group[i];
      i--;
    }
    snc->registerSwap(group[i + 1], key);
    group[i + 1] = key;
  }
  return group;
}

int Select::internalSelect(std::vector<int> scope, int k)
{
  if (scope.size() == 1)
    return scope[0];

  // ceil(n/5)
  int groupsCount = scope.size() / 5;
  if (scope.size() % 5 != 0)
    groupsCount++;

  std::vector<int> medians(groupsCount);

  for (int i = 0; i < scope.size(); i += 5)
  {
    int right = i + 5 > scope.size() - 1 ? scope.size() - 1 : i + 5;
    std::vector<int> group(scope.begin() + i, scope.begin() + right);
    // take the median of this sorted group
    medians[i / 5] = this->insertionSort(group)[2];
  }
  // find median among the medians
  // we use integer division to make sure we're picking the lower median
  // in case there are even count of groups
  int median = this->internalSelect(medians, groupsCount / 2);
}

int Select::partition(std::vector<int> toPartition, int pivotElement)
{
  int i = -1;
  for (int j = 0; j < toPartition.size() - 1; j++)
  {
    if (snc->compare(toPartition[j], pivotElement))
    {
      i++;
      snc->swap(&(toPartition[i]), &(toPartition[j]));
    }
  }
  snc->swap(&(toPartition[i + 1]), &(toPartition[toPartition.size() - 1]));
  return i + 1;
}
