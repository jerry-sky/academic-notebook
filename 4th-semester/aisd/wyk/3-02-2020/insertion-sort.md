# Insertion Sort
###### 2-03-2020

## Index

  - [`Insertion sort(A,n)`](#insertion-sortan)
  - [Worst Case Analysis](#worst-case-analysis)
  - [Average Case Analysis](#average-case-analysis)

## `Insertion sort(A,n)`

$A = \{ a_1, a_2, ... a_n \}$

```pseudo
for j = 2 to n {
  key = A[j]
  i = j-1
  while( i > 0 && A[i] > key) {
    A[i+1] = A[i]
    i--
  }
  A[i+1] = key
}
```
kroki:
```
[X][ ][ ]...[ ]
 1  2  3 ... n
```


```
       m
[X][X][ ]...[a_k]|...[ ]
 1  2  3 ...k   ... n
```

## Worst Case Analysis

$max($ Liczba porównań pomiędzy elementami input'u $A)$

### Example

```
[9, 7, 5, 3, 1]
 1  2  3  4  5
[5, 7, 9, 3, 1]
```

$T(n) = \sum_{n-1}^{j=1} O(j) = O(n^2)$
$\sum_{n-1, j=1} = \binom{n}{2} = \frac{n(n-1)}{2}$

## Average Case Analysis

