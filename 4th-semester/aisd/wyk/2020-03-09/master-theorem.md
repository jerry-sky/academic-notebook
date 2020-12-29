---
lang: 'pl'
title: 'Master Theorem'
author: 'Jerry Sky'
date: '2020-03-09'
---

---

Jeśli $T(n) = a\cdot T\big(\lceil\frac{n}{b}\rceil\big) + O(n^d)$ ale pewnych stałych $a > 0$, $b > 1$, $d \ge 0$ wówczas:

$$
T(n) =
\begin{aligned}
\begin{cases}
  O(n^{d})&: d > \log_b a\\
  O(n^{d} \log n)&: d = \log_b a\\
  O(n^{\log_b a})&: d < \log_b a
\end{cases}
\end{aligned}
$$

\<insert graph>

problem dzielimy na $a$ podproblemów, które się dzielą też na $a$ pod-podproblemów itd.

| #d            | Rozmiar         |
| ------------- | --------------- |
| $1$           | $n$             |
| $a$           | $\frac{n}{b}$   |
| $a^2$         | $\frac{n}{b^2}$ |
| ...           | ...             |
| $a^k$         | $\frac{n}{b^k}$ |
| ...           | ...             |
| $a^{\log_2n}$ | $1$             |

$a^{\log_2n}$ = $n^{\log_ba}$

koszt $k$-tego wiersza rekursji:
$$
O\bigg(\Big(\frac{n}{b^k}\Big)^d\bigg) \cdot a^k = O\big(n^d\big) \cdot \bigg(\frac{a}{b^d}\bigg)^k s
$$
koszt całego drzewa:
$$
\sum_{k=0}^{\log_bn}O(n^d)\cdot\Big(\frac{a}{b^d}\Big)^k = O\big(n^d\big) \cdot \sum_{k=0}^{\log_bn}\Big(\frac{a}{b^d}\Big)^k
$$
mamy $\sum_{k=0}^{x}q^k = \frac{1-q^{x+1}}{1- q}$ dla $q \neq 1$
za to dla $q = 1$ mamy $\sum_{k=0}^{x}1 = x + 1$

- jest $q = \frac{a}{b^d} < 1$ wtedy $T(n) = O(n^d)$\
  tylko kiedy $\frac{a}{b^d} < 1$?\
  na $a < b^d$ robimy $\log_b$\
  $\log_ba < d$
- jeśli $q = \frac{a}{b^d} = 1 \rightarrow T(n) = O\big(n^d \log n\big)$\
  $\frac{a}{b^d} = \log_b a = d$
- jeśli $q = \frac{a}{b^d} > 1 \rightarrow T(n) = O\Big(n^d \cdot \frac{a}{b^d}^{\log_bn}\Big) =$\
  $O\Bigg(n^d \cdot \frac{a^{\log_bn}}{\big(b^{\log_bn}\big)^d}\Bigg) = O\big(n^{\log_ba}\big)$
