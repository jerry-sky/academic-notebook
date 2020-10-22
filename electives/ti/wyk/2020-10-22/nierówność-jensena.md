# Nierówność Jensen’a

*(2020-10-22)*

- [1. Twierdzenie: Nierówność Jensen’a](#1-twierdzenie-nierówność-jensena)
    - [1.1. D-d](#11-d-d)
        - [1.1.1. Ćwiczenie](#111-ćwiczenie)
- [2. Przykład](#2-przykład)
    - [2.1. Uwaga](#21-uwaga)
    - [2.2. Uwaga](#22-uwaga)
- [3. Twierdzenie#2](#3-twierdzenie2)
    - [3.1. D-d](#31-d-d)
        - [3.1.1. Uwaga](#311-uwaga)
    - [3.2. Wniosek (*frukt z twierdzenia*)](#32-wniosek-frukt-z-twierdzenia)
        - [3.2.1. Ćwiczenie (było podobne)](#321-ćwiczenie-było-podobne)

---

## 1. Twierdzenie: Nierówność Jensen’a
Niech $f: [a;b] \to \mathbb{R}$ wypukła.

Załóżmy, że $x_0, x_1, \dots, x_n \in [a;b]$ oraz $p_0, p_1, \dots, p_n \ge 0 \quad \sum_{i=1}^{n} p_i = 1$.

Wówczas
$$
f\left(\sum_{i=0}^n p_ix_i\right) \ge \sum_{i=0}^n p_i f(x_i).
$$

\[ Jeśli dodatkowo $f$ jest ściśle wypukła oraz $|\{ x_0, x_1, \dots, x_n \}| \ge 2$ i $\forall i \enspace p_i > 0$, \
to nierówność jest ostra. \]

### 1.1. D-d
(przez indukcję względem $n$)

1. $n = 0$ jest OK
2. $n = 1$ (z [DEF wypukłości](przypomnienie-funkcja-wypukła.md#1-def-funkcja-wypukła))
3. $n \implies n+1$:
    1. ustalmy $x_0, x_1, \dots, x_{n+1} \in [a;b]$ oraz $p_0, p_1, \dots, p_{n+1} \ge 0 \quad \sum_{i=0}^{n+1} p_i = 1$
    2. $\sum_{i=0}^{n+1} p_i f(x_i) = \sum_{i=0}^{n} p_i f(x_i) + p_{n+1} f(x_{n+1}) = (p_0 + p_1 + \dotsb + p_n) \sum_{i=0}^{n} \frac{p_i}{p_0 + \dotsb p_n} f(x_i) + p_{n+1} f(x_{n+1}) = (*)$
    3. z zał. ind. możemy postawić „$\ge$” ($q_i = \frac{p_i}{p_0 + \dotsb p_n} \sum_{i=0}^n q_i = 1$)
    4. $(*) \ge (p_0 + \dotsb p_n) f\left( \sum_{i=0}^n \frac{p_i x_i}{p_0 + \dotsb + p_n} \right) + p_{n+1} f(x_{n+1}) = (**)$
    5. z wypukłości możemy postawić „$\ge$” ($q_0 = p_0 + \dotsb p_n \qquad q_1 = p_{n+1}$)
    6. $(**) \ge f\left( (p_0 + \dotsb p_n) \sum_{i=0}^{n} \frac{p_i x_i}{p_0 + \dotsb p_n + p_{n+1} x_{n+1}} \right) = f\left( \sum_{i=0}^{n+1} p_i x_i \right)$

$\blacksquare$

#### 1.1.1. Ćwiczenie
Ostrość!\
Załóż, że $x_0 < x_1 < \dots < x_n$ oraz $p_i > 0$.

---

## 2. Przykład

$f(x) = x \log_2 x$

- $f'(x) = \log_2 x + x\cdot\frac{1}{x} \frac{1}{\ln(2)} = \log_2 x + \frac{1}{\ln(2)}$
- $f''(x) = \frac{1}{x} \frac{1}{\ln(2)} > 0$

($f$ jest ściśle wypukła)

### 2.1. Uwaga
$f: (0;\infty) \to \mathbb{R}$\
czasami wygodnie jest przyjąć $f: [0; \infty) \to \mathbb{R}$ kładąc $f(0) = 0$. (Dlaczego?)

### 2.2. Uwaga
Nierówność Jensen’a w zastosowaniach probabilistycznych przyjmuje postać $\operatorname{E}(f(x)) \ge f(\operatorname{E}X)$. (Dlaczego?)

---

## 3. Twierdzenie#2
Niech $x_0, x_1, \dots, x_n > 0, \quad y_0, y_1, \dots, y_n > 0$ przy czym $\sum_{i=0}^n x_i = \sum_{i=0}^n y_i = 1$.\
Wówczas
$$
\sum_{i=0}^n x_i \log_2 \frac{1}{x_i} \le \sum_{i=0}^n x_i \log_2 \frac{1}{y_i}.
$$

### 3.1. D-d

$$
\sum_{i=0}^n \log_2 \frac{1}{y_i} - \sum_{i=0}^n x_i \log_2 \frac{1}{x_i} = \sum_{i=0}^n x_i \left( \log_2 \frac{1}{y_i} + \log x_i \right) =\\
= \sum_{i=0}^n y_i \cdot \frac{x_i}{y_i} \log_2 \frac{x_i}{y_i} = (*)
$$
z [nierówności Jensen’a](#1-twierdzenie-nierówność-jensena) dla
- $p_i = y_i$
- $t_i = \frac{x_i}{y_i}$
- $f(t) = t\log t$

mamy dalej:
$$
(*) \ge f\left( \sum_{i=0}^{n} y_u \frac{x_i}{y_i} \right) = f(1) = 1 \cdot \log_2(1) = 0
$$

#### 3.1.1. Uwaga
Można dopuścić $>0$ oraz $1 = \sum_{i=0}^n x_i \ge \sum_{i=0}^n y_i$.\
Nawiasem mówiąc, jeśli $\sum x_i > \sum y_i$ to dostaniemy ostrą nierówność.

---

### 3.2. Wniosek (*frukt z twierdzenia*)

- $|X| = N \qquad H(X) = \sum_{i=1}^N p_i \log_2 \frac{1}{p_i}$
- $H(X) \le \sum_{i=1}^N p_I \log_2 \frac{1}{q_i}$ dla dowolnego ($q_i > 0 \enspace \sum_{i=1}^N q_i = 1$)
- dla $q_1 = \frac{1}{N}$ dostajemy:
    - $H(X) \le \sum_{i=1}^N p_i \log_2 N = \log_2 N$.
- dla $p_i = \frac{1}{N}$ mamy:
    - $H(X) = \log_2 N$

#### 3.2.1. Ćwiczenie (było podobne)
Dla jakich $p_i$ mamy $H(X) = \log_2 N$.\
Zastanowić się, kiedy nierówności są ostre!

---
