#include <iostream>
#include "shared/algorithms/quick-sort.h"
#include "shared/algorithms/insertion-sort.h"
#include "shared/algorithms/merge-sort.h"

using namespace std;

/**
 * A program that sorts given array using selected sorting algorithm. See the `readme` file for more information.
 */
int main(int argc, char const *argv[])
{

  /**
   * The swaps and comparisons counter. Sets the sort order.
   * See SwapNCompare for more details.
   */
  SwapNCompare *snc;
  /**
   * Selected algorithm parsed from `--type` parameter.
   */
  string algorithm;
  /**
   * Actual sorting algorithm class.
   */
  Sort *sort;

  // parse parameters
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

  /**
   * Elements count - how many integers will the program accept via `stdin`.
   */
  int n = 0;

  cin >> n;
  // allocate a (pointer)array for the input integers.
  int *input = (int *)malloc(sizeof(int) * n);
  // collect provided integers
  for (int i = 0; i < n; i++)
  {
    cin >> input[i];
  }

  // choose the sorting algorithm based on what's been inputted
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

  /**
   * Sort the array.
   */
  int *output = sort->sort();
  cerr << "---" << endl;
  // check if sorted
  cerr << "is sorted? "
       << (sort->checkIfSorted() ? "yes" : "no")
       << endl;
  cout << "---" << endl;
  // print sorted array
  cout << "sorted array:" << endl;
  for (int i = 0; i < n; i++)
  {
    cout << output[i] << " ";
  }
  cerr << endl
       << "---" << endl;
  // print the statistics for how many swaps and comparisons there were
  cerr << "statistics:" << endl;
  cerr << "  comparisons: " << snc->getComparisonsCounter() << endl;
  cerr << "  swaps: " << snc->getSwapsCounter() << endl;

  return 0;
}
