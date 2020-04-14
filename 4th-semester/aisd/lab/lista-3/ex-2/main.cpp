#include <iostream>
#include <vector>
#include "random-generator.h"
#include "algorithms/select.h"

using namespace std;

int main(int argc, char const *argv[])
{
  vector<int> base = {5, 4, 3, 7, 1, 6, 8, 2, 9, 10, 4, 3, 6};
  // vector<int> base = {1, 2, 3, 4, 5, 6, 7};

  Select *sel = new Select(base);

  cout << sel->Run(7) << endl;

  return 0;

  // parse the arguments
  bool unique = false;

  if (argc > 1)
  {
    string arg = argv[1];
    if (arg == "-p")
    {
      unique = true;
    }
  }

  // collect necessary data
  int n = 0;
  int k = 0;
  cin >> n;
  cin >> k;

  vector<int> array = RandomGenerator(n, unique);

  return 0;
}
