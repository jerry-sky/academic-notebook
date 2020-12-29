---
lang: 'pl'
title: 'Kod Shannon’a raz jeszcze'
author: 'Jerry Sky'
date: '2020-10-29'
---

---

([wcześniejsza notatka](../2020-10-15/kod-shannona.md))

- [1. *Co wiemy o kodach Shannon’a?*](#1-co-wiemy-o-kodach-shannona)
    - [1.1. Frukt](#11-frukt)
- [Twierdzenie Shannon’a raz jeszcze](#twierdzenie-shannona-raz-jeszcze)
- [Uwaga o kodach Shannon’a](#uwaga-o-kodach-shannona)

---

## 1. *Co wiemy o kodach Shannon’a?*

$$
H(X) \le L_{Sh}(X) \le H(X) + 1 \qquad (\star)
$$

---
Teraz kodujemy słowa długości $n$ nad alfabetem $X$.\
Formalnie: patrzymy na $X_n = \underbrace{X \times X \dotsb \times X}_{n}$

$$
P(\{(a_1, \dots, a_n)\}) = p_{a_1} \cdot p_{a_2} \cdots p_{a_n}
$$

$$
H(X_n) = n \cdot H(X) \qquad \text{(ćw.)}
$$

Używamy kodowania Shanonn’a dla elementów $X$ i kodujemy elementy $X_n$.
$$
L(X_n) = n \cdot L_{Sh}(X) \qquad \text{(ćw.)}
$$

---

### 1.1. Frukt

Z [„$\star$”](#1-co-wiemy-o-kodach-shannona):
$$
n \cdot H(X) \le n \cdot L_{Sh}(X) \le H(X_n) + 1 = n \cdot H(X) + 1\\
H(X) \le \frac{L(X_n)}{n} \le H(X) + \frac{1}{n}.
$$

---

## Twierdzenie Shannon’a raz jeszcze

*biorąc pod uwagę [Frukt z poprzedniego punktu](#11-frukt):*
$$
\lim_{n \to \infty} \frac{L(X_n)}{n} = H(X)
$$

---

## Uwaga o kodach Shannon’a

*Kody Shannon’a bywają nieoptymalne.*

Bez straty ogólności dla $|X| = N$ jest skończenie wiele (rozsądnych) kodów.\
(Można ograniczyć długość słowa kodowego przez ?)

**Zrobimy optymalne kody!**\
*[Kody Huffmana](kody-huffmana.md)*

Kodowanie Shannon’a nie jest jednoznaczne!

---
