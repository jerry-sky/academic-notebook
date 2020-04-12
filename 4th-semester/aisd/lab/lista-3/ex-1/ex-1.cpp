#include "ex-1.h"

void Exercise1(Algorithm algorithm, SwapNCompare *snc)
{

  Sort *sort;

  /**
   * Elements count - how many integers will the program accept via `stdin`.
   */
  int n = 0;

  std::cin >> n;
  // allocate a (pointer)array for the input integers.
  int *input = (int *)malloc(sizeof(int) * n);
  // collect provided integers
  for (int i = 0; i < n; i++)
  {
    std::cin >> input[i];
  }

  // choose the sorting algorithm based on what's been inputted
  switch (algorithm)
  {
  case Algorithm::Insertion:
    sort = (Sort *)new InsertionSort(input, n, snc);
    break;
  case Algorithm::Merge:
    sort = (Sort *)new MergeSort(input, n, snc);
    break;
  case Algorithm::DualPivotQuick:
    sort = (Sort *)new DualPivotQuickSort(input, n, snc);
    break;
  case Algorithm::Radix:
    sort = (Sort *)new RadixSort(input, n, snc);
    break;
  default:
  case Algorithm::Quick:
    sort = (Sort *)new QuickSort(input, n, snc);
    break;
  }

  /**
   * Sort the array.
   */
  int *output = sort->sort();
  std::cerr << "---" << std::endl;
  // check if sorted
  std::cerr << "is sorted? "
            << (sort->checkIfSorted() ? "yes" : "no")
            << std::endl;
  std::cout << "---" << std::endl;
  // print sorted array
  std::cout << "sorted array:" << std::endl;
  for (int i = 0; i < n; i++)
  {
    std::cout << output[i] << " ";
  }
  std::cerr << std::endl
            << "---" << std::endl;
  // print the statistics for how many swaps and comparisons there were
  std::cerr << "statistics:" << std::endl;
  std::cerr << "  comparisons: " << snc->getComparisonsCounter() << std::endl;
  std::cerr << "  swaps: " << snc->getSwapsCounter() << std::endl;
}
