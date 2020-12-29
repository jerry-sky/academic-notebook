---
lang: 'pl'
title: 'Insertion Sort'
author: 'Jerry Sky'
date: '2020-03-02'
---

---

- [`Insertion sort(A,n)`](#insertion-sortan)
- [Worst Case Analysis](#worst-case-analysis)
    - [Example](#example)
- [Average Case Analysis](#average-case-analysis)

---

## `Insertion sort(A,n)`

$A = \{ a_1, a_2, ... a_n \}$

```
for j = 1 to n {
  key = A[j]
  i = j-1
  while( i >= 0 && A[i] > key) {
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

$$
T(n) =
\sum^{n-1}_{j=1} O(j) =
O\Bigg(
  \sum^{n-1}_{j=1}j
\Bigg) = (*)
$$
przy czym
$$
\sum^{n-1}_{j=1}j = \binom{n}{2} = \frac{n(n-1)}{2}
$$
dlatego
$$
(*) = O(n^2)
$$

## Average Case Analysis
