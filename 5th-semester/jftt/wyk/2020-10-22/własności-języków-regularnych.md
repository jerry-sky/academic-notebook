# Własności języków regularnych

*(2020-10-22)*

- [1. Lemat o pompowaniu](#1-lemat-o-pompowaniu)
    - [1.1. D-d](#11-d-d)
- [2. Dowodzenie, że $L$ nie jest regularny](#2-dowodzenie-że-l-nie-jest-regularny)
    - [2.1. Przykład](#21-przykład)
    - [2.2. Przykład](#22-przykład)
    - [2.3. Przykład](#23-przykład)
- [3. Lemat o zamknięciu na działania](#3-lemat-o-zamknięciu-na-działania)
    - [3.1. D-d](#31-d-d)
- [4. Lemat o liczebności języków](#4-lemat-o-liczebności-języków)
- [5. Lemat o równoważności języków](#5-lemat-o-równoważności-języków)
    - [5.1. D-d](#51-d-d)

---

## 1. Lemat o pompowaniu

Niech $L$ będzie językiem regularnym. Wówczas istnieje stała $n$ taka, że jeśli $z$ jest dowolnym słowem z $L$ oraz $|z| \ge n$, to $z$ możemy przedstawić w postaci $z = uvw$, gdzie $|uv| \le n$ oraz $|v| \ge 1$ oraz $uv^iw$ należy do $L$ dla każdego $i \ge 0$.

- *($n$ jest nie większe niż liczba stanów najmniejszego DFA akceptującego $L$)*
- *(lemat ten jest używany do pokazywania, że dany język **nie** jest regularny)*

### 1.1. D-d

- $n$ — liczba stanów DFA
- $L \ni x_1,x_2,x_3,\dots, x_n,x_{n+1},\dots,x_m$
- mamy układ: $q_{i_0} \xrightarrow{x_1} q_{i_1} \xrightarrow{x_2} q_{i_2} \xrightarrow{x_3} \dots \xrightarrow{x_n} q_{i_n} \xrightarrow{x_{n+1}} \dots \xrightarrow{x_m} q_{\text{akceptujący}}$
- zauważmy, że elementów iteratora w stanach od $q_{i_0}$ do $q_{i_n}$ jest $n+1$, kiedy stanów naszego DFA jest $n$ czyli z zasady Dirichleta mamy przynajmniej jeden stan, który wystąpił dwa razy: $q_{i_k} = q_{i_j}$

- czytamy:
    $$
    \overbrace{x_1, \dots, x_k\underbrace{\text{»«}}_{\text{tu jesteśmy w }q_{i_k} = q_{i_j}}}^{u}\overbrace{x_{k+1},\dots,x_j \underbrace{\text{»«}}_{q_{i_j} = q_{i_k}}}^{v} \overbrace{x_{j+1},\dots,x_m \underbrace{»«}_{q_{\text{akceptujący}}}}^{w}
    $$
- stąd (że mamy powtarzające się stany) możemy pominąć lub powielić część $v$

---

## 2. Dowodzenie, że $L$ nie jest regularny

1. Załóżmy, że $L$ jest regularny i istnieje odpowiednie $n$.
2. Wybierzmy słowo $z$ zgodne z lematem (jego długość musi zależeć od $n$).
3. Pokażmy, że dla każdego podziału $z$ zgodnego z lematem istnieje $i$ takie, że $uv^iw \notin L$.

### 2.1. Przykład

Mamy $L = \left\{ 0^{i^2}: i \in \mathbb{N} \right\}$.

Załóżmy, że $L$ jest regularny i weźmy $n$ z Lematu o pompowaniu.\
Weźmy $z = 0^{n^2}$ oraz podzielmy $z = uvw$ w taki sposób, że:
- $|uv| \le n$
- $|v| \ge 1$

Bierzemy $i = 2$ (czyli patrzymy czy słowo należy do języka, jeśli zdwukrotnimy $v$).

*(szukamy słów o długości równej kwadratowi liczby naturalnej)*

$$
n^2 < |uv^2w| = |uvw| + |v| \le n^2 + n < (n+1)^2
$$

Nasze nowe słowo jest w przedziale **otwartym** $(n^2; n+1)$ co oznacza, że na pewno nie spełnia żądanego warunku długości słowa (miało być kwadratem liczby naturalnej).\
Zatem $L$ nie jest regularny.

### 2.2. Przykład

Mamy $L = \left\{ x \in \left\{ a,b \right\}^*: |x|_a = |x|_b \right\}$ czyli takie słowa, które mają taką samą liczbę $a$ co liczbę liter $b$.

- zakładamy, że $L$ jest regularny i istnieje $n$ z [Lematu o pompowaniu](#1-lemat-o-pompowaniu)
- $z = a^n b^n$
- patrzymy na możliwe podziały
- $\forall k = \left\{ 1,\dots,n \right\}\enspace (v^k)^i a^{n-k}b^n$
- łatwo zauważyć, że dodanie dowolnej liczby literek „$a$” wyrzuca nas z języka $\implies$ $L$ jest nieregularny

### 2.3. Przykład

Mamy $L = \left\{ x \in \left\{ a,b \right\}^*: |x|_a \neq |x|_b  \right\}$ czyli takie słowa, które mają różne liczby literek $a$ oraz $b$.

- zakładamy, że $L$ jest regularny i istnieje $n$ z [Lematu o pompowaniu](#1-lemat-o-pompowaniu)
- $z = a^n b^{n+1}$
- patrzymy na możliwe podziały
- $\forall i \enspace (a^2)^i a^{n-2} b^{n+1} \in L$ — nie udało się udowodnić
- bierzemy inne słowo $z = a^n b_{n! + n} \in L$ — znowu nie
- bierzemy $k \in \left\{ 1, \dots, n \right\}$
- bierzemy słowo $(a^k)^i a^{n-k} b^{n! + n}$
- tutaj wystarczy wziąć $i = \frac{n!}{k} + 1$, żeby słowo wyleciało z języka, ponieważ po podstawieniu wychodzi, że mamy tyle samo liter $a$ co $b$ ($k \cdot \left( \frac{n!}{k} + 1 \right) + (n-k) = n! + n$)
- zatem $L$ jest nieregularny

---

## 3. Lemat o zamknięciu na działania

Klasa języków regularnych jest zamknięta na operację sumy, dopełnienia, przecięcia, złożenia i domknięcia Kleene’ego.

### 3.1. D-d

1. Suma, złożenie i domknięcie Kleene’ego (z [definicji RE](../2020-10-08/języki-formalne-wprowadzenie.md#52-działania))
2. Dopełnienie:

    jeśli $L$ jest akceptowany przez DFA $M = (Q, \Sigma, \delta, q_0, F)$\
    wówczas $\overline{L}$ akceptowany przez $M' = (Q,\Sigma, \delta, q_0, Q \setminus F)$.

3. Przecięcie:

    Jeśli $L_1$ oraz $L_2$ są akceptowane przez odpowiednie DFA $M_1 = (Q_1, \Sigma, \delta_1, q_1, F_1)$ oraz $M_2 = (Q_2, \Sigma, \delta_2, q_2, F_2)$\
    wówczas $L_1 \cap L_2$ jest akceptowany przez $M = (Q_1 \times Q_2, \Sigma, \delta, (q_1, q_2), F_1 \times F_2)$, gdzie $\delta((p,q),a) = (\delta_1(p,a), \delta_2(q,a))$.

4. Suma:

    $M = \big(Q_1 \times Q_2, \Sigma, \delta, (q_1, q_2), (Q_1 \times Q_2) \setminus ((Q_1 \setminus F_1) \times (Q_2 \setminus F_2))\big)$.

---

## 4. Lemat o liczebności języków

Zbiór słów akceptowanych przez DFA $M$ o $n$ stanach jest:
1. niepusty $\iff M$ akceptuje słowo o długości mniejszej niż $n$
2. nieskończony, jeśli $M$ akceptuje słowo o długości $l$, dla $n \le l \le 2n$.

---

## 5. Lemat o równoważności języków

Istnieje algorytm rozstrzygający czy dwa automaty skończone są równoważne (akceptują te same języki).

### 5.1. D-d

- weźmy $M_1$ oraz $M_2$, które są DFA akceptującymi odpowiednio języki $L_1$ oraz $L_2$
- jeśli $L_1 \neq L_2$ wówczas $(L_1 \cap \overline{L_2}) \cup (\overline{L_1} \cap L_2)$ jest niepusty

---
