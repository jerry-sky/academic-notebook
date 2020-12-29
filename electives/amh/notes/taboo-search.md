---
lang: 'pl'
title: '`TabooSearch`'
author: 'Jerry Sky'
---

---

- [1. Outline](#1-outline)

---

## 1. Outline

1. Generujemy *w jakiś sposób (losowo nie zawsze jest dobrze)* rozwiązanie początkowe $x_0$.
2. Mamy zbiór tabu *(taboo)* $T = \emptyset$
3. Mamy definicję sąsiedztwa.
4. Dopóki jakiś warunek jest `True` robimy:
   1. Generujemy sąsiedztwo aktualnego rozwiązania $N(x)$.
   2. Przeszukujemy je i wybieramy najlepszego z sąsiadów.
   3. Zależnie od problemu aktualizujemy nasze $T$.
   4. Jeśli mamy lepsze rozwiązanie $\hat{x}$ to $x_0 = \hat{x}$.
5. Zmień $T$ i wróć do 4 jeśli warunek nadal jest `True`.
6. `return` $x_0$.
