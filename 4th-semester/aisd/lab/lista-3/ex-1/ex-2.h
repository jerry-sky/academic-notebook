#include <iostream>
#include <time.h>
#include <string>
#include <fstream>
#include <unistd.h>

#include "shared/algorithms.h"
#include "shared/swap-and-compare.h"
#include "shared/algorithms/quick-sort.h"
#include "shared/algorithms/dual-pivot-quick-sort.h"
#include "shared/algorithms/insertion-sort.h"
#include "shared/algorithms/merge-sort.h"
#include "shared/algorithms/radix-sort.h"

void Exercise2(Algorithm algorithm, SwapNCompare *snc, std::string stat_file, int k);
