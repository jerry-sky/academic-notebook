---
lang: 'pl'
title: 'Optymalizacja'
author: 'Jerry Sky'
---

---

- [1. Funkcja kosztu](#1-funkcja-kosztu)
- [2. Zbiór rozwiązań dopuszczalnych $S$](#2-zbiór-rozwiązań-dopuszczalnych-s)
- [3. Optimum globalne](#3-optimum-globalne)
- [4. $\epsilon$-aproksymacja](#4-epsilon-aproksymacja)

---

## 1. Funkcja kosztu

Mamy funkcję kosztu
$$
f(\overline{x}) = \mathbb{K}^n \rightarrow \mathbb{K}
$$
która nam mówi o przydatności danego rozwiązania - chcemy jak najmniejszy koszt w celu uzyskania rozwiązania jak najbliższego optimum.

## 2. Zbiór rozwiązań dopuszczalnych $S$

Niech $S$ będzie zbiorem rozwiązań dopuszczalnych dla problemu (minimalizacyjnego) $\mathcal{P}$ o funkcji kosztu $f$.

## 3. Optimum globalne

**Rozwiązanie $s^{\star} \in S$ jest optimum globalnym $\iff$ $\forall s \in S~ f(s^{\star}) \le f(s)$.**

## 4. $\epsilon$-aproksymacja

Niech $Opt(x) = \min_{s\in S(x)} f(s)$ gdzie [zbiór $S$ jest zbiorem rozwiązań dopuszczalnych.](#zbi%c3%b3r-rozwi%c4%85za%c5%84-dopuszczalnych-s)\
Dla algorytmu $M$, który rozwiązuje problem optymalizacyjny, tż. $M(x) \in S(x)$, mówimy że jest $\epsilon$-aproksymacją dla $\epsilon \ge 0$, jeśli $\forall x$:
$$
\frac{|f(M(X)) - Opt(x)|}{\max\{Opt(x), f(M(x))\}} \le \epsilon
$$
