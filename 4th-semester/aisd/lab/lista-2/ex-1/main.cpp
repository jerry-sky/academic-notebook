#include <iostream>
#include "sort.h"

using namespace std;

/**
 * Sorts an arbitrary array of integers using the QuickSort algorithm.
 */
class QuickSort : Sort
{
private:
  int partition(int left, int right, int PivotIndex)
  {
    // take the pivot
    int pivot = input[PivotIndex];
    /**
     * Index of „smaller” than pivot element.
     */
    int i = left - 1;
    for (int j = left; j <= right - 1; j++)
    {
      // if (input[j] < pivot)
      if (snc->compare(input[j], pivot))
      {
        // increment the index of „smaller” element
        i++;
        snc->swap(&(input[i]), &(input[j]));
      }
    }
    snc->swap(&(input[i + 1]), &(input[right]));
    // return the current position of the pivot element
    return i + 1;
  }

  void internalQuickSort(int left, int right)
  {
    if (left < right)
    {
      int PivotIndex = right;
      int pivotNewIndex = partition(left, right, PivotIndex);

      internalQuickSort(left, pivotNewIndex - 1);
      internalQuickSort(pivotNewIndex + 1, right);
    }
  }

public:
  using Sort::Sort;
  int *sort()
  {
    internalQuickSort(0, inputSize - 1);
    return input;
  }
};

/**
 * Sorts an arbitrary array of integers using the InsertionSort algorithm.
 */
class InsertionSort : Sort
{
public:
  using Sort::Sort;
  int *sort()
  {
    for (int j = 1; j < inputSize; j++)
    {
      int key = input[j];
      int i = j - 1;
      // while (i > 0 && input[i] > key)
      while (i >= 0 && !snc->compare(input[i], key))
      {
        snc->registerSwap(input[i + 1], input[i]);
        input[i + 1] = input[i];
        i--;
      }
      snc->registerSwap(input[i + 1], key);
      input[i + 1] = key;
    }
    return input;
  }
};

/**
 * Sorts an arbitrary array of integers using the MergeSort algorithm.
 */
class MergeSort : Sort
{
private:
  void merge(int left, int middle, int right)
  {
    int leftSize = middle - left + 1;
    // int rightSize = right -(middle+1)+1;
    int rightSize = right - middle;
    int *merged = (int *)malloc(sizeof(int) * (leftSize + rightSize));

    int minSize = leftSize > rightSize ? rightSize : leftSize;

    int mergedIndex = 0;
    int leftIndex = 0;
    int rightIndex = 0;
    while (leftIndex < leftSize && rightIndex < rightSize)
    {
      if (snc->compare(input[left + leftIndex], input[(middle + 1) + rightIndex]))
      {
        merged[mergedIndex] = input[left + leftIndex];
        leftIndex++;
      }
      else
      {
        merged[mergedIndex] = input[(middle + 1) + rightIndex];
        rightIndex++;
      }
      mergedIndex++;
    }

    while (leftIndex < leftSize)
    {
      merged[mergedIndex] = input[left + leftIndex];
      leftIndex++;
      mergedIndex++;
    }
    while (rightIndex < rightSize)
    {
      merged[mergedIndex] = input[(middle + 1) + rightIndex];
      rightIndex++;
      mergedIndex++;
    }

    // commit changes
    for (int k = 0; k < leftSize + rightSize; k++)
    {
      snc->registerSwap(input[left + k], merged[k]);
      input[left + k] = merged[k];
    }
  }
  int *internalMergeSort(int left, int right)
  {
    if (left < right)
    {
      int middle = left + (right - left) / 2;
      internalMergeSort(left, middle);
      internalMergeSort(middle + 1, right);

      merge(left, middle, right);
    }
  }

public:
  using Sort::Sort;
  int *sort()
  {
    internalMergeSort(0, inputSize - 1);
    return input;
  }
};

int main(int argc, char const *argv[])
{

  SwapNCompare *snc;
  string algorithm;
  Sort *sort;

  for (int i = 0; i < argc; i++)
  {
    string a = argv[i];
    string av = argv[i];
    // take a value of the switch if possible
    if (i != argc - 1)
    {
      av = argv[i + 1];
    }

    if (a == "--comp")
    {
      snc = new SwapNCompare(av);
    }
    else if (a == "--type")
    {
      algorithm = av;
    }
  }

  int n = 0;

  cin >> n;
  int *input = (int *)malloc(sizeof(int) * n);

  for (int i = 0; i < n; i++)
  {
    cin >> input[i];
  }

  if (algorithm == "insert")
  {
    sort = (Sort *)new InsertionSort(input, n, snc);
  }
  else if (algorithm == "merge")
  {
    sort = (Sort *)new MergeSort(input, n, snc);
  }
  else
  {
    sort = (Sort *)new QuickSort(input, n, snc);
  }

  int *output = sort->sort();
  cerr << "---" << endl;
  cerr << "is sorted? "
       << (sort->checkIfSorted() ? "yes" : "no")
       << endl;
  cout << "---" << endl;
  cout << "sorted array:" << endl;
  for (int i = 0; i < n; i++)
  {
    cout << output[i] << " ";
  }
  cerr << endl
       << "---" << endl;
  cerr << "statistics:" << endl;
  cerr << "  comparisons: " << snc->getComparisonsCounter() << endl;
  cerr << "  swaps: " << snc->getSwapsCounter() << endl;

  return 0;
}
