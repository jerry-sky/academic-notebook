---
lang: 'pl'
title: 'Rekurencja'
author: 'Jerry Sky'
date: '2020-03-02'
---

---

- [$1\degree$ Metoda indukcyjna](#1degree-metoda-indukcyjna)

---

## $1\degree$ Metoda indukcyjna

$$
T(n) = 4\cdot T\Big(\frac{n}{2}\Big) + n
$$
$$
T(1) = \Theta(1)
$$
*Założenie indukcyjne:*
$$
\forall{k<n}:~ T(k) \le c \cdot k^3
$$
Robimy krok indukcyjny
$$
T(n) = 4\cdot T\Big(\frac{n}{2}\Big) + n \le 4c \cdot \frac{n^3}{2^3} + n =
$$
$$
= c \cdot n^3 + \Big( -\frac{c \cdot n^3}{2} + n \Big) \le c \cdot n^3
$$
przy czym
$$
\Big( -\frac{c \cdot n^3}{2} + n \Big) \le 0
$$
wówczas

$$
-\frac{cn^3}{2} + n \le 0
$$
$$
\frac{cn^2}{2} \ge 1
$$

$$
c = 2, n_0 = 1
$$
$$
T(n) = O(n^3)
$$

---
$$
T(n) = O(n^2)
$$
*Założenie indukcyjne*
$$
\forall{k < n}:~ T(k) \le ck^2
$$
Krok indukcyjny
$$
T(n) \le 4\cdot\frac{cn^2}{2^2} + n = cn^2 + n \not\le cn^2
$$

---
*Założenie indukcyjne*
$$
\forall{k < n }: T(k) \le c_1k^2 - c_2k
$$
Krok indukcyjny
$$
T(n) \le 4\Big( c_1\frac{n^2}{4} - c_2 \frac{n}{2} \Big) + n =
$$
$$
= c_1n^2 - 2c_2n + n \le c_1n^2 - c_2n =
$$
$$
c_1n^2 - c_2n + \big(c_2n + n\big) \le c_1n^2 + c_2n
$$
przy czym
$$
(c_2n + n) \le 0
$$
wówczas

$$
-c_2n + n \le 0
$$
$$
c_2 \ge 1
$$
$$
T(1) \le c_1 - c_2 \ge 0
$$

$$
T(n) = O(n^2)
$$
