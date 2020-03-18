# Liniowa złożoność obliczeniowa
*(2020-03-16)*

Aby osiągnąć sortowanie o złożoności $O(n)$ należy dodać dodatkowe założenia na dane wejściowe *(wyjść poza [comparison model](comparison-model.md))*, takie jak **sortujemy liczby naturalne** z danego przedziału.

## `CountingSort`

- Input: $A = (a_1,\dots,a_n), \forall{j}~a_j \in \{1,\dots,k\}$
- posortowany ciąg jest zwracany w tablicy $B = (a_1',\dots,a_n')$, w trakcie sortowania używana jest tablica pomocnicza $C$ wielkości $k$
- Złożoność obliczeniowa $O(n+k)$. Jeśli $k = O(n)$ wtedy `CountingSort` ma złożoność $O(n)$

Własność stabilności sortowania:\
algorytm sortowania musi zachowywać porządek równych sobie elementów.\
`CountingSort` ma własność stabilności sortowania.

## `RadixSort`

Użycie np. [`CountingSort`a](#countingsort) aby sortować w złożoności linowej z przedziału wielkości $n^d$, gdzie $d$ jest stałe.

Złożoność `RadixSort`a to $O(d \cdot n)$
