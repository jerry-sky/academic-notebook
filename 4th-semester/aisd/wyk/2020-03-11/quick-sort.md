# Quick Sort
*(2020-03-11)*

## The QuickSort sorting algorithm

### Pseudocode `QuickSort`
Input:
- `Arr` - array to sort
- `left` - starting index
- `right` - ending index

Uses:
- [`partition`](#pseudocode-partition)

Pseudocode:
```
function QuickSort(Arr, left, right):
  if left < right:
    select a PivotIndex
    pivotNewIndex :=
      partition(Arr, left, right, PivotIndex)

    QuickSort(Arr, left, pivotNewIndex-1)
    QuickSort(Arr, pivotNewIndex+1, right)
```

### Pseudocode `partition`
Input:
- `Arr` - array to partition
- `left` - starting index
- `right` - ending index

Pseudocode:
```
function partition(Arr, left, right, PivotIndex):
  pivot = Arr[PivotIndex]

  i := left - 1 // index of smaller element

  for j = left, j <= right - 1, j++:
    if Arr[j] < pivot:
      i++ // increment the index of smaller element
      swap Arr[i] and Arr[j]
  swap Arr[i + 1] and Arr[right]
  return i+1
```

## Resolving the asymptotic of `QuickSort`

Assumptions:
- $\forall x_i,x_j \in Arr : x_i \neq x_j$ for $i\neq j$
- all permutations of the $Arr$ sequence have the same probability of appearance
- $|Arr| = n$

$Q_n$ - average number of comparisons used by QuickSort function

Clearly $Q_0 = Q_1 = 0$.

Let $n \ge 2$. After selecting an arbitrary pivot element there are $n-1$ comparisons because of the [`partition` function](#pseudocode-partition) invoked by the [`QuickSort` function](#pseudocode-quicksort).
The `partition` function has divided `Arr` into two pieces: left and right with the pivot in the middle.
Assuming the left part is of length $k$ then the right part is of length $n-1-k$. Please note that all $k \in \{0,\dots,n-1\}$ are equal probability of appearance.\
Which gives us following equation for $Q_n$:
$$
Q_n = (n-1) + \frac{1}{n} \sum_{k=0}^{n-1}(Q_k + Q_{n-1-k})
$$

However $\sum_{k=0}^{n-1}Q_{n-1-k} = \sum_{k=0}^{n-1}Q_k$ thus we can rewrite the above equation in a more clear way:
$$
Q_n = (n-1) + \frac{2}{n}\sum_{k=0}^{n-1}Q_k
$$

**This is the Quick Sort Equation.**\
See [this paper by Jacek Cichoń][cichoń] on how to solve this equation.

We get
$$
Q_n = (n+1) (4H_{n+1} - 2H_n -4)
$$
where [$H_n$ is the $n$th harmonic number](https://en.wikipedia.org/wiki/Harmonic_number).

We need to obtain an asymptotic of the terms $Q_n$. See [this paper by Jacek Cichoń][cichoń] on how to obtain this asymptotic.

We have
$$
Q_n = 2n(\ln n + \gamma -2) + 2\ln n + 2\gamma + 1 + O\Big(\frac{1}{n}\Big)
$$
where $\gamma$ is the [Euler-Mascheroni constant](https://en.wikipedia.org/wiki/Euler%E2%80%93Mascheroni_constant)
Above equation can obviously be written as
$$
T(n) = 2n(\ln n + \gamma -2) + 2\ln n + 2\gamma + 1 + O\Big(\frac{1}{n}\Big)
$$
to adhere to the format of previous algorithm analyses we performed.

Above equation describes what is the average time complexity of the `QuickSort` function.

Sources:
- [QuickSort - Average Complexity by Jacek Cichoń][cichoń]
- [QuickSort - GeeksForGeeks][geeks]

[cichoń]: https://cs.pwr.edu.pl/cichon/Math/QSortAvg.pdf
[geeks]: https://www.geeksforgeeks.org/quick-sort/
