#include <iostream>
#include <vector>
#include "random-generator.h"

using namespace std;

int main(int argc, char const *argv[])
{

  vector<int> base = {2, 3, 4, 5, 7, 8, 9, 10};

  vector<int> part(base.begin() + 2, base.begin() + 5);

  for (auto x : part)
  {
    cout << x << endl;
  }

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
