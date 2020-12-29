---
lang: 'pl'
title: 'Select'
author: 'Jerry Sky'
date: '2020-03-23'
---

---

- [Description](#description)
- [Algorithm](#algorithm)
- [Complexity](#complexity)

---

## Description

`Select` jest pięknym przykładem nietrywialnego wykorzystania [metodologii dziel i zwyciężaj](../2020-03-09/divide-and-conquer.md).

Składa się on z 5 kroków *(w tym dwa rekurencyjne)*.

## Algorithm

1. Najpierw znajdowany jest element $x$ tablicy $A$ zwany medianą median, dla którego zapewnione jest, że liczba elementów tablicy $A$ większych od $x$ jest nie mniejsza niż $\frac{3n}{10} - 6$.
2. Następnie wykorzystuje się element $x$ jako pivot do procedury [`partition`](../2020-03-11/quick-sort.md#pseudocode-partition) i wykonuje dalsze dalsze kroki podobnie jak to miało miejsca w przypadku [algorytmu `RandomSelect`](random-select.md).

## Complexity

Dzięki temu, że mediana median $x$ jest wykorzystywana jako pivot możemy pokazać, że liczba porównań $T(n)$ *(dla $n$ odpowiednio dużego)* jest zadana następującą rekurencją:
$$
T(n) \le T\left(\left\lceil\frac{n}{5}\right\rceil\right) + T\left(n - \left(\frac{3n}{10} - 6\right)\right) + \Theta(n)
$$
Rozwiązując tę rekurencję metodą dowodu indukcyjnego możemy pokazać, że algorytm `Select` działa w złożoności $O(n)$ *(Worst Case Analysis)*.

Więcej informacji [tutaj](http://people.csail.mit.edu/rivest/pubs/BFPRT73.pdf) oraz [tutaj (9.3)](https://web.ist.utl.pt/~fabio.ferreira/material/asa/clrs.pdf).
