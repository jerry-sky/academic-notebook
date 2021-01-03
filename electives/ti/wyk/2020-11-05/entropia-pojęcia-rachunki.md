---
lang: 'pl'
title: 'Entropia: trochę pojęć i rachunków'
author: 'Jerry Sky'
date: 2020-11-05
---

---

- [1. Zmienna losowa](#1-zmienna-losowa)
- [2. DEF: Entropia łączna](#2-def-entropia-łączna)
- [3. Przykład](#3-przykład)
- [4. Twierdzenie#1](#4-twierdzenie1)
    - [4.1. D-d](#41-d-d)
- [5. DEF: Informacja wzajemna zmiennych losowych](#5-def-informacja-wzajemna-zmiennych-losowych)
    - [5.1. Fakt#1 (oczywisty)](#51-fakt1-oczywisty)
    - [5.2. Fakt#2 (oczywisty)](#52-fakt2-oczywisty)
    - [5.3. Równoważnie](#53-równoważnie)
- [6. Odległość Kullbacha-Leiblera](#6-odległość-kullbacha-leiblera)
- [7. DEF: Entropia warunkowa](#7-def-entropia-warunkowa)
- [8. Fakt#3](#8-fakt3)
    - [8.1. D-d](#81-d-d)

---

## 1. Zmienna losowa

*Myślimy tu o entropii zmiennej losowej.*

$$
X: \Omega \to \mathcal{X} \quad (\text{u nas } \mathcal{X} \text{ jest skończona})
$$

Zamiast $P(X = x), \enspace x \in \mathcal{X}$ będziemy pisać $p(x)$.

$$
H(X) = \sum_{x \in \mathcal{X}} p(x) \log \frac{1}{p(x)}.
$$

---

## 2. DEF: Entropia łączna

Mamy zmienne losowe:

$$
X: \Omega \to \mathcal{X}, \enspace Y: \Omega \to \mathcal{Y}.
$$

Przez entropię łączną rozumiemy

$$
H(X,Y) = \sum_{x \in \mathcal{X}} \sum_{y \in \mathcal{Y}} p(x,y) \log \frac{1}{p(x,y)}
$$

gdzie

$$
p(x,y) = P(X = x, Y = y) = P(X = x \land Y = y).
$$

Można myśleć o tym jak o zmiennej losowej

$$
T: \Omega \to \mathcal{X} \times \mathcal{Y}
\\[10pt]
T(\omega) = \left( X(\omega), Y(\omega) \right)
\\[10pt]
H(X,Y) = H(T)
$$

Umawiamy się, że $0 \cdot \log \frac{1}{0} = 0$.

---

## 3. Przykład

Załóżmy, że $X$ i $Y$ są niezależne, czyli

$$
P(X = x, Y = y) = P(X = x) \cdot P(Y = y), \quad p(x,y) = p(x) \cdot p(y),
$$

wówczas

$$
H(X,Y) = \sum_{x,y} p(x,y) \log \frac{1}{p(x,y)} = \sum_{x,y} p(x) p(y) \frac{1}{p(x) p(y)} =\\
=\sum_{x,y} p(x) p(y) \left( \log \frac{1}{p(x)} + \log \frac{1}{p(y)} \right) =\\
= \sum_{x,y} p(x) p(y) \log \frac{1}{p(x)} + \sum_{x,y} p(x) p(y) \log\frac{1}{p(y)} =\\
= \left( \sum_y p(y) \right) \left( \sum_x p(x) \log \frac{1}{p(x)} \right) + \left( \sum_x p(x) \right) \left( \sum_y p(y) \log \frac{1}{p(y)} \right) =\\
= H(X) + H(Y).
$$

---

## 4. Twierdzenie#1

$$
H(X,Y) \le H(X) + H(Y)
$$

Ponadto mamy tutaj równość, wtedy i tylko wtedy gdy zmienne losowe są niezależne.

### 4.1. D-d

$$
H(X,Y) = \sum_{x,y} p(x,y) \log\frac{1}{p(x,y)}
$$

[Wcześniej wyrachowaliśmy](#3-przykład), że

$$
H(X) + H(Y) = \sum_{x,y} p(x) p(y) \log \frac{1}{p(x) p(y)} =\\
= \sum_x p(x) \log \frac{1}{p(x)} + \sum_{y} p(y) \log\frac{1}{p(y)} =\\
= \sum_{x,y} p(x,y) \log\frac{1}{p(x)} + \sum_{x,y} p(x,y) \log \frac{1}{p(y)} = (*)
$$

Tutaj korzystamy z naturalnego faktu, że

$$
p(x) = \sum_y p(x,y).
$$

Dalej:

$$
\sum_{x,y} p(x,y) \left( \log \frac{1}{p(x)} + \log \frac{1}{p(y)} \right) =
\\[10pt]
\sum_{x,y}p(x,y) \log \frac{1}{p(x) p(y)}
$$

Mamy też:

$$
\sum_{x,y} p(x,y) = 1
\\[10pt]
\sum_{x,y} p(x) p(y) = 1
$$

Z [twierdzenia](../2020-10-29/kody-huffmana.md#6-twierdzenie-o-kodach-huffmana) (o $p_N, q_N, \dots$) mamy $H(X,Y) \le H(X) + H(Y)$.

$\square$

---

Ponadto

$$
H(X,Y) = H(X) + H(Y)
$$

wtedy i tylko wtedy, gdy $(p_N = q_N)$:

$$
p(x,y) = p(x) p(y)
$$

co oznacza, że zmienne $X$ i $Y$ są niezależne.

$\square$

---

## 5. DEF: Informacja wzajemna zmiennych losowych

Informacją wzajemną zmiennych $X,Y$ nazywamy

$$
I(X,Y) = H(X) + H(Y) - H(X,Y).
$$

### 5.1. Fakt#1 (oczywisty)

$$
I(X,Y) = 0 \iff X,Y \text{ są niezależne}
$$

### 5.2. Fakt#2 (oczywisty)

$$
I(X,Y) \ge 0.
$$

---

### 5.3. Równoważnie

$$
I(X,Y) = \sum_{x,y} p(x,y) \log \frac{1}{p(x) p(y)} + \sum_{x,y} p(x,y) \log \frac{1}{p(x,y)} =\\
= \sum_{x,y} p(x,y) \log \frac{p(x,y)}{p(x) p(y)}
$$

---

## 6. Odległość Kullbacha-Leiblera

$$
D(p || q) = \sum_{a \in A} p(a) \log \frac{p(a)}{q(a)}
$$

gdzie $A$ to skończona przestrzeń probabilistyczna.

$$
(A, p), \enspace (A, q), \enspace \mathcal{F} = \mathcal{P}(A)
$$

W [$I(X,Y)$](#5-def-informacja-wzajemna-zmiennych-losowych) mamy dwie funkcje prawdopodobieństw na zbiorze $\mathcal{X} \times \mathcal{Y}$:

$$
\begin{aligned}
    {p_1(\{(x,y)\})} = p_1(x,y) &= p(x,y)\\
    p_2(x,y) &= p(x) p(y)
\end{aligned}
$$

Mamy $D(p || q) \ge 0$ oraz $D(p || q) = 0 \iff p = q$.

*Czy funkcja $D( \cdot || \cdot )$ ma coś jeszcze wspólnego z metryką?*

---

## 7. DEF: Entropia warunkowa

Entropię warunkową $X$ od $Y$ definiujemy przez

$$
H(X | Y) = \sum_{y \in \mathcal{Y}} p(y) H(X | y),
$$

gdzie
$$
H(X | y) = \sum_{x \in \mathcal{X}} p(x | y) \log \frac{1}{p(x | y)}
$$

Równoważnie:

$$
H(X | Y) = \sum_{x,y} p(y) p(x | y) \log \frac{1}{p(x | y)} =\\
= \sum_{x,y} p(x,y) \log \frac{1}{p(x | y)},
$$

bo warto pamiętać, że:

- $p(x | y) = P(X = x | Y = y)$,
- $p(y) \cdot p(x | y) = p(y) \cdot \frac{p(x,y)}{p(y)}$.

---

## 8. Fakt#3

$$
H(X,Y) = H(X | Y) + H(Y).
$$

### 8.1. D-d

$$
H(X | Y) + H(Y) = \sum_{x,y} p(x,y) \log \frac{1}{p(x | y)} + \sum_{x,y} p(x,y) \log \frac{1}{p(y)} =\\
\sum_{x,y} p(x,y) \log \frac{1}{p(x | y) \cdot p(y)}
$$

---
