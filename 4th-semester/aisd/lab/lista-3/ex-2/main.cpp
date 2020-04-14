#include <iostream>
#include <vector>
#include "random-generator.h"
#include "algorithms/select.h"

using namespace std;

int main(int argc, char const *argv[])
{

  vector<int> base = {5, 4, 3, 7, 1, 2, 6};

  Select *sel = new Select(base);

  cout << sel->Run(3) << endl;

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
