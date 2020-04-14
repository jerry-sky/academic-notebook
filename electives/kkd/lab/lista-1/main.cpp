#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;

/**
 * An analysis of a file's characters.
 */
class FileAnalysis
{
private:
  /**
   * A stream of the file's contents.
   */
  ifstream file;

  string filePath;

  int possibleCharactersCount = 256;
  /**
   * How many times a character has appeared in the file.
   */
  int countOne[256] = {};
  /**
   * How many time a character has appeared after another one.
   */
  int countTwo[256][256] = {};
  /**
   * Total character count - how many characters there are in the file in total.
   */
  int totalCount = 0;

  void init(string filePath)
  {
    file.open(filePath);

    unsigned char current = 0;
    unsigned char previous = 0;
    while (!file.eof())
    {
      this->countOne[current]++;
      this->countTwo[previous][current]++;

      // get the next character
      previous = current;
      current = file.get();

      this->totalCount++;
    }
  }

public:
  FileAnalysis(string filePath)
  {
    this->filePath = filePath;
    this->init(filePath);
  }

  double ConditionalProbability(char x, char y)
  {
    return 1.0 * this->countTwo[x][y] / this->countOne[x];
  }

  double Probability(char x)
  {
    return 1.0 * this->countOne[x] / this->totalCount;
  }

  double ConditionalInformation(char x, char y)
  {
    return -1.0 * log2(this->ConditionalProbability(x, y));
  }

  double Information(char x)
  {
    return -1.0 * log2(this->Probability(x));
  }

  double Entropy()
  {
    double output = 0.0;
    int count = 0;
    for (int x = 0; x < possibleCharactersCount; x++)
    {
      if (this->countOne[x])
      {
        output += -1.0 * log2(this->countOne[x]) * this->countOne[x];
        count++;
      }
    }

    output /= this->totalCount;
    return output + log2(this->totalCount);
  }

  double ConditionalEntropy()
  {
    double output = 0.0;
    for (int x = 0; x < possibleCharactersCount; x++)
    {
      for (int y = 0; y < possibleCharactersCount; y++)
      {
        if (this->countOne[x] && this->countTwo[x][y])
          output += 1.0 *
                    this->countTwo[x][y] / this->totalCount * (-1 * log2(this->countTwo[x][y]) + log2(this->countOne[x]));
      }
    }
    return output;
  }

  void printResults()
  {
    double e = this->Entropy();
    double ce = this->ConditionalEntropy();

    cout << this->filePath << endl;
    cout << "  Entropy:               " << e << endl;
    cout << "  Conditional entropy:   " << ce << endl;
    cout << "  Difference:            " << e - ce << endl;
  }
};

int main(int argc, char const *argv[])
{

  if (argc < 2)
  {
    cout << "usage: ./main.out <input_file_path>" << endl;
    return 0;
  }

  string inputFilePath = argv[1];

  FileAnalysis *fa = new FileAnalysis(inputFilePath);

  fa->printResults();

  return 0;
}
