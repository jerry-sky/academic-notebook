# Divide and conquer
*(2020-03-9)*

## Binary search$(x, A)$
$A$ - posortowana tablica

1. Dziel: porównujemy $x$ ze środkowym elementem z $A$
2. $\lor$ $\downdownarrows$
   1. Jeśli $x == A\big(\frac{n}{2}\big)$ $\rightarrow$ kończymy
   2. Jeśli $x < A\big(\frac{n}{2}\big)$ $\rightarrow$ Binary Search$\Big(~x, A\big[1..., \frac{n}{2} -1\big]~\Big)$
   3. Oth $x > A\big(\frac{n}{2}\big)$ $\rightarrow$ Binary Search$\Big(~x, A\big[\frac{n}{2}, ..., n\big]~\Big)$

### Worst case analysis

$T(n) = O(1) + T(\frac{n}{2})$ $\rightarrow~T(n) = O(\log n)$ z [Master theorem](master-theorem.md)

## Podnoszenie do potęgi $x^n$

$\rightarrow$ n razy: $x \cdot x \cdot x \cdot ... \cdot x$ $\rightarrow$ #mnożeń $= O(n)$

### [Divide and conquer case](#divide-and-conquer)

$$
x^n =
\begin{aligned}
\begin{cases}
  x^{\frac{n}{2}} \cdot x^{\frac{n}{2}} &: n \% 2 = 0\\
  x^{\frac{n-1}2} \cdot x^{\frac{n-1}{2}} \cdot x &: oth
\end{cases}
\end{aligned}
$$
$T(n) = 1\cdot T(\frac{n}{2}) + O(1) = O(log n)$

## Liczenie $n$-tej liczby Fibonacciego

$$
F_n =
\begin{aligned}
\begin{cases}
  0 &: n = 0\\
  1 &: n =1\\
  F_{n-1} + F_{n-2} &: oth
\end{cases}
\end{aligned}
$$

### Brute force
$\Theta(\phi^n)$, gdzie $\phi = \frac{1 + \sqrt{5}}{2}$

### Podejście *bottom-up*
$F_2, F_3, F_4,...F_n$ $\rightarrow$ $\Theta(n)$

$F_n = \frac{1}{\sqrt{5}} \phi^n \plusmn \frac{1}{\sqrt{5}}\Big(\frac{1- \sqrt{5}}{2}\Big)^n$ $\rightarrow~O\big(\log n\big)$ mnożeń $\rightarrow$ przybliżenie z $\sqrt{5}$


