---
lang: 'pl'
title: 'Merge sort'
author: 'Jerry Sky'
date: '2020-03-09'
---

---

- [Example 1](#example-1)
- [Example 2](#example-2)
- [Example 3](#example-3)

---

## Example 1

$T(n) = 2T(\frac{n}{2}) + O(n)$, przy czym $a = 2$, $b = \frac{n}{2}$, $d = 1$, $\log_22 = 1$\
$T(n) = O(n\log n)$

## Example 2

$T(n) = 9T(\frac{n}{3}) + 11\cdot n^{\frac{3}{2}}$\
przy czym $a = 9$, $b = 3$, $d = \frac{3}{2}$\
$\log_3 9 = 2 > \frac{3}{2} \rightarrow T(n) = O(n^2)$

## Example 3

$T(n) = 4T(\frac{n}{2}) + \frac{n^2}{\log n}$\
mamy $a = 4$, $b = 2$,\
$\frac{n^2}{\log n} = O(n^2)$

$\overline{T}(n) = 4\overline{T}\big(\frac{n}{2}\big) + n^2$\
$\overline{T}(n) = O\big(n^2 \log n\big)$\
$T(n) = O\big(~\overline{T}(n)~\big) = O\big(n^2 \log n\big)$ $\leftarrow$ może być za duże
