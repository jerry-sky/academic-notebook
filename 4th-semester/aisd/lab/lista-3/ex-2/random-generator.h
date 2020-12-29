#include <stdlib.h>
#include <time.h>
#include <vector>

/**
 * Generates a random array of integers.
 *
 * @param `n` - array size
 * @param `unique` - if the numbers in this sequence should be unique
 *    (a permutation of set {1..n} or just random numbers)
 */
std::vector<int> RandomGenerator(int size, bool unique);
