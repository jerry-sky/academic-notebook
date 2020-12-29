---
lang: 'pl'
title: 'Lista 0'
author: 'Jerry Sky'
---

---

- [Zadanie 1.](#zadanie-1)
- [Zadanie 2.](#zadanie-2)
- [Zadanie 3.](#zadanie-3)

---

## Zadanie 1.

> Udowodnić, że najdłuższa ścieżka od korzenia do liścia w dowolnym drzewie binarnym o $n$ wierzchołkach ma co najmniej $\lfloor\log_2n\rfloor$ krawędzi.

Musimy sprawdzić jak sytuacja wygląda dla *drzew zbalansowanych*, jako że to drzewa zbalansowane mają najkrótsze «drogi najdłuższe». Innymi słowy — chodzi o drzewa o jak najmniejszej wysokości.

Bez straty ogólności niech
$$
n = 2^k + l\\
\text{gdzie } l \in [0; 2^k) \cap \mathbb{N}
$$

![drzewo binarne](1.drzewo-binarne-1.png)

Warto zauważyć, że w przypadku drzewa zbalansowanego dodajemy kolejne węzły na tym samym „poziomie” i nie zaczynamy dodawać węzłów na następnych „poziomach” jeśli jest jeszcze miejsce na aktualnym.

![drzewo binarne 2^(k+1) - 1](1.drzewo-binarne-2.png)

$$
2^0 + 2^1 + 2^2 + \dotsb + 2^k = 2^{k+1} - 1
$$

(korzystamy z [zadania 3.2.](#zadanie-3) przy tamtejszym $k=2$)

Dalej, widzimy, że wysokość naszego drzewa jest taka sama dla liczby węzłów w przedziale $[2^k; 2^{k+1} - 1]$ i wynosi ona dokładnie $k$ co zgadza się z tym czego oczekiwaliśmy:\
wynik logarytmu „spłaszczamy”, bierzemy część całkowitą:
$$
\lfloor \log_2(2^k + l) \rfloor = log_2(2^k) = k
$$

$k$ — liczba o 1 mniejsza niż liczba węzłów na najdłuższej drodze czyli liczba krawędzi.

---

## Zadanie 2.

> Uogólnij zadanie 1. na drzewo, w którym każdy wierzchołek ma co najwyżej $\cancel{k}$ $p$ synów.

Dokonujemy zmian w [powyższych rozważaniach](#zadanie-1):
- zamieniamy $2$ na żądaną zmienną
- zamieniamy sumę $\sum_{i=0}^{k+1}2^i = 2^{k+1} - 1$ na sumę $\sum_{i=0}^{k+1}p^i = \frac{p^{k+1} - 1}{p - 1}$
- zmieniamy przedział: $l \in \left[0; p^{k}\cdot(p-1)\right)\cap \mathbb{N}$

---

## Zadanie 3.

> Mamy alfabet złożony z $k$ symboli. Policz ile jest:

1. > wszystkich różnych słów długości $n$ nad tym alfabetem

    $$
    1 \cdot \underbrace{k \cdot k \cdot \dotsb k}_{n \text{ razy}} = k^n
    $$

    ponieważ za każdym razem mamy $k$ możliwości do wyboru litery a potrzebujemy dobrać $n$ liter.

    1. $n=0$: $1 = k^0$ — mamy jedno słowo puste — *zgadza się*
    2. $n\implies n+1$:\
        mamy $\underbrace{k \cdot k \cdot \dotsb k}_{n \text{ razy}} = k^n$\
        doklejamy nową literę: dla każdej litery (mamy ich $k$) mamy osobno nowych $k^n$ słów; zatem:\
        $\underbrace{k^n + k^n + \dotsb + k^n}_{k\text{ razy}} = k \cdot k^n = k^{n+1}$
---
2. > wszystkich różnych słów długości co najwyżej $n$

    **Dowód tradycyjny:**\
    Niech
    $$
    \sum_{i=0}^{n}k^i = S_n
    $$

    Wówczas:

    $$
    S_n = \sum_{i=0}^{n}k^i\\
    //\cdot k
    \\
    S_n \cdot k = \sum_{i=1}^{n+1}k^i
    \\
    S_n \cdot k = S_n - 1 + k^{n+1}\\
    //-S_n
    \\
    S_n \cdot (k - 1) = k^{n+1} - 1
    \\
    \blacksquare
    $$

    **Dowód indukcyjny:**
    $$
    \sum_{i=0}^{n}k^i
    =
    \frac{k^{n+1} - 1}{k-1}
    $$

    1. $n=0$: $1 = k^0 = \frac{k^{1} - 1}{k-1} = 1$ — *zgadza się*
    2. $n \implies n+1$:
        $$
        \sum_{i=0}^{n}k^i = \frac{k^{n+1} - 1}{k-1}\\
        // + k^{n+1}
        \\
        \sum_{i=0}^{n+1}k^i = \frac{k^{n+1} - 1}{k-1} + \frac{k^{n+1} \cdot (k-1)}{k-1}
        \\
        \sum_{i=0}^{n+1}k^i = \frac{k^{n+1} - 1 + k^{n+2} - k^{n+1}}{k-1}
        \\
        \sum_{i=0}^{n+1}k^i = \frac{k^{n+2} - 1}{k-1}
        $$
        *zgadza się*
---
3. > wszystkich palindromów długości $n$

    rozważamy dwa przypadki:
    1. $n$ jest parzyste\
        dobieramy $\frac{n}{2}$ liter z alfabetu $k$-elementowego na jedną połówkę słowa:
        $$
        k^{\frac{n}{2}}
        $$
    2. $n$ jest nieparzyste\
        dobieramy $\left\lfloor \frac{n}{2} \right\rfloor$ liter z alfabetu $k$-elementowego na jedną połówkę słowa:
        $$
        k^{\left\lfloor \frac{n}{2} \right\rfloor}
        $$
        dodatkowo dobieramy jedną literę środkową słowa spośród $k$ liter

    dowód taki sam jak dla «3.1.»
---
4. > wszystkich palindromów długości co najwyżej $n$

    tak samo jak dla «3.2.» + «3.3.»
