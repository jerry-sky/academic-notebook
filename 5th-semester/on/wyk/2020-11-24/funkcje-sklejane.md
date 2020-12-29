---
lang: 'pl'
title: 'Funkcje sklejane'
author: 'Jerry Sky'
date: '2020-11-24'
---

---

- [1. DEF](#1-def)
- [2. Twierdzenie#4](#2-twierdzenie4)
- [3. Wyznaczanie funkcji sklejanej 3-go stopnia](#3-wyznaczanie-funkcji-sklejanej-3-go-stopnia)
    - [3.1. Przykład](#31-przykład)

---

## 1. DEF

Zadanie interpolacji za pomocą funkcji sklejanych 3-go stopnia możemy sformułować następująco:

Dla danych $n+1$ punktów $(x_i, y_i)$, gdzie $a = x_0 < x_1 < \dots < x_n = b$, znaleźć funkcję $s$ spełniającą warunki:
1. $s \in C^2 [x_0; x_n]$
2. $s\upharpoonright_{[x_{k-1}; x_k]} \equiv p_k \in \Pi_3 \enspace (1 \le k \le n)$
3. $s(x_k) = y_k \enspace (0 \le k \le n)$

Jeżeli funkcja $s$ spełnia $s''(x_0) = s''(x_n) = 0$,\
to $s$ jest **naturalną funkcją sklejaną 3-go stopnia.**

---

## 2. Twierdzenie#4

Dla dowolnych $n, x_0 < x_1 < \dotsb < x_n, y_0, y_1, \dots, y_n$ istnieje dokładnie jedna funkcja sklejana 3-go stopnia spełniająca dodatkowe warunki $s''(x_0) = s''(x_n) = 0$.

Wartości $M_k = s''(x_k) \enspace (0 \le ke \le n)$, ($M_0 = M_n = 0$) spełniają układ $n-1$ równań liniowych
$$
\lambda_k M_{k-1} + 2M_k + (1 - \lambda_k) M_{k+1} = 6 f[x_{k-1}, x_k, x_{k+1}] \quad (1 \le k \le n-1),
$$
gdzie $\lambda_k = \frac{h_k}{h_k + h_{k+1}}, \enspace h_k = x_k - x_{k-1}$.

Ponadto
$$
\begin{aligned}
    s(x) = p_k(x) &= \frac{1}{h_k}\Bigg( \frac{1}{6} M_{k-1} (x_k - x)^3\\
    &+ \frac{1}{6} M_k (x - x_{k-1})^3\\
    &+ (y_{k-1} - \frac{1}{6} M_{k-1} h^2_k) (x_k - x)\\
    &+ (y_k - \frac{1}{6} M_k h_k^2) (x - x_{k-1}) \Bigg)\\
    &\quad x_k \in [x_{k-1}, x_k].
\end{aligned}
$$

---

## 3. Wyznaczanie funkcji sklejanej 3-go stopnia

1. Obliczyć ilorazy różnicowe $d_k = 6f[x_{k-1}, x_k, x_{k+1}]$ dla $k = 1,\dots,n$, gdzie $f[x_{k-1}, x_k, x_{k+1}] = \frac{f[x_k, x_{k+1}] - f[x_{k-1}, x_k]}{x_{k+1} - x_{k-1}}$.
2. Obliczyć $\lambda_k = \frac{h_k}{h_k + h_{k+1}}$ dla $k = 1,\dots,(n-1)$.
3. Wyznaczyć $M_k$ dla $k = 1,\dots,(n-1)$ rozwiązując układ (metodą przegnania — TBA)

$$
\begin{bmatrix}
    2 & 1 - \lambda_1\\
    \lambda_2 & 2 & 1 - \lambda_2\\
    & \ddots & \ddots & \ddots\\
    && \lambda_{n-2} & 2 & 1 - \lambda_{n-2}\\
    &&& \lambda_{n-1} & 2
\end{bmatrix}
\begin{bmatrix}
    M_1\\
    M_2\\
    \vdots\\
    M_{n-2}\\
    M_{n-1}
\end{bmatrix}
=
\begin{bmatrix}
    d_1\\
    d_2\\
    \vdots\\
    d_{n-2}\\
    d_{n-1}
\end{bmatrix}
$$

Macierz powyższego układu jest diagonalnie silnie dominująca $(2 > |\lambda_k| + |1 - \lambda_k|)$. Stąd jest nieosobliwa.

---

### 3.1. Przykład

$S''(x)$ jest przedziałami liniowa, ponieważ $s$ jest przedziałami $\Pi_3$ ($s''\upharpoonright_{[x_{k-1}, x_k]} \equiv p_k'' \in \Pi_1$).

- $s''(x_{k-1}) = M_{k-1}$
- $s''(x_k) = M_k$

Narazie załóżmy, że $M_{k-1}$ i $M_k$ mamy dane. Chcemy zobaczyć, jaka jest postać drugiej pochodnej w przedziale $[x_{k-1}, x_k]$ — musimy przeprowadzić interpolację. Wiemy, że jest to wielomian co najwyżej pierwszego stopnia.\
Stosujemy [wzór Lagrange’a](../2020-11-10/interpolacja-za-pomocą-wielomianów.md#3-postać-lagrangea-wzoru-interpolacyjnego) na przedziale $[x_{k-1}, x_k]$.
$$
s''(x) = M_{k-1} \frac{(x - x_k)}{- h_k} + M_k \frac{(x - x_{k-1})}{h_k} = M_{k-1} \frac{(x_k - x)}{h_k} + M_k \frac{(x - x_{k-1})}{h_k}
$$

Teraz dwukrotnie całkujemy:
$$
s'(x) = M_{k-1} \frac{(x_k - x)^2}{-2 h_k} + M_K \frac{(x - x_{k-1})^2}{2h_k} + A
$$
$$
s(x) = M_{k-1} \frac{(x_k - x)^3}{6h_k} + M_k \frac{(x - x_{k-1})^3}{6h_k} + A(x - x_{k-1}) + B
$$

Musimy teraz jakoś wyznaczyć $A$ i $B$.
$$
s(x_{k-1}) = y_{k-1}, \enspace s(x_k) = y_k
$$
$$
s(x_{k-1}) = M_{k-1} \frac{(x_k - x_{k-1})^3}{6h_k} + B = y_{k-1} \implies\\
\implies B = y_{k-1} - \frac{h_k^2}{6}M_{k-1}
$$

$$
s(x_k) = M_k \frac{h_k^2}{6} + A\cdot h_k + y_{k-1} - M_{k-1} \frac{h_k^2}{6} = y_k \enspace \Bigg|\, /h_k
$$
$$
A = \frac{y_k - y_{k-1}}{h_k} - M_k \frac{h_k}{6} + M_{k-1} \frac{h_k}{6}
$$

Mamy już $A$ i $B$. Wstawiamy je do wzoru na $s(x)$:
$$
s(x) = \frac{1}{h_k}\Bigg( \frac{1}{6} M_{k-1} (x_k - x)^3 + \frac{1}{6} M_{k-1} (x - x_{k-1})^3 +\\
\left( y_k - y_{k-1} - \frac{M_k h_k^2}{6} + \frac{M_{k-1}h_k^2}{6} \right)(x - x_{k-1}) + y_{k-1} h_k - \frac{h_k^3}{6}M_{k-1} \Bigg)
\dots
$$
$$
s(x) = \frac{1}{h_k}\Bigg( \frac{1}{6}M_{k-1}(x_k - x)^3 + \frac{1}{6}M_{k-1}(x - x_{k-1})^3 + \left( y_k - \frac{M_k h_k^2}{6} \right)(x - x_{k-1})\\
+ \left( y_{k-1} - \frac{h_k^2}{6}M_{k-1} \right)(x_k - x)\Bigg)
$$
(tutaj trzeba pamiętać o sytuacjach typu $x_k = h_k + x_{k-1}$)

Wymagamy ciągłość 1. pochodnej w $[x_{k-1}; x_k]$.
$$
s'(x) = M_{k-1} \frac{(x_k - x)^2}{-2h_k} + M_k\frac{(x - x_{k-1})^2}{2h_k} + \frac{y_k - y_{k-1}}{h_k} - M_k \frac{h_k}{6} + M_{k-1} \frac{h_k}{6}
$$

*itd.*

---
