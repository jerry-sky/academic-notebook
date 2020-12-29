---
lang: 'pl'
title: 'Działania arytmetyczne w arytmetyce *fl*'
author: 'Jerry Sky'
date: '2020-10-06'
---

---
- [2. Oznaczenia działań](#2-oznaczenia-działań)
- [3. Przykład](#3-przykład)
    - [3.1. Błędy](#31-błędy)
- [4. Przykład (dodawanie kiedy $x \gg y$)](#4-przykład-dodawanie-kiedy-x-gg-y)
- [5. Warunek na błędy](#5-warunek-na-błędy)
- [6. Przykład (narastający błąd po $3$ działaniach)](#6-przykład-narastający-błąd-po-3-działaniach)
- [7. Twierdzenie#1](#7-twierdzenie1)
    - [7.1. D-d](#71-d-d)
- [8. Przykład (narastający błąd po $n$ działaniach)](#8-przykład-narastający-błąd-po-n-działaniach)
- [9. Redukcja cyfr znaczących](#9-redukcja-cyfr-znaczących)
    - [9.1. Przykład](#91-przykład)
    - [9.2. Przykład](#92-przykład)
- [10. Twierdzenie#2](#10-twierdzenie2)
    - [10.1. D-d](#101-d-d)

---

## 1. Reprezentacja liczb w *fl*

[notatka «Numeryczna reprezentacja liczb»](numeryczna-reprezentacja-liczb.md#2-arytmetyka-zmiennopozycyjna-fl)

---

## 2. Oznaczenia działań

Niech
- $x = rd(x)$
- $y = rd(y)$

będą liczbami w arytmetyce *fl*, wówczas przez
$$
fl(x * y) = fl(x \circledast y)
$$
oznaczamy wynik działania $x * y$, gdzie $* \in \{+, -, /, \cdot\}$, w arytmetyce *fl*.

---

## 3. Przykład

Mamy
- $\beta = 10$
- $t = 5$
- $x = rd(x) = 0.31426 \cdot 10^3$
- $y = rd(y) = 0.92577 \cdot 10^5$

**Używamy akumulatora o podwójnej długości do pośrednich obliczeń.**

$$
x + y \overset{\text{po wyrównaniu cech}}{=} 0.9289126000 \cdot 10^5\\ \xrightarrow{\text{zaokrągl.}} fl(x + y) = 0.92891 \cdot 10^5
$$
$$
x - y \overset{\text{po wyrównaniu cech}}{=} -0.9226274000 \cdot 10^5\\ \xrightarrow{\text{zaokrągl.}} fl(x-y) = -0.92263 \cdot 10^5
$$
$$
x \cdot y = 0.2909334802 \cdot 10^8 \xrightarrow{\text{zaokrągl.}} fl(x \cdot y) = 0.29093 \cdot 10^8
$$
$$
\frac{x}{y} \approx 0.3394579647 \cdot 10^{-2} \xrightarrow{\text{zaokrągl.}} fl\left(\frac{x}{y}\right) = 0.33946 \cdot 10^{-2}
$$

### 3.1. Błędy

Błędy względne:
- $|\delta_+| \approx 2.8 \cdot 10^{-6}$
- $|\delta_-| \approx 2.8 \cdot 10^{-6}$
- $|\delta_{\cdot}| \approx 8.5 \cdot 10^{-6}$
- $|\delta_{/}| \approx 6 \cdot 10^{-6}$

Precyzja arytmetyki:\
$\epsilon = 5 \cdot 10^{-5}$

---

## 4. Przykład (dodawanie kiedy $x \gg y$)

Niech
- $x = rd(x) = m_x \beta^{c_x}$
- $y = rd(y) = m_y \beta^{c_y}$
- $x \ge y > 0$ (dla uproszczenia)

Wówczas:
$$
x + y = m_x\beta^{c_x} + m_y \beta^{c_y} = (m_x + m_y\beta^{-(c_x - c_y)}) \beta^{c_x} = m_s \beta^{c_x}
$$

![schemat liczb $x \gg y$](3.x-znacznie-większe-od-y-schemat.png)

Z powyższego rysunku wynika, że dla $x \gg y$\
mamy $fl(x+y) = x$.

---

## 5. Warunek na błędy

Arytmetyka *fl* powinna zapewnić równość
$$
fl(x * y) = rd(x*y)
$$
dla $* \in \{+, -, /, \cdot\}$ oraz $x * y \in [-\mathrm{MAX};~ \mathrm{MAX}]$.

Jeśli powyższe jest prawdziwe, to zachodzi równość
$$
fl(x * y) = (x*y)(1 + \delta)
$$
gdzie $|\delta| \le \epsilon$, $\epsilon = 0.5\beta^{1-t}$

---

## 6. Przykład (narastający błąd po $3$ działaniach)

Obliczymy $x(y + z)$ w *fl*. ($x = rd(x)$, $y = rd(y)$, $z = rd(z)$)

$fl(x(y+z)) = fl(x \cdot fl(y+z)) = [x \cdot fl(y+z)](1 + \delta_1) = [x(y+z)(1 + \delta_2)](1 + \delta_1) = x(y+z)(1 + \delta_2 + \delta_1 + \delta_2\delta_1) \approx x(y+z)(1+ \delta_2 + \delta_1) = x(y+z)(1+\delta_3)$

gdzie $|\delta_i| \le \epsilon,~ i = 1,2$, za to $|\delta_3| \le 2\epsilon$

---

## 7. Twierdzenie#1
Jeśli $\forall i = 1,\dots,n \enspace |\delta_i| \le \epsilon$ oraz $\prod_{i=1}^n(1 + \delta_i) = 1 + E_n$ oraz $n_\epsilon < 2$, wówczas
$$
|E_n| < \frac{n \epsilon}{1 - 0.5n\epsilon} \approx n\epsilon
$$

### 7.1. D-d

$$
\begin{aligned}
|E_n| &= \left|\prod_{i=1}^{n} (1 + \delta_i) - 1\right| \le (1 + \epsilon)^n - 1\\
&= 1 + \binom{n}{1}\epsilon + \binom{n}{2}\epsilon^2 + \binom{n}{3}\epsilon^3 + \dotsb + \binom{n}{n}\epsilon^n - 1\\
&= n\epsilon + \frac{n\epsilon(n-1)\epsilon}{2!} + \frac{n\epsilon(n-1)\epsilon(n-2)\epsilon}{3!} + \dotsb + \frac{n\epsilon(n-1)\epsilon\dotsb1\epsilon}{n!}\\
&= n\epsilon\left( 1 + \frac{(n-1) \epsilon}{2!} + \frac{(n-1)\epsilon(n-2)\epsilon}{3!} + \dotsb +\frac{(n-1) \epsilon \dotsb 1 \epsilon}{n!} \right)\\
&\qquad q = \frac{n\epsilon}{2} < 1\\
|E_n| &< n\epsilon(1 + q + q^2 + \dotsb + q^{n-1}) = n\epsilon \frac{1 - q^n}{1 - q} < \frac{n\epsilon}{1 - 0.5n\epsilon} \approx n\epsilon \quad \blacksquare
\end{aligned}
$$

---

## 8. Przykład (narastający błąd po $n$ działaniach)

Mamy:
- $x_i > 0$, $i = 0,\dots, n$

Obliczyć:
- $S = \sum_{i=0}^n x_i$

Algorytm:
1. $S_0 = x_0$
2. `for` $i := 1$ `to` $n$ `do`:
    1. $S_i := S_{i-1} + x_i$
3. `end for`

---

$$
\begin{aligned}
fl(S) &= fl(\dots fl(fl(fl(x_0 + x_1) + x_2) + x_3) + \dotsb + x_n)\\
&= (\dots (((x_0 + x_1)(1 + \delta_1) + x_2)(1 + \delta_2) +\\
&+ x_3)(1 + \delta_3) + \dotsb + x_n)(1 + \delta_n)\\
&= x_0 \prod_{i=1}^{n}(1 + \delta_i) + x_1\prod_{i=1}^{n}(1 + \delta_i)+\\
&+ x_2\prod_{i=2}^{n}(1+\delta_i) + x_3\prod_{i=3}^{n}(1+\delta_i) + \dotsb + x_n (1+\delta_n)
\end{aligned}
$$
przy czym $|\delta_i| \le \epsilon,~ i = 1,\dots, n$.

Podstawmy $\prod_{i=k}^{n}(1 + \delta_i) = 1+E_k$:
$$
\begin{aligned}
fl(S) &= x_0 + x_0E_1 + x_1 + x_1E_1 + x_2 + x_2E_2 + x_3 + x_3E_3 + \dotsb + x_n + x_nE_n\\
&= S + x_0E_1 + x_1E_1 + x_2E_2 + x_3E_3 + \dotsb + x_nE_n\\
&\le S + (x_0 + x_1 + x_2 + x_3 + \dotsb + x_n)\max_{1 \le k \le n} E_k = S(1 + E_1)
\end{aligned}
$$
gdzie $|E_1| < n\epsilon$ z [«Twierdzenie#1»](#7-twierdzenie1).

---

## 9. Redukcja cyfr znaczących

Przeanalizujmy zjawisko redukcji cyfr znaczących:
- $rd(x) = x(1 + \delta_x)$
- $rd(y) = y(1 + \delta_y)$

$$
\frac{|x - y - [rd(x) - rd(y)]|}{|x - y|} = \frac{|\delta_x x - \delta_y y|}{|x - y|} \le \epsilon\frac{|x| + |y|}{|x - y|}
$$

Z powyższego oszacowania wynika, że niedokładność danych może przenieść się na wynik z wielkim mnożnikiem $\frac{|x| + |y|}{|x - y|}$ nawet gdy samo działanie nie wprowadza błędu.

### 9.1. Przykład

Niech
- $x = 0.3721478693$
- $y = 0.3720230572$

($x \approx y$)

Różnica dokładna to $x - y = 0.0001248121$.

Policzymy $x - y$ w arytmetyce *fl*.
- $t = 5$
- $rd(x) = 0.37215$
- $rd(y) = 0.37202$
- $fl(rd(x) - rd(y)) = 0.00013$

Zauważmy, że tutaj mamy $fl(rd(x) - rd(y)) = rd(x) - rd(y)$.

$|\delta| = \frac{|x - y - [rd(x) - rd(y)]|}{|x - y|} = \frac{|0.0001248121 - 0.00013}{|0.0001248121|} \approx 4.16 \cdot 10^{-2}$.

Precyzja arytmetyki $\epsilon = 5 \cdot 10^{-5}$.

---

### 9.2. Przykład

Gdy liczymy wartość wyrażenia $\sqrt{x^2 + 1} - 1$ kiedy $\bold{|x|}$ **jest mała**.\
W tym przypadku następuje redukcja cyfr znaczących.

Przekształćmy $\sqrt{x^2 + 1} - 1$:
$$
y = (\sqrt{x^2 + 1 } - 1) \frac{\sqrt{x^2 + 1} + 1}{\sqrt{x^2 + 1} + 1} = \frac{x^2}{\sqrt{x^2 + 1} + 1}.
$$

---

## 10. Twierdzenie#2

*Ile cyfr znaczących tracimy przy odejmowaniu $x - y$, kiedy $x \approx y$?*

Jeśli $x$ i $y$ są dodatnimi liczbami w dwójkowej arytmetyce *fl* takimi, że $x > y$ oraz $2^{-q} \le 1 - \frac{y}{x} \le 2^{-p}$, wówczas\
tracimy co najmniej $p$ i co najwyżej $q$ bitów przy odejmowaniu.

### 10.1. D-d

Niech $x$ oraz $y$ będą dwiema liczbami w dwójkowej arytmetyce *fl*, czyli $x = m_x 2^{c_x},~ y = m_y 2^{c_y},$; $m_x, m_y \in \left[\frac{1}{2};~ 1\right)$.

Ponieważ $x > y$, to aby obliczyć różnicę $r = x-y$ musimy wyrównać cechy:
$$
r = m_x 2^{c_x} - m_y 2^{c_y} = (m_x - m_y 2^{c_y - c_x})\cdot 2^{c_x} = m_r 2^{c_x}
$$

Mantysa $m_r$ spełnia
$$
m_r = (m_x - m_y 2^{c_y - c_x}) = m_x \left( 1 - \frac{m_y 2^{c_y}}{m_x 2^{c_x}} \right) = m_x\left( 1 - \frac{y}{x} \right) < 2^{-p}.
$$

Aby znormalizować reprezentację $x - y$ w arytmetyce *fl*, musimy przesunąć mantysę $m_r$ o co najmniej $p$ bitów w lewo. Wówczas wprowadzone są zera (na prawo), które nie niosą żadnej informacji. Co oznacza redukcję $p$ znaczących bitów.

Rozumowanie dla drugiej części jest podobne.

---
