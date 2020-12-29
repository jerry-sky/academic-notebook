---
lang: 'pl'
title: 'Travelling salesman problem'
author: 'Jerry Sky'
---

---

- [1. Rozwiązanie $x_0$](#1-rozwiązanie-x_0)
- [2. Sąsiedztwo](#2-sąsiedztwo)
- [3. Pętla główna](#3-pętla-główna)
- [4. Koniec](#4-koniec)
- [5. Najlepszy znany LocalSearch dla TSP](#5-najlepszy-znany-localsearch-dla-tsp)

---

## 1. Rozwiązanie $x_0$

1. Podczas generowania wybierać najkrótszą drogę do następnego miasta.
2. Losowa permutacja - *discouraged*.

## 2. Sąsiedztwo

1. Zamiana wierzchołków [2–opt][2-opt], ewentualnie [3-opt][3-opt]. Dwa rozwiązania $x_0,\hat{x}$ są sąsiednie $\iff$ $|$`diff x,y`$| = 2$ *(mamy tylko dwie różnice)*

    $$
    \begin{aligned}
    x_0 =&~ \langle~1,2,3,4,5,6,1~\rangle\\
    \hat{x} =&~ \langle~1,\bold3,\bold2,4,5,6,1~\rangle
    \end{aligned}
    $$

2. Zamiana krawędzi k–opt. W sąsiedztwie $x_0$ leżą wszystkie rozwiązania, w których $k$ nieincydentnych krawędzi zastępujemy innymi np. dla $k=2$:

    $$
    \begin{aligned}
      \hat{x} =&~ \lang~1,2,3,\bold5,\bold4, 6,1~\rang\\
      \hat{x}_2 =&~ \lang~1,\bold4,3,\bold2,5,6,1~\rang
    \end{aligned}
    $$

    dla $k=3$:

    $$
    \begin{aligned}
      \hat{x} =&~ \lang~1,2,\bold6,\bold5,\bold3,\bold4,1~\rang\\
      \hat{x}_2 =&~ \lang~1,2,\bold4,\bold3,\bold6,\bold5,1~\rang
    \end{aligned}
    $$

3. Inwersja podciągu. Wybieramy $i,j$ a następnie odwracamy kolejność ciągu $x^{(i)}\dots x^{(j)}$, np.

    $$
    \hat{x} = \lang~1,2,\bold6,\bold5,\bold4,\bold3,1~\rang
    $$


## 3. Pętla główna

Sprawdzamy tak długo aż nie znajdziemy lepszego sąsiada lub sprawdzimy wszystkich sąsiadów

## 4. Koniec

Brak lepszych sąsiadów lub koniec czasu.

## 5. Najlepszy znany LocalSearch dla [TSP][tsp]

Połączenie pomiędzy 2–opt a 3–opt.

[*Sh. Lin, B. Kernighan’73 – „An Effective Heuristic Algorithm for the Traveling-Salesman Problem”*][effective-alg]

[tsp]: https://en.wikipedia.org/wiki/Travelling_salesman_problem

[2-opt]: http://matejgazda.com/tsp-algorithms-2-opt-3-opt-in-python/

[3-opt]: http://tsp-basics.blogspot.com/2017/03/3-opt-move.html

[effective-alg]: https://www.cs.princeton.edu/~bwk/btl.mirror/tsp.pdf
