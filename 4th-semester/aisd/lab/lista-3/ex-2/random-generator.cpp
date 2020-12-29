#include "random-generator.h"

std::vector<int> RandomGenerator(int size, bool unique)
{
  std::vector<int> output(size);

  srand(time(NULL));

  if (unique)
  {
    std::vector<int> possibleNumbers(size);
    for (int i = 1; i <= size; i++)
      possibleNumbers.at(i - 1) = i;

    int i = 0;
    while (possibleNumbers.size() > 0)
    {
      int t = rand() % possibleNumbers.size();
      output[i] = possibleNumbers.at(t);
      possibleNumbers.erase(possibleNumbers.begin() + t);
      i++;
    }
  }
  else
  {
    for (int i = 0; i < size; i++)
    {
      output[i] = rand() % size + 1;
    }
  }

  return output;
};
