---
lang: 'pl'
title: 'Drzewo rekursji'
author: 'Jerry Sky'
date: '2020-03-09'
---

---

$T(n) = T\big(\frac{n}{2}\big) = T\big(\frac{n}{4}\big) + n^2$, $T(1) = \Theta(1)$

\<insert tree>

$\rightarrow$ rozmiar
1. $n^2$ $\rightarrow$ $n$
   1. $(\frac{n}{2})^2$ $\rightarrow$ $\frac{n}{2} + \frac{n}{4}$
      1. $(\frac{n}{4})^2$ $\rightarrow$ $\frac{n}{4} + 2 \cdot \frac{n}{16}$
      2. $(\frac{n}{8})^2$ $\rightarrow$ $\frac{n}{4} + 2 \cdot \frac{n}{16}$
   2. $(\frac{n}{4})^2$ $\rightarrow$ $\frac{n}{2} + \frac{n}{4}$
      1. $(\frac{n}{8})^2$ $\rightarrow$ $\frac{n}{4} + 2 \cdot \frac{n}{16}$
      2. $(\frac{n}{16})^2$ $\rightarrow$ $\frac{n}{4} + 2 \cdot \frac{n}{16}$

Koszt:

1. $n^2$
2. $n^2 \cdot \frac{15}{16}$
3. $n^2 \cdot \frac{25}{256} = n^2 \cdot (\frac{5}{16})^2$
4. $n^2 \cdot (\frac{5}{16})^3$

\<insert tree>

$height = \log n +1$

$\frac{n}{2^x} = 1$\
$x = \log_2n$

mamy $\sum_{j=0}^{\infin}q^j = \frac{1}{1-q}$ dla $|q| < 1$

$T(n) \le \sum_{k=0}^{\log n}n^2 \cdot (\frac{5}{16})^k \le n^2 \cdot \sum_{k=0}^{\infin}\big(\frac{5}{16}\big)^k = \frac{16}{11} n^2$

$T(n) = O(n^2)$

$\sum_{k=0}^{\log n}n^2 \cdot (\frac{5}{16})^k = n^2(\frac{16}{11} - 5\cdot (\frac{5}{16})^{\log n})=$\
$n^2(\frac{16}{11} - 5\cdot n^{\log \frac{5}{16}})$, $\log(\frac{5}{16}) = -1.67$
