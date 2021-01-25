---
lang: 'pl'
title: 'Lista 4'
author: 'Jerry Sky'
---

---

- [Zadanie 3.](#zadanie-3)

---

## Zadanie 3.

> Zastosować algorytm Hornera do obliczenia wartości $w(3)$
> $$
> w(x) = x^4 - 4x^3 + 7x^2 - 5x - 2,
> $$
> gdzie $w(3)$ jest resztą z dzielenia wielomianu $w(x)$ przez $(x-3)$. Obliczyć za pomocą algorytmu Hornera wartość pierwszej pochodnej wielomianu $w(x)$ w punkcie $3$.
>
> *Uwaga: nie wyznaczać jawnie pochodnej.*
>
> Wiadomo, że $r = 2$ jest zerem wielomianu $w(x)$. Za pomocą algorytmu Hornera wykonać deflację czynnikiem $(x-2)$.

Stosujemy algorytm Hornera:
```
    |  1 | -4 |  7 | -5 | -2 |
  3 |    |  3 | -3 | 12 | 21 |
    |  1 | -1 |  4 |  7 | 19 |
```
i uzyskujemy $w(3) = 19$.

Żeby uzyskać wartość $w'(3)$ zobaczmy jak wygląda $w(x)$ *tak fizycznie* po deflacji przez $(x-3)$:
$$
w(x) = (x-3)(x^3 - x^2 + 4x + 7) + 19
$$
Wówczas licząc pochodną mamy:
$$
w'(x) = (x^3 - x^2 + 4x + 7) + (x-3)\cdot f(x)
$$
gdzie $f(x)$ nas nie interesuje, bo jest mnożone przez czynnik, który zeruje się, kiedy liczymy $w'(3)$. Czyli mamy $w'(3) = 3^3 - 3^2 + 12 + 7 = 37$.

*Deflacja dla $(x-2)$ analogicznie.*

---
