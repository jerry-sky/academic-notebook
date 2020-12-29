---
lang: 'pl'
title: 'Zamiana zmiennych'
author: 'Jerry Sky'
date: '2020-03-09'
---

---

$T(n) = 2T(\sqrt{n}) + \log_2 n$\
$m = \log_2 n$, $n = 2^m$, $S(m) = T(2^n) = T(n)$\
$T(2^m) = 2\cdot T(2^{\frac{n}{2}}) + m$

$S(n) = 2\cdot S(\frac{n}{2}) +m = \Theta(m\log m)$ - ta równość wynika z poprzednich metod

$$
T(n) = S(m) = \Theta(m\log m) =\Theta\big((\log n) \cdot (\log \log n)\big)
$$
