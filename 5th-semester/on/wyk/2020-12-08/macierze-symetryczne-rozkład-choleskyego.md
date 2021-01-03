---
lang: 'pl'
title: 'Macierze Symetryczne, Rozkład Choleskyego'
author: 'Jerry Sky'
date: 2020-12-08
---

---

- [1. Macierze Symetryczne](#1-macierze-symetryczne)
    - [1.1. Zmodyfikowany rozkład $LU$](#11-zmodyfikowany-rozkład-lu)
    - [1.2. Sposób liczenia wektora $x$](#12-sposób-liczenia-wektora-x)
    - [1.3. Ostatecznie](#13-ostatecznie)
- [2. Rozkład Choleskyego](#2-rozkład-choleskyego)
    - [2.1. DEF: Macierz symetryczna dodatnio określona](#21-def-macierz-symetryczna-dodatnio-określona)
    - [2.2. Kolejny zmodyfikowany rozkład $LU$](#22-kolejny-zmodyfikowany-rozkład-lu)
    - [Implementacja](#implementacja)

---

## 1. Macierze Symetryczne

Problem pozostaje taki sam — mamy do policzenia wynik równania
$$
Ax = b,
$$
przy czym mamy
$$
A^T = A.
$$

### 1.1. Zmodyfikowany rozkład $LU$

Stosujemy [rozkład $LU$ tak jak wcześniej](../2020-11-24/rozwiązywanie-układu-równań-liniowych.md#14-rozkład-lu):

$$
A = L \times U
$$

przy czym teraz zapisujemy to samo nieco inaczej:

$$
L U = L D \overline{U}
$$

gdzie

- $$
  L =
    \begin{bmatrix}
        1\\
        l_{21} & 1\\
        l_{31} & l_{32} & 1\\
        \vdots &&&& \ddots\\
        l_{n1} & l_{n2} & \dotsb && l_{n,n-1} & 1
    \end{bmatrix}
  $$

- $$
  \overline{U} =
    \begin{bmatrix}
        1 & u_{12} & \dots & \dots & u_{1n}\\
        & 1 & u_{23} & \dots & u_{2n}\\
        && \ddots && \vdots\\
        &&& 1 & u_{n-1,n}\\
        &&&& 1
    \end{bmatrix}
  $$

- $$
  D = \operatorname{diag}(d_i)
  $$

Warto zauważyć, że w takiej konfiguracji mamy:
$$
A^T = \overline{U}^T D L^T = L D \overline{U} = A
$$
jako, że macierz $A$ jest symetryczna.

### 1.2. Sposób liczenia wektora $x$

Jesteśmy uzbrojeni w rozkład macierzy:
$$
A = L D L^T
$$

taki, że

$$
LD =
\begin{bmatrix}
    d_1\\
    d_1 l_{21} & d_2\\
    d_1 l_{31} & d_2 l_{32} & d_3\\
    \vdots & && \ddots\\
    d_1 l_{n1} & d_2 l_{n2} &\dots&& d_n
\end{bmatrix}
\\[10pt]

L^T =
\begin{bmatrix}
    1 & l_{21} & l_{31} & \dots & l_{n1}\\
    & 1 & l_{32} & \dots & l_{n2}\\
    && \ddots && \vdots\\
    &&&& 1
\end{bmatrix}
\\[10pt]

A =
\begin{bmatrix}
    a_{11} & a_{21} & a_{31} & \dots & a_{n1}\\
    a_{21} & a_{22} & a_{32} & \dots & a_{n2}\\
    a_{31} & a_{32} & a_{33} & \dots & a_{n3}\\
    \vdots &&&& \vdots\\
    a_{n1} & a_{n2} & a_{n3} & \dots & a_{nn}\\
\end{bmatrix}
$$

Czyli liczymy po kolei:

1. mamy $d_{1} = a_{11}$, czyli wiemy ile wynosi $d_{1}$
2. mamy:
    - $d_1 l_{21} = a_{21}$ — z tego wyznaczamy $l_{21}$
    - $d_1 l_{21} \cdot l_{21} + d_2 = a_{22}$ — z tego wyznaczamy $d_2$
3. mamy:
    - $d_1 l_{31} = a_{31}$ — z tego wyznaczamy $l_{31}$
    - $d_1 l_{31} \cdot l_{21} + d_2 l_{32} = a_{32}$ — z tego wyznaczamy $l_{32}$
    - $d_1 l_{31} \cdot l_{31} + d_2 l_{32} \cdot l_{32} + d_3 = a_{33}$ — z tego wyznaczamy $d_3$
4. itd.

5. aż w końcu:
    - $d_1 l_{n1} = a_{n1}$
    - $d_1 l_{n1} \cdot l_{21} + d_2 l_{n2} = a_{n2}$
    - …
    - $d_1 l_{n1} \cdot l_{n1} + d_2 l_{n2} \cdot l_{n2} + \dots + d_{n-1} l_{n-1, n} \cdot l_{n-1, n} + d_n = a_{nn}$

Możemy dodatkowo określić ciąg $r_j = d_i l_{n,j}$ i go zastosować w obliczeniach.

Powyższy algorytm w formie programu:

1. `for` $k := 1$ `to` $n$:
    1. `for` $j := 1$ `to` $k-1$:
        1. $r_{j} := a_{k,j} - \sum_{q=1}^{j-1} l_{j,q} \cdot r_{q}$
        2. $l_{k,j} := \frac{r_j}{d_j}$
    2. $d_k := a_{k,k} - \sum_{q=1}^{k-1} l_{k,q} \cdot r_q$

W faktycznej implementacji przechowywanie danych wyglądałoby następująco:

- macierze trójkątne $L, A$ w jednej macierzy $n\times n$,
- macierz diagonalną $D$ jako wektor,
- ciąg $r_j$ jako wektor.

---

### 1.3. Ostatecznie

Czyli mając
$$
Ax = b
$$
robimy
$$
L D L^T x = b
$$
i podstawiamy
$$
\begin{cases}
    z = L^T x & O\left( \frac{1}{2} n^2 \right)\\
    D z = y & O\left( n \right)\\
    L y = b & O\left( \frac{1}{2} n^2 \right)\\
\end{cases}
$$

Złożoność obliczeniowa: $O\left( \frac{1}{6} n^3 \right) + O\left( n^2 \right) + O(n)$.

---

## 2. Rozkład Choleskyego

Mamy

$$
Ax = b
$$

i tak jak [wcześniej](#1-macierze-symetryczne) macierz $A$ jest symetryczna, ale tym razem macierz $A$ jest [dodatnio określona](#21-def-macierz-symetryczna-dodatnio-określona).

---

### 2.1. DEF: Macierz symetryczna dodatnio określona

Macierzą symetryczną $A^T = A \in \mathbb{R}^{n\times n}$ nazywamy dodatnio określoną,\
jeśli dla dowolnego niezerowego wektora $x \in \mathbb{R}^n$ spełniona jest nierówność $x^T A x > 0$

---

### 2.2. Kolejny zmodyfikowany rozkład $LU$

Wprowadzamy małą modyfikację do [wcześniej określonego rozkładu](#11-zmodyfikowany-rozkład-lu):
$$
A = L U = L D L^T = \overbrace{L \sqrt{D}}^{\hat{L}} \overbrace{\sqrt{D} L^T}^{\hat{L}^T} = \hat{L} \hat{L}^T
$$

gdzie

- $D = \operatorname{diag}(d_i)$
- $\sqrt{D} = \operatorname{diag}(\sqrt{d_i})$

*(robimy pierwiastki, więc potrzebujemy macierzy dodatnio określonych)*

---

### Implementacja

Mamy:
$$
\begin{bmatrix}
    \hat{l}_{11}\\
    \hat{l}_{21} & \hat{l}_{22}\\
    \vdots && \ddots\\
    \hat{l}_{n1} & \hat{l}_{n2} & \dots &\hat{l}_{nn}
\end{bmatrix}
\times
\begin{bmatrix}
    \hat{l}_{11} & \hat{l}_{21} & \dots & \hat{l}_{n1}\\
    & \hat{l}_{22} & \dots & \hat{l}_{n2}\\
    && \ddots & \vdots\\
    &&& \hat{l}_{nn}\\
\end{bmatrix}
=
\begin{bmatrix}
    a_{11} & a_{21} & \dots & a_{n1}\\
    a_{21} & a_{22} & \dots & a_{n2}\\
    \vdots &&& \vdots\\
    a_{n1} & a_{n2} & \dots & a_{nn}\\
\end{bmatrix}
$$

I podobnie jak [wcześniej](#12-sposób-liczenia-wektora-x) mamy równania postaci:

1.
    - $\hat{l}_{11} \cdot \hat{l}_{11} = a_{11}$
    - $\hat{l}_{i1} \hat{l}_{11} = a_{i1} \quad i = 2,\dots,n$
2.
    - $\hat{l}_{21}^2 + \hat{l}_{22}^2 = a_{22}$
    - $\hat{l}_{i1} \cdot \hat{l}_{21} + \hat{l}_{i2} \cdot \hat{l}_{22} = a_{i2} \quad i = 3,\dots,n$
3. …
4. ($j$-ta kolumna):
    - $\hat{l}_{j1}^2 + \hat{l}_{j2}^2 + \dots + \hat{l}_{jj}^2 = a_{jj}$
    - $\hat{l}_{i1} \cdot \hat{l}_{j1} + \hat{l}_{i2} \cdot \hat{l}_{j2} + \dots + \hat{l}_{ij} \cdot \hat{l}_{jj} = a_{ij} \quad i = j+1,\dots,n$

Program:

1. `for` $j := 1$ `to` $n$:
    1. $\hat{l}_{jj} := \sqrt{a_{jj} - \sum_{k=1}^{j-1} \hat{l}_{jk}^2}$
    2. `for` $i := j+1$ `to` $n$:
        1. $\hat{l}_{ij} := \frac{a_{ij} - \sum_{k=1}^{j-1} \hat{l}_{ik} - \hat{l}_{jk}}{\hat{l}_{jj}}$

W pamięci przechowujemy:

- macierze trójkątne $A$ i $\hat{L}$ w macierzy $n \times n$ oraz jednym wektorze (mamy kolizję — obie macierze trójkątne mają wartości niekoniecznie równe wektorowi złożonego z jedynek)

Dostajemy układ równań:

$$
\begin{cases}
    \hat{L} y = b & O\left( \frac{1}{2}n^2 \right)\\
    \hat{L} x = y & O\left( \frac{1}{2}n^2 \right)\\
\end{cases}
$$

Złożoność obliczeniowa: $O\left(\frac{1}{6} n^3\right) + O(n^2)$.

---
