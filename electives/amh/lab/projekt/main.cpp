#include <iostream>
#include <vector>
#include <algorithm>
#include <time.h>
#include <chrono>
#include <ratio>

using namespace std;
using namespace std::chrono;

/**
 * Returns a random integer from range [a,b].
 */
int randint(int a, int b)
{
  return (rand() % (b - a + 1)) + a;
}

/**
 * Checks if two provided directions are the opposites of each other.
 */
bool isInverse(char a, char b)
{
  if ((a == 'L' && b == 'R') || (a == 'R' && b == 'L'))
  {
    return true;
  }
  if ((a == 'U' && b == 'D') || (a == 'D' && b == 'U'))
  {
    return true;
  }
  return false;
}

/**
 * Removes unnecessary mini loops like LR or UD from the solution.
 */
string removeMiniLoops(string solution)
{

  int length = solution.length();
  int i = 0;
  while (i < length - 1)
  {
    char curr = solution[i];
    char next = solution[i + 1];
    if (isInverse(curr, next))
    {
      solution.erase(i, 1);
      solution.erase(i, 1);
      i -= 2;
      if (i < 0)
      {
        i--;
      }
      length -= 2;
    }
    i++;
  }

  return solution;
}

/**
 * Moves provided vector in the provided direction.
 */
vector<int> translatePosition(vector<int> position, char direction)
{

  if (direction == 'U')
  {
    position[0]--;
  }
  else if (direction == 'D')
  {
    position[0]++;
  }
  else if (direction == 'L')
  {
    position[1]--;
  }
  else
  {
    position[1]++;
  }

  return position;
}

/**
 * Validates solution and gives a shorter version of it if possible.
 *
 * It returns `NULL` if the solution is not valid.
 */
string validateSolution(string solution, vector<int> startingPosition, vector<vector<int>> simulationMap)
{

  vector<int> pos = startingPosition;
  string modifiedSolution = "";
  for (char &move : solution)
  {
    int currentCell = simulationMap[pos[0]][pos[1]];
    // check if the agent hit a wall
    if (currentCell == 1)
    {
      return "";
    }
    // check if the agent is already at the exit
    else if (currentCell == 8)
    {
      return modifiedSolution;
    }
    translatePosition(pos, move);
    modifiedSolution += move;
  }

  if (simulationMap[pos[0]][pos[1]] == 8)
  {
    return modifiedSolution;
  }

  return "";
}

bool compareLen(const string &a, const string &b)
{
  return (a.size() < b.size());
}

vector<string> fitnessFunc(vector<string> population, vector<int> startingPosition, vector<vector<int>> simulationMap)
{
  vector<string> fittedPopulation = vector<string>();
  for (auto sol : population)
  {
    if (sol != "")
    {
      fittedPopulation.push_back(
          validateSolution(sol, startingPosition, simulationMap));
    }
    else
    {
      fittedPopulation.push_back("");
    }
  }
  // sort the population by their fitness
  sort(fittedPopulation.begin(), fittedPopulation.end(), compareLen);

  return fittedPopulation;
}

string GAFindShortestPath(vector<vector<int>> simulationMap, vector<string> initialSolutions, int maxPopSize, float mutationProbability, int maxRunningTime)
{

  auto begin = high_resolution_clock::now();

  vector<int> startingPosition = vector<int>(2);
  int i = 0;
  for (auto line : simulationMap)
  {
    int j = 0;
    for (auto cell : line)
    {
      if (cell == 5)
      {
        startingPosition = {i, j};
      }
      j++;
    }
    i++;
  }

  vector<string> population = initialSolutions;

  auto end = high_resolution_clock::now();
  auto runningTime = duration_cast<seconds>(end - begin).count();
  while (runningTime <= maxRunningTime)
  {

    // selection stage
    int pivot = maxPopSize / 2;
    // select the best solutions based on their length (the lowest the best)
    vector<string> foundingFathers = vector<string>(population.begin(), population.begin() + pivot);
    vector<string> theRest = vector<string>(population.begin() + pivot + 1, population.end());
    // take a valid solution that wasn't that good but it will
    // introduce more diversity
    if (population.size() == maxPopSize)
    {
      string r = "";
      while (r == "" && theRest.size() > 0)
      {
        int index = randint(0, theRest.size() - 1);
        r = theRest[index];
        theRest.erase(theRest.begin() + index);
      }
      if (r != "")
      {
        foundingFathers.push_back(r);
      }
    }

    // crossover stage
    population = foundingFathers;
    // generate remaining population members based on the „founding fathers”
    while (population.size() < maxPopSize)
    {
      // // pick two parents to crossover
      // int one_index = randint(0, foundingFathers.size() - 1);
      // auto one = foundingFathers[one_index];
      // foundingFathers.erase(one_index);
      // auto two = foundingFathers[randint(0, foundingFathers.size() - 1)];
      // foundingFathers.push_back(one);
      // // take a part from the first parent
      // int index = randint(1, one.length() - 1);
      // auto part_one = vector<string>(one.begin(), one.begin() + index);
      // if (rand() % 2 == 1)
      // {
      //   part_one = vector<string>(one.begin() + index + 1, one.end());
      // }
      // // take a part from the second parent
      // index = randint(1, len(two) - 1);
      // auto part_two = vector<string>(two.begin(), two.begin() + index);
      // if (rand() % 2 == 1)
      // {
      //   part_two = vector<string>(two.begin() + index + 1, two.end());
      // }

      // auto newMember = part_one + part_two;

      // // mutation stage
      // for (int i = 0; i < newMember.length(); i++)
      // {
      //   // if (random)
      // }


    }

    auto end = high_resolution_clock::now();
    auto runningTime = duration_cast<seconds>(end - begin).count();
  }

  return population[0];
}

int main(int argc, char const *argv[])
{
  srand((unsigned)time(0));

  cout << random() << endl;

  return 0;
}
