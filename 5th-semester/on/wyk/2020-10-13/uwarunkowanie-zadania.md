---
lang: 'pl'
title: 'Uwarunkowanie zadania'
author: 'Jerry Sky'
date: '2020-10-13'
---

---

- [1. DEF: Złe uwarunkowanie zadania](#1-def-złe-uwarunkowanie-zadania)
- [2. Przykład (obliczanie wartości funkcji)](#2-przykład-obliczanie-wartości-funkcji)
- [3. DEF: Wskaźniki uwarunkowania](#3-def-wskaźniki-uwarunkowania)
- [4. Przykład (iloczyn skalarny)](#4-przykład-iloczyn-skalarny)
- [5. Normy wektorów](#5-normy-wektorów)
    - [5.1. Definicja](#51-definicja)
        - [5.1.1. Przykład](#511-przykład)
- [6. Normy macierzy](#6-normy-macierzy)
    - [6.1. Definicja](#61-definicja)
    - [6.2. Normy](#62-normy)
        - [6.2.1. Przykład](#621-przykład)
    - [6.3. Przykład ($Ax = b$)](#63-przykład-ax--b)
    - [6.4. Przykład (Macierz Hilberta)](#64-przykład-macierz-hilberta)
    - [6.5. Przykład (Zaburzenia macierzy w zadaniu $Ax = b$)](#65-przykład-zaburzenia-macierzy-w-zadaniu-ax--b)
- [7. „Złośliwy wielomian” (Wilkinson)](#7-złośliwy-wielomian-wilkinson)
    - [7.1. Uwarunkowanie zadania $\omega(x) = 0$](#71-uwarunkowanie-zadania-omegax--0)
        - [7.1.1. Wniosek](#711-wniosek)

---

## 1. DEF: Złe uwarunkowanie zadania

*Jeśli niewielkie względne zmiany danych powodują dużę względne odkształcenia wyników, to zadanie nazywamy źle uwarunkowanym.*

---

## 2. Przykład (obliczanie wartości funkcji)

Zbadajmy uwarunkowanie zadania obliczania wartości funkcji $f(x) \neq 0$ w punkcie $x$. W tym celu zaburzymy dane $x$, $\widetilde{x} = x(1 + \delta) = x + x\delta$. Oszacujmy względną zmianę wyniku.

$$
\frac{|f(\widetilde{x}) - f(x)|}{|f(x)|} = \frac{|f(x + x\delta) - f(x)|}{|f(x)|} \approx \frac{|f'(x)\cdot x \delta|}{|f(x)|} = cond(x) |\delta|
$$

$cond(x) = \frac{|f'(x) \cdot x|}{|f(x)|}$ jest wskaźnikiem uwarunkowania zadania.

**Jeśli $\bold{cond(x)}$ jest mały ($\bold{|f'(x)|}$ jest mała), to zadanie jest dobrze uwarunkowane.**

---

## 3. DEF: Wskaźniki uwarunkowania

Wielkości charakteryzujące wpływ zaburzeń danych na odkształcenia wyników nazywamy *wskaźnikami uwarunkowania*.

---

## 4. Przykład (iloczyn skalarny)

Mamy:
- $S(a,b) = \sum_{i=1}^{n} a_i b_i \neq 0$
- $a = (a_1, \dots, a_n)$
- $b = (b_1, \dots, b_n)$

Zaburzamy dane:
- $\widetilde{a} = (a_1(1 + \alpha_1), \dots, a_n(1 + \alpha_n))$
- $\widetilde{b} = (b_1(1 + \beta_1), \dots, b_n(1 + \beta_n))$

Oszacujmy względną zmianę wyniku:

$$
\frac{|S(\widetilde{a}, \widetilde{b}) - S(a,b)|}{|S(a,b)|} = \frac{|\sum_{i=1}^{n} a_i b_i (1 + \alpha_i)(1 + \beta_i) - \sum_{i=1}^{n} a_i b_i|}{|\sum_{i=1}^{n} a_i b_i|}\\
= \frac{|\sum_{i=1}^{n} a_i b_i(1 + \alpha_i + \beta_i + \alpha_i\beta_i) - \sum_{i=1}^{n} a_i b_i|}{|\sum_{i=1}^{n} a_i b_i|} \approx\\
\approx \frac{|\sum_{i=1}^{n} a_i b_i(\alpha_i + \beta_i)|}{|\sum_{i=1}^{n} a_i b_i|}\\
\le \max_{1 \le i \le n} |\alpha_i + \beta_i|\frac{\sum_{i=1}^{n} |a_i b_i|}{|\sum_{i=1}^{n} a_i b_i|} = cond(a,b) \cdot \max_{1 \le i \le n}|\alpha_i + \beta_i|
$$

Jeśli $a_i, b_i$, $i = 1, \dots, n$ są tego samego znaku, wówczas
$cond(a,b) = 1$ i zadanie jest dobrze uwarunkowane.

---

## 5. Normy wektorów

### 5.1. Definicja

Normą w $\mathbb{R}^n$ nazywamy funkcję rzeczywistą o własnościach:
- $||x|| \ge 0$, $||x|| = 0 \Leftrightarrow x = 0$
- $||\alpha x|| = |\alpha|||x||$, $\alpha \in \mathbb{R},~ x \in \mathbb{R}^n$
- $||x + y|| \le ||x|| + ||y||$, $x,y \in \mathbb{R}^n$

#### 5.1.1. Przykład

Mamy $x = (x_1, \dots, x_n)$.

- Norma sumacyjna: $||x||_1 = \sum_{i=1}^{n} |x_i|$
- Norma euklidesowa: $||x||_2 = \sqrt{\sum_{i=1}^{n} x_i^2}$
- Norma maksymalna: $||x||_\infty = \max_{1\le i \le n}|x_i|$
- (*Julia lang*) `norm(A, p::Real=2)` z pakietu `LinearAlgebra`

---

## 6. Normy macierzy

### 6.1. Definicja

Normą w $\mathbb{R}^{m\times n}$ nazywamy funkcję rzeczywistą o własnościach:
- $||A|| \ge 0$, $||A|| = 0 \Leftrightarrow A = 0$
- $||\alpha A|| = |\alpha|||A||$, $\alpha \in \mathbb{R}, A \in \mathbb{R}^{m\times n}$
- $||A + B|| \le ||A|| + ||B||$, $A,B \in \mathbb{R}^{m\times n}$

### 6.2. Normy

Ważną podklasę norm macierzy stanowią normy macierzy *indukowane* przez normy wektorów definiowane jako
$$
||A|| = \sup\{ ||Ax||: x \in \mathbb{R}^n,~ ||x|| = 1 \}
$$

Z powyższego wynika następująca nierówność
$$
||Ax|| \le ||A||~ ||x||
$$

#### 6.2.1. Przykład

Mamy $A \in \mathbb{R}^{m\times n}$.

- $||A||_1 = \max_{1 \le j \le n} \sum_{i=1}^{m} |a_{ij}|$
- Norma spektralna: $||A||-2 = \sqrt{\lambda_{\max} (A^T A)}$, gdzie $\lambda_{\max}$ jest maksymalną wartością własną macierzy $A^T A$.
- $||A||_\infty = \max_{1\le i \le m} \sum_{j=1}^{n} |a_{ij}|$
- (*Julia lang*) `norm(A, p::Real=2)` z pakietu `LinearAlgebra`

---

### 6.3. Przykład ($Ax = b$)

Zbadajmy uwarunkowanie zadania rozwiązywania układu równań liniowych
$$
Ax = b
$$

o danej nieosobliwej macierzy $A~ (n\times n)$ i o niezerowym wektorze $b$.

Zaburzymy wektor $b$ otrzymując $\tilde{b} = (b_1 (1+\delta_1), \dots, b_n(1 + \delta_n))$. Jeśli $x$ oraz  $\tilde{x}$ spełniają $Ax = b$ oraz $A\tilde{x} = \tilde{b}$, to oszacujmy względną zmianę wyniku.

$$
||x - \tilde{x}|| = ||A^{-1}b - A^{-1}\tilde{b}|| = ||A^{-1}(b - \tilde{b})|| \le ||A^{-1}||~ ||b - \tilde{b}|| =\\
||A^{-1}||~||b||~\frac{||b - \tilde{b}||}{||b||} = ||A^{-1}||~||Ax|| \frac{||b-\tilde{b}}{||b||} \le ||A^{-1}||~||x||\frac{||b - \tilde{b}||}{||b||}
$$

$$
\frac{||x - \tilde{x}}{||x||} \le \bold{||A^{-1}||~||A||} \frac{||b - \tilde{b}||}{||b||} = cond(A) \frac{||b - \tilde{b}||}{||b||}
$$

Oczywiście $cond(A)$ to wskaźnik uwarunkowania macierzy.

W *Julia lang* mamy `cond(M, p::Real=2)` z pakietu `LinearAlgebra`.

---

### 6.4. Przykład (Macierz Hilberta)

Przykładem macierzy bardzo źle uwarunkowanej jest macierz Hilberta $H_n = \left[\frac{1}{i + j - 1}\right]_{i,j=1}^{n}$.

Wskaźniki $cond(H_6) \approx 1.5 \cdot 10^7$, $cond(H_{10}) \approx 1.6 \cdot 10^{13}$.

---

### 6.5. Przykład (Zaburzenia macierzy w zadaniu $Ax = b$)

Rozważmy teraz uwarunkowanie zadania $Ax = b$ ze względu na zaburzenia macierzy układu $\tilde{A} = A + \delta A$. Oszacujmy względną zmianę wyniku. Oszacowanie podamy bez dowodu.

Jeśli $||A||~||\delta A|| < 1$ oraz $||l|| = 1$, to
$$
\frac{||x - \tilde{x}||}{||x||} \le \frac{||A^{-1}||~||A||\frac{||A - \tilde{A}||}{||A||}}{1 - ||A^{-1}||~||A||\frac{||A-\tilde{A}||}{||A||}} = \frac{cond(A)\frac{||A-\tilde{A}||}{||A||}}{1 - cond(A)\frac{||A-\tilde{A}||}{||A||}}.
$$

---

## 7. „Złośliwy wielomian” (Wilkinson)

Dany jest wielomian
$$
\omega(x) = \prod{i=1}^{20}(x_i - i) = x^{20} + a_{19}x^{19} + \dotsb + a_1x + a_0
$$
gdzie $a_{19} = -210$. Zaburzymy teraz $a_{19}$.

$$
\omega_\epsilon(x) = \omega(x) - \epsilon x^{19} = x^{20} - (210 + \epsilon)x^{19} + \dotsb + a_1 x + a_0
$$
gdzie $\epsilon = 2^{-23}$.

$$
a_{19}(\epsilon) = -210 - \epsilon = a_{19}\left( 1 + \frac{1}{2^{23}\cdot 210} \right) = a_{19}(1+\delta)
$$
względne zaburzenie $\delta < 2^{-30}$.

Dla tak niewielkiego względnego zaburzenia $a_{19}$ wielomian $\omega_\epsilon(x)$ ma zera zespolone.

---

### 7.1. Uwarunkowanie zadania $\omega(x) = 0$

Załóżmy, że $\omega'(r) \neq 0$, gdzie $r$ jest pierwiastkiem $\omega$, tj. $\omega(r) = 0$.

Zaburzymy $\omega$:
$$
\tilde{\omega} = \omega - \epsilon z
$$
gdzie $z \in C^2$.

Pytanie: *Jaki jest pierwiastek $\tilde{\omega}$, tj. $r + h$ taki, że $\tilde{\omega}(r+h) = 0$?*

Rozwijamy $\tilde{\omega}$ w szereg Taylora:
$$
\omega(r) + h\omega'(r) + \frac{1}{2}h^2\omega''(\eta) - \epsilon\left( z(r) + hz'(r) + \frac{1}{2}h^2z''(\xi) \right) = 0.
$$
Stąd
$$
h = \approx \epsilon\frac{z(r)}{\omega'(r) - \epsilon z'(r)} \approx \epsilon\frac{z(r)}{\omega'(r)}.
$$

$$
\omega(x) = \prod_{i=1}^{20} (x_i - i)
$$

Zaburzenie $z(x) = \epsilon x^{19}$, $\epsilon = 2^{-23}$.

Pytanie: *jak powyższe zaburzenie wpływa na pierwiastek $r = 20$?*
$$
h \approx \epsilon\frac{z(20)}{\omega'(20)} \approx \epsilon \frac{20^{19}}{19!} \approx \epsilon10^8 \approx 102.76
$$

#### 7.1.1. Wniosek
Zadanie wyznaczania pierwiastków wielomianu jest źle uwarunkowane ze względu na zaburzenia współczynników.

---
