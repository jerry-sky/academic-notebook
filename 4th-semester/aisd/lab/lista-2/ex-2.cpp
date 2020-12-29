#include "ex-2.h"

void Exercise2(Algorithm algorithm, SwapNCompare *snc, std::string stat_file, int k)
{
  srand(time(NULL));
  for (int i = 0; i < k; i++)
  {
    for (int n = 100; n <= 10000; n += 100)
    {
      snc->reset();
      int *input = (int *)malloc(sizeof(int) * n);
      for (int j = 0; j < n; j++)
      {
        input[j] = rand() % n;
      }
      Sort *sort;

      switch (algorithm)
      {
      case Insertion:
        sort = (Sort *)new InsertionSort(input, n, snc);
        break;
      case Merge:
        sort = (Sort *)new MergeSort(input, n, snc);
        break;
      case DualPivotQuick:
        sort = (Sort *)new DualPivotQuickSort(input, n, snc);
        break;
      default:
      case Quick:
        sort = (Sort *)new QuickSort(input, n, snc);
        break;
      }

      // measure sorting time
      clock_t begin;
      clock_t end;
      begin = clock();
      sort->sort();
      end = clock();

      std::ofstream outfile;
      outfile.open(stat_file, std::ios_base::app);
      outfile << n << " " << snc->getComparisonsCounter() << " "
              << snc->getSwapsCounter() << " " << (double)(((double)end - begin) / CLOCKS_PER_SEC) << std::endl;

      outfile.close();

      snc->reset();
    }
  }
}
