# Rozwiązywanie układu równań liniowych

*(2020-11-24)*

- [1. Pierwszy etap eliminacji Gaussa](#1-pierwszy-etap-eliminacji-gaussa)
    - [1.1. Pseudokod](#11-pseudokod)
    - [1.2. Macierzowe sformułowanie jednego kroku](#12-macierzowe-sformułowanie-jednego-kroku)
        - [1.2.1. Kroki](#121-kroki)
        - [1.2.2. Rozkład $LU$](#122-rozkład-lu)
- [2. Drugi etap eliminacji Gaussa](#2-drugi-etap-eliminacji-gaussa)

---

## 1. Pierwszy etap eliminacji Gaussa

*Chcemy sprowadzić macierz kwadratową do macierzy trójkątnej.*

Mamy $Ax = b$, gdzie
- $A \in \reals^{n\times n}$
- $x \in \reals^n$
- $b \in \reals^n$
- $\det(A) \neq 0$

Znakiem $^{(k)}$ oznaczamy $k$-ty krok. Wówczas oczywiście $A^{(1)} = A,\enspace b^{(1)} = b$.

$$
A^{(1)} x = b^{(1)}:
\quad
\begin{matrix}
    a^{(1)}_{11} x_1 &+ &a^{(1)}_{12} x_2 &+ &\dotsb &+ &a^{(1)}_{1n} x_n &= &b^{(1)}_1\\
    a^{(1)}_{21} x_1 &+ &a^{(1)}_{22} x_2 &+ &\dotsb &+ &a^{(1)}_{2n} x_n &= &b^{(1)}_2\\
    \vdots && \vdots &&&& \vdots && \vdots\\
    a^{(1)}_{n1} x_1 &+ &a^{(1)}_{n2} x_2 &+ &\dotsb &+ &a^{(1)}_{nn} x_n &= &b^{(1)}_n\\
\end{matrix}
$$

Eliminujemy zmienną $x_1$ z równań od $2$-go do $n$-tego. Mnożymy $1$-sze równanie przez
$$
l_{i1} = \frac{a^{(1)}_{i1}}{a^{(1)}_{11}},\quad i = 2,\dots,n
$$
i odejmujemy od pozostałych.

Po pierwszym kroku mamy
$$
A^{(2)}x = b^{(2)}
\quad
\begin{matrix}
    a_{11}^{(1)} x_1 &+ & a_{12}^{(1)} x_2 &+ &\dots &+ &a_{1n}^{(1)} x_n &= &b_1^{(1)}\\
    && a_{22}^{(2)} x_1 &+ &\dots &+ &a_{2n}^{(2)} x_n &= &b_2^{(2)}\\
    &&\vdots &&&& \vdots && \vdots\\
    && a_{n2}^{(2)} x_2 &+ &\dots &+ &a_{nn}^{(2)} x_n &= &b_n^{(2)}\\
\end{matrix}
$$

Eliminujemy zmienną $x_2$ z równań od $3$-go do $n$-tego. Mnożymy $2$-gie równanie przez
$$
l_{i2} = \frac{a_{i2}^{(2)}}{2_{22}^{(2)}}, \enspace i = 3,\dots,n
$$
i odejmujemy od pozostałych.

Ogólnie po $k-1$ krokach otrzymujemy
$$
A^{(k)} x = b^{(k)}
\quad
\begin{matrix}
    a_{11}^{(1)} x_1 &+ & a_{12}^{(1)} x_2 &+ &\dots &+ &a_{1n}^{(1)} x_n &= &b_1^{(1)}\\
    && a_{22}^{(2)} x_1 &+ &\dots &+ &a_{2n}^{(2)} x_n &= &b_2^{(2)}\\
    &&& \ddots &&&& \vdots && \vdots\\
    &&&&a_{kk}^{(k)} x_k &+ \dots + &a_{kn}^{(k)} x_n &= &b_k^{(k)}\\
    &&&&\vdots && \vdots && \vdots\\
    &&&& a_{nk}^{(k)} x_2 &+ \dots + &a_{nn}^{(k)} x_n &= &b_n^{(k)}\\
\end{matrix}
$$

Eliminujemy zmienną $x_k$ z równań od $(k+1)$–tego do $n$-tego. Mnożymy $k$-te równanie przez
$$
l_{ik} = \frac{a_{i2}^{(k)}}{a_{kk}^{(k)}}, \enspace i = (k+1),\dots,n
$$
i odejmujemy od pozostałych.

---

Po $n-1$ krokach dostajemy układ z macierzą górno-trójkątną:
$$
A^{(n)} x = b^{(n)}
\quad
\begin{matrix}
    a_{11}^{(1)} x_1 &+ & a_{12}^{(1)} x_2 &+ &\dots &+ &a_{1n}^{(1)} x_n &= &b_1^{(1)}\\
    && a_{22}^{(2)} x_1 &+ &\dots &+ &a_{2n}^{(2)} x_n &= &b_2^{(2)}\\
    &&& \ddots &&& \vdots && \vdots\\
    &&&&&&a_{nn}^{(n)} x_n &= &b_n^{(n)}\\
\end{matrix}
$$

### 1.1. Pseudokod

1. `for` $k \gets 1$ `to` $(n-1)$:
    1. `for` $i \gets (k+1)$ `to` $n$:
        1. $l_{ik} \gets \frac{a_{ik}^{(k)}}{a_{kk}^{(k)}}$
        2. `for` $j \gets (k+1)$ `to` $n$:
            1. $a_{ij}^{(k+1)} \gets a_{ij}^{(k)} - l_{ik} a_{kj}^{(k)}$
        3. $b_i^{(k+1)} \gets b_i^{(k)} - l_{ik} b^{(k)}_k$

### 1.2. Macierzowe sformułowanie jednego kroku

Przejście od macierzy $A^{(k)}$ do $A^{(k+1)}$ i od wektora $b^{(k)}$ do $b^{(k+1)}$ możemy zapisać
$$
A^{(k+1)} = L^{(k)}A^{(k)}, \quad b^{(k+1)} = L^{(k)}b^{(k)},
$$
gdzie
$$
L^{(k)} =
\begin{bmatrix}
    1\\
    & \ddots\\
    &&& 1\\
    &&& -l_{k+1,k} & 1\\
    &&& -l_{k+2,k}\\
    &&& \vdots &&&\ddots\\
    &&& -l_{n,k} &&&& 1
\end{bmatrix}
$$

#### 1.2.1. Kroki

Proces sprowadzania macierzy $A^{(1)}$ do macierzy górno-trójkątnej $A^{(n)}$ w $(n-1)$ krokach możemy zapisać
$$
A^{(n)} = L^{(n-1)} \dots L^{(2)} L^{(1)} A^{(1)}.
$$

Oznaczając $A^{(n)}$ przez $U$ oraz z tego, że $A = A^{(1)}$ mamy
$$
\begin{aligned}
    U &= L^{(n-1)} \dots L^{(2)} L^{(1)} A\\
    A &= \left( L^{(n-1)} \dots L^{(2)} L^{(1)} \right)^{-1} U\\
    A &= L^{(1)^{-1}} L^{(2)^{-1}} \dots L^{(n-1)^{-1}} U
\end{aligned}
$$

#### 1.2.2. Rozkład $LU$

$$
L^{(k)^{-1}}=
\begin{bmatrix}
    1\\
    &\ddots\\
    &&& 1\\
    &&& l_{k+1,k} & 1\\
    &&& l_{k+2,k}\\
    &&& \vdots &&& \ddots\\
    &&& l_{n,k} &&&& 1
\end{bmatrix}
\quad
L =
\begin{bmatrix}
    1\\
    l_{21} & 1\\
    l_{31} & l_{32} & 1\\
    \vdots &&&& \ddots\\
    l_{n1} & l_{n2} & \dotsb & l_{n,n-1} & 1
\end{bmatrix}
$$
gdzie $L = L^{(1)^{-1}} L^{(2)^{-1}} \dots L^{(n-1)^{-1}}$.

Jak widać elminacja Gaussa jest równoważna rozkładowi macierzy $A$ na iloczyn $A = LU$ macierzy dolnej i górno-trójkątnej.

---

## 2. Drugi etap eliminacji Gaussa

Mamy $Ux = B$, gdzie
- $U \in \reals^{n\times n}$
- $x \in \reals^n$
- $b \in \reals^n$

Czyli:
$$
\begin{matrix}
    u_{11} x_1 &+ &u_{12} x_2 &+ &\dotsb &+& u_{1n}x_n &= &b_1\\
    & &u_{22} x_2 &+ &\dotsb &+ u_{2n} x_n &= &b_2\\
    && &\ddots & & \vdots && \vdots\\
    &&&&& u_{nn} &= &b_n
\end{matrix}
$$
*(idziemy od dołu do góry stopniowo, jeden po drugim, wyznaczając kolejne zmienne)*

Zakładamy, że macierz $U$ jest nieosobliwa ($\det(U) \neq 0$) stąd $u_{kk} \neq 0$ dla $k = 1,\dots,n$. Wyznaczamy $x_n$ z ostatniego równania
$$
x_n = \frac{b_n}{u_{nn}}
$$

Dalej wyznaczamy $x_k$ dla $k = (n-1),\dots,1$
$$
x_k = \frac{b_k - \sum_{j = k+1}^n u_{kj} x_j}{u_{kk}}
$$

---
