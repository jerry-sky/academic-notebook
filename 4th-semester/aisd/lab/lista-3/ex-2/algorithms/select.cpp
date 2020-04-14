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

  // report current state of the inputted array
  std::cerr << "{ ";
  for (auto t : this->input)
  {
    std::cerr << t << " ";
  }
  std::cerr << "}" << std::endl;

  std::cerr << "  k = " << k << std::endl;

  // ceil(n/5)
  int groupsCount = (*scope).size() / 5;
  if ((*scope).size() % 5 != 0)
    groupsCount++; // this is the `ceil` part

  // find the medians of those little groups
  std::vector<int> medians(groupsCount);

  for (int i = 0; i < (*scope).size(); i += 5)
  {
    // to avoid overflowing out of the scope the last group has to end before
    // the end of the scope
    int right = i + 5 > (*scope).size() ? (*scope).size() : i + 5;
    // create the group of up to 5 elements
    std::vector<int> group((*scope).begin() + i, (*scope).begin() + right);
    // take the median of this sorted group
    std::vector<int> sorted = this->insertionSort(group);
    // copy sorted array back to the scope
    for (int j = 0; j < sorted.size(); j++)
    {
      (*scope)[i + j] = sorted[j];
    }
    // with those groups that have less than 5 elements we need to make sure
    // we're taking the lower median if there are even number of elements
    // in this group
    int medianIndex = sorted.size() % 2 == 0 ? sorted.size() / 2 - 1 : sorted.size() / 2;
    medians[i / 5] = sorted[medianIndex];
  }

  // find median among the medians
  // we use integer division to make sure we're picking the lower median
  // in case there are even count of groups
  int medianIndex = groupsCount % 2 == 0 ? groupsCount / 2 - 1 : groupsCount / 2;
  // int medianIndex = (*scope).size() / 10;
  int median = this->internalSelect(&medians, medianIndex);

  std::cerr << "  taken median " << median << " as the pivot for partitioning" << std::endl;

  // partition the array
  int medianNewIndex = this->partition(scope, median);

  int result;
  if (medianNewIndex == k)
  {
    // pivot's got what we're looking for
    result = median;
  }
  else if (k <= medianNewIndex)
  {
    // create an array containing the lower side
    std::vector<int> lowerSide((*scope).begin(), (*scope).begin() + medianNewIndex);

    result = this->internalSelect(&lowerSide, k);
    // copy modified lower side back onto the scope
    for (int i = 0; i < lowerSide.size(); i++)
    {
      (*scope)[i] = lowerSide[i];
    }
  }
  else // k > medianNewIndex
  {
    // create an array containing the higher side
    std::vector<int> higherSide((*scope).begin() + medianNewIndex + 1, (*scope).end());

    result = this->internalSelect(&higherSide, k - medianNewIndex - 1);
    // copy modifed higher side back onto the scope
    for (int i = 0; i < higherSide.size(); i++)
    {
      (*scope)[i + medianNewIndex + 1] = higherSide[i];
    }
  }
  return result;
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
