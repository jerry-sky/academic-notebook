---
lang: 'pl'
title: '`LocalSearch`'
author: 'Jerry Sky'
---

---

- [1. Outline](#1-outline)
- [2. *Concerns*](#2-concerns)

---

## 1. Outline

1. Generujemy *w jakiś sposób (losowo nie zawsze jest dobrze)* rozwiązanie początkowe $x_0$.
2. Dopóki jakiś warunek jest `True` robimy:
   1. Generujemy sąsiedztwo aktualnego rozwiązania $N(x)$.
   2. Jeśli $\exists_{\hat{x}\in N(x)}~ f(\hat{x}) < f(x)$ wówczas $x_0 := \hat{x}$
3. `return` $x_0$.

## 2. *Concerns*

1. Jak dobrać $x_0$?
   1. Funkcja w której szukamy $\min$ - losowo
   2. [TSP][tsp] - lokalnie rozglądać się za minimalnym kosztem przejścia z miasta do miasta
2. Co oznacza, że dwa rozwiązania są sąsiednimi?
   1. Są podobne do siebie, ale różnią się np. transpozycją jakiejś pary $(i,j)$ jeśli mowa o sekwencjach elementów.
3. Ile rozwiązań sąsiednich sprawdzać?
   1. *All of 'em.*
4. W jakiej kolejności sprawdzać sąsiedztwo.
   1. W takiej w jakiej zwróciła funkcja sąsiedztwa.
      1. W jakiej kolejności generować sąsiedztwo?
         1. Nie ma znaczenia.
5. Kiedy skończyć procedurę?
   1. Po przejściu wielu iteracji bez żadnego polepszenia osiągniętego wyniku od jakiegoś czasu.
   2. Po przekroczeniu czasu.
6. Co w przypadku $f(x) = f(\hat{x})$?
   1. *W większości przypadków* zignorować $\hat{x}$.
7. Problemy dyskretne vs. ciągłe, wypukłe vs. niewypukłe
8. Ekstrema lokalne


[tsp]: https://en.wikipedia.org/wiki/Travelling_salesman_problem
