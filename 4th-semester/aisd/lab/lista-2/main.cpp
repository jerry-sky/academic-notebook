#include <iostream>
#include "shared/algorithms.h"
#include "ex-1.h"
#include "ex-2.h"

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
  Algorithm sort;

  /**
   * Basically tells what exercise to run.
   */
  string mode = "ex-1";

  int k = 0;

  string stat_file = "";

  // parse parameters
  for (int i = 0; i < argc; i++)
  {
    string a = argv[i];
    string av = argv[i];
    string avv = argv[i];
    // take a value of the switch if possible
    if (i != argc - 1)
    {
      av = argv[i + 1];
    }
    if (i != argc - 2)
    {
      avv = argv[i + 2];
    }

    if (a == "--comp")
    {
      snc = new SwapNCompare(av);
    }
    else if (a == "--type")
    {
      algorithm = av;
    }
    else if (a == "--stat")
    {
      mode = "ex-2";
      stat_file = av;
      k = stoi(avv);
    }
  }

  // choose the sorting algorithm based on what's been inputted
  if (algorithm == "insert")
  {
    sort = Insertion;
  }
  else if (algorithm == "merge")
  {
    sort = Merge;
  }
  else
  {
    sort = Quick;
  }

  if (mode == "ex-2")
  {
    Exercise2(sort, snc, stat_file, k);
  }
  else
  {
    Exercise1(sort, snc);
  }

  return 0;
}
