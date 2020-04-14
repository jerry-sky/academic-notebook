#include <iostream>
#include <vector>
#include "random-generator.h"
#include "algorithms/select.h"
#include "algorithms/randomized-select.h"
#include "algorithms/swap-and-compare.h"

using namespace std;

int main(int argc, char const *argv[])
{

  // parse the arguments
  bool unique = false;
  string algorithm = "--select";

  // type of data
  if (argc > 1)
  {
    string arg = argv[1];
    if (arg == "-p")
    {
      unique = true;
    }
  }
  // which algorithm to run
  if (argc > 2)
  {
    algorithm = argv[2];
  }

  // collect necessary data
  int n, k;
  cin >> n;
  cin >> k;

  // difference in indexing systems
  // (humans count elements starting from 1 and computers starting from 0)
  k--;

  vector<int> array = RandomGenerator(n, unique);

  SwapNCompare *snc = new SwapNCompare(SortDirection::Ascending);

  SelectionAlgorithm *sel;

  if (algorithm == "--randomized-select")
  {
    sel = (SelectionAlgorithm *)new RandomizedSelect(array, snc);
  }
  else
  {
    sel = (SelectionAlgorithm *)new Select(array, snc);
  }

  int result = sel->Run(k);

  cerr << "---" << endl
       << "summary:" << endl
       << "  comparisons total : " << snc->getComparisonsCounter()
       << endl
       << "  swaps total       : " << snc->getSwapsCounter()
       << endl
       << endl;

  bool alreadyFlagged = false;
  for (auto t : sel->getList())
  {
    if (t == result && !alreadyFlagged)
    {
      cout << "[" << t << "]"
           << " ";
      alreadyFlagged = true;
    }
    else
    {
      cout << t << " ";
    }
  }
  cout << endl;

  return 0;
}
