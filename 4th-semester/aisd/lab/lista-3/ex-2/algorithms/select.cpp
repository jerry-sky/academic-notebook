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

int Select::internalSelect(std::vector<int> *scope, int k)
{
  if ((*scope).size() == 1)
  {
    return (*scope)[0];
  }

  // if ((*scope).size() < 6)
  // {
  //   std::vector<int> sorted = this->insertionSort((*scope));
  //   return sorted[k];
  // }

  // ceil(n/5)
  int groupsCount = (*scope).size() / 5;
  if ((*scope).size() % 5 != 0)
    groupsCount++;

  std::vector<int> medians(groupsCount);

  for (int i = 0; i < (*scope).size(); i += 5)
  {
    int right = i + 5 > (*scope).size() ? (*scope).size() : i + 5;
    std::vector<int> group((*scope).begin() + i, (*scope).begin() + right);
    // take the median of this sorted group
    std::vector<int> sorted = this->insertionSort(group);
    // copy sorted array back to the scope
    for (int j = 0; j < sorted.size(); j++)
    {
      (*scope)[i + j] = sorted[j];
    }
    int medianIndex = sorted.size() % 2 == 0 ? sorted.size() / 2 - 1 : sorted.size() / 2;
    medians[i / 5] = sorted[medianIndex];
  }

  // find median among the medians
  // we use integer division to make sure we're picking the lower median
  // in case there are even count of groups
  int medianIndex = groupsCount % 2 == 0 ? groupsCount / 2 - 1 : groupsCount / 2;
  // int medianIndex = (*scope).size() / 10;
  int median = this->internalSelect(&medians, medianIndex);

  // partition the array
  int medianNewIndex = this->partition(scope, median);

  if (medianNewIndex == k)
  {
    return median;
  }
  else if (k <= medianNewIndex)
  {
    // create an array containing the lower side
    std::vector<int> lowerSide((*scope).begin(), (*scope).begin() + medianNewIndex);
    // exit(0);
    return this->internalSelect(&lowerSide, k);
  }
  else // k > medianNewIndex
  {
    // create an array containing the higher side
    std::vector<int> higherSide((*scope).begin() + medianNewIndex + 1, (*scope).end());
    return this->internalSelect(&higherSide, k - medianNewIndex - 1);
  }
}

int Select::partition(std::vector<int> *toPartition, int pivotElement)
{
  int i = -1;
  for (int j = 0; j < (*toPartition).size() - 1; j++)
  {
    if (snc->compare((*toPartition)[j], pivotElement))
    {
      i++;
      snc->swap(&((*toPartition)[i]), &((*toPartition)[j]));
    }
  }
  snc->swap(&((*toPartition)[i + 1]), &((*toPartition)[(*toPartition).size() - 1]));
  return i;
}

int Select::Run(int k)
{
  return this->internalSelect(&(this->input), k);
}
