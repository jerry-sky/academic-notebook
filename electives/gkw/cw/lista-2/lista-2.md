---
lang: 'pl'
title: 'Lista 2.'
subtitle: 'Grafika komputerowa i wizualizacje, Ćwiczenia'
author: 'Jerry Sky'
---

- [Zadanie 1.](#zadanie-1)
    - [Idea](#idea)
    - [Rozwiązanie](#rozwiązanie)
- [Zadanie 2.](#zadanie-2)
    - [Idea](#idea-1)
    - [Rozwiązanie](#rozwiązanie-1)
- [Zadanie 3.](#zadanie-3)
    - [Rozwiązanie](#rozwiązanie-2)

---

## Zadanie 1.

> Napisz procedurę sprawdzającą, czy punkty $P_1, P_2, P_3 \in \reals^2$ są współliniowe.

### Idea

1. Wyznaczamy linię przechodzącą przez dwa punkty.
2. Sprawdzamy, czy trzeci punkt należy do linii.

### Rozwiązanie

1. Niech $P_1 = (x_1, y_1) \quad P_2 = (x_2, y_2) \quad P_3 = (x_3, y_3)$.
2. $A = \left\lvert x_1 - x_2 \right\rvert, \quad B = \left\lvert y_1 - y_2 \right\rvert.$
3. `if` $A \neq 0$:
    1. $a = \frac{B}{A}.$
    2. Narazie mamy nachylenie $a$: $y = ax + b$.
    3. Szukamy $b$: $b = y_1 - a x_1$.
    4. Mamy wzór linii $y = ax + b$.
    5. `if` $y_3 = a x_3 + b$:
        1. `return` $\mathrm{True}$
    6. `else`:
        1. `return` $\mathrm{False}$
4. `else`: \[mamy do czynienia z linią pionową\]
    1. `if` $x_3 = x_1$:
        1. `return` $\mathrm{True}$
    2. `else`:
        1. `return` $\mathrm{False}$

---

## Zadanie 2.

> Napisz procedurę sprawdzającą, czy punkty $P_1, P_2, P_3 \in \reals^3$ są współliniowe.

### Idea

Wykorzystamy tutaj rozwiązanie z zadania 1.

Niech $\operatorname{CPW2W(P_1, P_2, P_3)}$ będzie funkcją z zadania 1.

1. Dzielimy przestrzeń trójwymiarową na dwie płaszczyzny odzwierciedlające dwie perspektywy
$XY$ oraz $ZY$.
2. Sprawdzamy współliniowość punktów względem tych dwóch perspektyw.

---

### Rozwiązanie

1. Niech:
    1. $P_{1XY} = (x_1, y_1), \enspace P_{1ZY} = (z_1, y_1)$,
    2. $P_{2XY} = (x_2, y_2), \enspace P_{2ZY} = (z_2, y_2)$,
    3. $P_{3XY} = (x_3, y_3), \enspace P_{3ZY} = (z_3, y_3)$.
2. `if` $\operatorname{CPW2W}(P_{1XY}, P_{2XY}, P_{3XY}) \land \operatorname{CPW2W}(P_{1ZY}, P_{2ZY}, P_{3ZY})$:
    1. `return` $\mathrm{True}$
3. `else`:
    1. `return` $\mathrm{False}$

---

## Zadanie 3.

> Napisz procedurę sprawdzającą, czy dla $P_1, P_2, P_3, P_4 \in \reals^2$
> punkty $P_3$ i $P_4$ leżą po tej samej stronie prostej przechodzącej przez punkty $P_1, P_2$.

### Rozwiązanie

1. $A = \left\lvert x_1 - x_2 \right\rvert, \quad B = \left\lvert y_1 - y_2 \right\rvert.$
2. `if` $A \neq 0$:
    1. $a = \frac{B}{A}.$
    2. Narazie mamy nachylenie $a$: $y = ax + b$.
    3. Szukamy $b$: $b = y_1 - a x_1$.
    4. Mamy wzór linii $y = ax + b$.
    5. `if` $(y_3 > a x_3 + b) \enspace\oplus\enspace (y_4 > a x_4 + b)$:
        1. `return` $\mathrm{False}$
        2. \[oba punkty są po dwóch przeciwnych stronach\]
    6. `elif` $(y_3 = a x_3 + b) \enspace\land\enspace (y_4 = a x_4 + b)$:
        1. `return` $\mathrm{True}$
        2. \[oba punkty są na linii\]
    7. `else`:
        1. `return` $\mathrm{True}$
        2. \[oba punkty muszą być po tej samej stronie\]
3. `else`: \[linia pionowa\]
    1. `if` $(x_1 > x_3) \enspace\oplus\enspace (x_1 > x_4)$:
        1. `return` $\mathrm{False}$
    2. `elif` $x_3 = x_4$:
        1. `return` $\mathrm{True}$
    3. `else`:
        1. `return` $\mathrm{True}$

---
