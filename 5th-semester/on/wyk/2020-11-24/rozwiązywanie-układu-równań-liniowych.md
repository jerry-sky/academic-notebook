---
lang: 'pl'
title: 'Rozwiązywanie układu równań liniowych'
author: 'Jerry Sky'
date: '2020-12-01'
---

---

- [1. Pierwszy etap eliminacji Gaussa](#1-pierwszy-etap-eliminacji-gaussa)
    - [1.1. Pseudokod](#11-pseudokod)
    - [1.2. Macierzowe sformułowanie jednego kroku](#12-macierzowe-sformułowanie-jednego-kroku)
    - [1.3. Kroki](#13-kroki)
    - [1.4. Rozkład $LU$](#14-rozkład-lu)
    - [1.5. Obliczanie wyznacznika](#15-obliczanie-wyznacznika)
    - [1.6. Obliczanie macierzy odwrotnej](#16-obliczanie-macierzy-odwrotnej)
    - [1.7. Wybór elementu głównego](#17-wybór-elementu-głównego)
        - [1.7.1. Przykład](#171-przykład)
        - [1.7.2. Modyfikacja eliminacji Gaussa](#172-modyfikacja-eliminacji-gaussa)
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
    && a_{22}^{(2)} x_2 &+ &\dots &+ &a_{2n}^{(2)} x_n &= &b_2^{(2)}\\
    &&\vdots &&& \vdots && \vdots\\
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
    && a_{22}^{(2)} x_2 &+ &\dots &+ &a_{2n}^{(2)} x_n &= &b_2^{(2)}\\
    &&& \ddots &&& \vdots && \vdots\\
    &&&&a_{kk}^{(k)} x_k &+ \dots + &a_{kn}^{(k)} x_n &= &b_k^{(k)}\\
    &&&&\vdots && \vdots && \vdots\\
    &&&& a_{nk}^{(k)} x_k &+ \dots + &a_{nn}^{(k)} x_n &= &b_n^{(k)}\\
\end{matrix}
$$

Eliminujemy zmienną $x_k$ z równań od $(k+1)$–tego do $n$-tego. Mnożymy $k$-te równanie przez
$$
l_{ik} = \frac{a_{ik}^{(k)}}{a_{kk}^{(k)}}, \enspace i = (k+1),\dots,n
$$
i odejmujemy od pozostałych.

---

Po $n-1$ krokach dostajemy układ z macierzą górno-trójkątną:
$$
A^{(n)} x = b^{(n)}
\quad
\begin{matrix}
    a_{11}^{(1)} x_1 &+ & a_{12}^{(1)} x_2 &+ &\dots &+ &a_{1n}^{(1)} x_n &= &b_1^{(1)}\\
    && a_{22}^{(2)} x_2 &+ &\dots &+ &a_{2n}^{(2)} x_n &= &b_2^{(2)}\\
    &&&& \ddots && \vdots && \vdots\\
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

### 1.3. Kroki

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

### 1.4. Rozkład $LU$

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
    l_{n1} & l_{n2} & \dotsb && l_{n,n-1} & 1
\end{bmatrix}
$$
gdzie $L = L^{(1)^{-1}} L^{(2)^{-1}} \dots L^{(n-1)^{-1}}$.

Jak widać elminacja Gaussa jest równoważna rozkładowi macierzy $A$ na iloczyn $A = LU$ macierzy dolnej i górno-trójkątnej.

W komputerowej realizacji, rozkład $LU$ pamiętamy w jednej tablicy umieszczając mnożniki $l^{(k)}_{ik}$ w miejscu zerowanych elementów $a_{ik}^{(k)}$.
$$
A =
\begin{bmatrix}
    a_{11} & a_{12} & \dotsb & a_{1n}\\
    a_{21} & a_{22} & \dotsb & a_{2n}\\
    \vdots & \vdots & \dotsb & \vdots\\
    a_{n1} & a_{n2} & \dotsb & a_{nn}\\
\end{bmatrix}

\rightarrow

LU =
\begin{bmatrix}
    u_{11} & u_{12} & \dotsb & u_{1n}\\
    l_{21} & u_{22} & \dotsb & u_{2n}\\
    \vdots & \vdots & \dotsb & \vdots\\
    l_{n1} & l_{n2} & \dotsb & u_{nn}\\
\end{bmatrix}
$$

Znając rozkład $A = LU$ zadanie $Ax = b$ sprowadzamy do rozwiązania dwóch układów trójkątnych
$$
Ly = b \qquad Ux = y
$$

Rozwiązanie układu $Ly = b$ odpowiada
$$
y = L^{-1} b = L^{(n-1)} \dotsb L^{(2)} L^{(1)} b = b^{(n)}.
$$

---

### 1.5. Obliczanie wyznacznika

Załóżmy, że znamy rozkład $Uu$ macierzy $A$ wówczas
$$
\det(A) = \det(LU) = \det(L) \cdot \det(U) = \prod_{i=1}^n u_{ii}.
$$

---

### 1.6. Obliczanie macierzy odwrotnej

Z definicji $A^{-1}$ jest macierzą odwrotną do $A$, jeżeli
$$
AA^{-1} = I.
$$

Oznaczając $A^{-1}$ przez $X$ mamy
$$
AX = I \iff A\left[x^{(1)},\dots,x^{(n)}\right] = \left[e^{(1)}, \dots, e^{(n)}\right],\quad x^{(i)}, e^{(i)} \in \mathbb{R}^n
$$
gdzie $x^{(i)}$ jest $i$-tą kolumną macierzy odwrotnej, $e^{(i)}$ jest $i$-tą kolumną macierzy jednostkowej.

Znając rozkład $LU$ macierzy $A$ wyznaczamy $n$ kolumn macierzy $A^{(-1)}$ co jest równoważne rozwiązaniu $2n$ układów trójkątnych
$$
\begin{aligned}
    LU x^{(i)} &= e^{(i)}, \quad i = 1, \dots, n\\
    Ly^{(i)} = e^{(i)}, \enspace Ux^{(i)} &= y^{(i)}, \quad i = 1, \dots, n\\
\end{aligned}
$$

---

### 1.7. Wybór elementu głównego

Wariant podstawowy metody eliminacji Gaussa może być stosowany jeżeli wszystkie elementy przekątniowe $a_{kk}^{(k)}, \enspace k = 1,2,\dots,(n-1)$ są różne od zera. Warunek ten nie jest spełniony nawet dla macierzy nieosobliwych, jak na przykład
$$
\begin{bmatrix}
    0 & 1\\
    1 & 1\\
\end{bmatrix}
\begin{bmatrix}
    x_1\\
    x_2\\
\end{bmatrix}
=
\begin{bmatrix}
    1\\
    2\\
\end{bmatrix}
$$

W takim przypadku wystarczy zamienić równania miejscami. Należy podkreślić, że w numerycznej realizacji ważne jest nie tylko, aby elementy $a^{(k)}_{kk}$ były różne od zera, ale by nie były zbyt małę co do wartości bezwzględnej.

#### 1.7.1. Przykład

Rozważmy układ równań
$$
\begin{bmatrix}
    \epsilon & 1\\
    1 & 1\\
\end{bmatrix}
\begin{bmatrix}
    x_1\\
    x_2\\
\end{bmatrix}
=
\begin{bmatrix}
    1\\
    2\\
\end{bmatrix}
$$
gdzie $\epsilon$ jest małą liczbą.

Po zastosowaniu eliminacji Gaussa otrzymujemy układ trójkątny
$$
\begin{bmatrix}
    \epsilon & 1\\
    0 & 1 - \epsilon^{-1}\\
\end{bmatrix}
\begin{bmatrix}
    x_1\\
    x_2\\
\end{bmatrix}
=
\begin{bmatrix}
    1\\
    2 - \epsilon^{-1}\\
\end{bmatrix}.
$$

Rozwiązując otrzymujemy
$$
x_2 = \frac{2 - \epsilon^{-1}}{1 - \epsilon^{-1}}
\\[10pt]
x_1 = (1 - x_2) \cdot \epsilon^{-1}
$$

Jeżeli $\epsilon$ jest wystarczająca małe np. $\epsilon = 10^{-8}$ w arytmetyce `single`, wówczas $2 - \epsilon^{-1} \approx \epsilon^{-1}$ oraz $1 - \epsilon^{-1} \approx \epsilon^{-1}$.

Stąd obliczone $x_2 \approx 1$ i $x_1 \approx 0$ znacznie różnią się od prawidłowych wartości $x_2 \approx 1$ i $x_1 \approx 1$.

Problem znika jeżeli zamienimy kolejność równań:
$$
\begin{bmatrix}
    1 & 1\\
    \epsilon & 1\\
\end{bmatrix}
\begin{bmatrix}
    x_1\\
    x_2\\
\end{bmatrix}
=
\begin{bmatrix}
    2\\
    1\\
\end{bmatrix}.
$$

Stosując eliminację Gaussa dostajemy układ trójkątny
$$
\begin{bmatrix}
    1 & 1\\
    0 & 1 - \epsilon\\
\end{bmatrix}
\begin{bmatrix}
    x_1\\
    x_2\\
\end{bmatrix}
=
\begin{bmatrix}
    2\\
    1 - 2\epsilon\\
\end{bmatrix}.
$$

Rozwiązując układ otrzymujemy prawidłowe wyniki:
$$
x_2 = \frac{1 - 2\epsilon}{1 - \epsilon} \approx 1,
\\[10pt]
x_1 = 2 - x_2 \approx 1.
$$

---

#### 1.7.2. Modyfikacja eliminacji Gaussa

Rozważmy, $k$-ty krok eliminacji Gaussa.

- eliminacja Gaussa z *częściowym wyborem* polega na znalezieniu elementu takiego, że
    $$
    \left\lvert a_{pk}^{(k)} \right\rvert = \max_{k \le i \le n} \left\lvert a_{ik}^{(k)} \right\rvert
    $$
    i przestawieniu w macierzy $A^{(k)}$ wiersza $p$-tego z $k$-tym oraz elementu $p$-tego z $k$-tym w wektorze $b^{(k)}$.

- eliminacja Gaussa z *pełnym wyborem* polega na znalezieniu elementu takie, że
    $$
    \left\lvert a_{pl}^{(k)} \right\rvert = \max_{k \le i,j \le n} \left\lvert a_{ij}^{(k)} \right\rvert
    $$
    i przestawieniu w macierzy $A^{(k)}$ wiersza $p$-tego z $k$-tym, kolumny $l$-tej z $k$-tą oraz elementu $p$-tego z $k$-tym w wektorze $b^{(k)}$.

Niech $P_{ij}$ będzie macierzą permutacji
$$
P_{ij} =
\begin{bmatrix}
    1\\
    & \ddots\\
    && 0 & \dotsb & 1\\
    && \vdots && \vdots\\
    && 1 & \dotsb & 0\\
    &&&&&\ddots\\
    &&&&&& 1\\
\end{bmatrix}
$$

Czyli $P_{ij}$ różni się od $I$ elementami $p_{ii} = p_{jj} = 0$ oraz $p_{ij} = p_{ji} = 1$.\
Ponadto $P^T_{ij} = P_{ij} = P^{-1}_{ij}, \quad P^2_{ij} = I$.\
$P_{ij} A$ jest równoważne zamianie w macierzy $A$ wiersza $i$-tego z $j$-tym.\
$AP_{ij}$ jest równoważne zamianie w macierzy $A$ kolumny $i$-tej z $j$-tą.

W zapisie macierzowym częściowy wybór ma postać
$$
P_{pk} A^{(k)}, \quad P_{pk} b^{(k)},
$$
natomiast pełny wybór ma postać
$$
P_{pk} A^{(k)} P_{kl}, \quad P_{pk} b^{(k)}.
$$

Zatem, metodę eliminacji Gaussa z pełnym wyborem możemy przedstawić
$$
\begin{aligned}
L^{(n-1)} P_{p_{n-1} n-1} \dots L^{(2)} P_{p_2 2} L^{(1)} P_{p_1 1}A^{(1)} P_{1 j_1} P_{2 j_2} \dots P_{n-1, j_{n-1}} &= A^{(n)}\\
L^{(n-1)} P_{p_{n-1} n-1} \dots L^{(2)} P_{p_2 2} L^{(1)} P_{p_1 1} P^{-1} P A^{(1)} \overline{P} &= A^{(n)}
\end{aligned}
$$
gdzie

- $P = P_{p_{n-1} n-1} \dots P_{p_2 2} P_{p_1 1}$
- $\overline{P} = P_{1 j_1} P_{2 j_2} \dots P_{n-1 j_{n-1}}$

$L = \left( L^{(n-1)} P_{p_{n-1} n-1} \dots L^{(2)} P_{p_2 2} L^{(1)} P_{p_2 2} \dots P_{p_{n-1} n-1} \right)^{-1}$ jest macierzą dolno trójkątną spełniającą równanie
$$
LU = PA\overline{P}
$$
gdzie $U = A^{(n)}$.

W przypadku częściowego wyboru mamy po prostu $\overline{P} = I$.\
Zatem
$$
LU = PA.
$$

Znany rozkład $LU = PA$ możemy wykorzystać do rozwiązania układu równań $Ax = b$
$$
Ly = Pb, \quad Ux = y.
$$

Wyznacznik macierzy obliczamy następująco:
$$
\det(A) = (-1)^p \prod_{i=1}^n u_{ii}
$$
gdzie $p$ jest liczbą przestawień kolumn i wierszy.

---

## 2. Drugi etap eliminacji Gaussa

Mamy $Ux = b$, gdzie

- $U \in \reals^{n\times n}$
- $x \in \reals^n$
- $b \in \reals^n$

Czyli:
$$
\begin{matrix}
    u_{11} x_1 &+ &u_{12} x_2 &+ &\dotsb &+ u_{1n}x_n &= &b_1\\
    & &u_{22} x_2 &+ &\dotsb &+ u_{2n} x_n &= &b_2\\
    && &\ddots & & \vdots && \vdots\\
    &&&&& u_{nn} x_n &= &b_n
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
