---
lang: 'pl'
title: 'Lista-4'
author: 'Jerry Sky'
date: '2020-12-20'
---

---

- [Zadanie 1.](#zadanie-1)
- [Zadanie 2.](#zadanie-2)
- [Zadanie 3.](#zadanie-3)
- [Zadanie 4.](#zadanie-4)

---

Do rozwiązań dołączone są pliki o rozszerzeniu `.wls` — są to pliki zawierające skrypty napisane w *WolframScript* i realizują praktyczną część danego zadania.

Uruchomienie na Linuxie (z zainstalowanym *Wolfram Mathematica* i *WolframScript*): `./ex-‹numer zadania›.wls`.

---

## Zadanie 1.

> Ile jest permutacji zbioru $30$-elementowego, składających się z cykli długości co najwyżej $5$?

Podobne zadanie do [zadania 2. z listy 4. z ćwiczeń](../../cw/lista-4/lista-4.md#zadanie-2) — tym razem jednak ograniczamy długość cykli:
$$
\mathcal{P}'' = \operatorname{SET}(\operatorname{CYC}_{\le5}(\mathcal{Z}))
$$
wówczas mamy EGF:
$$
P''(z) = \exp\left( \sum_{n=1}^5 \frac{z^n}{n} \right)
$$

Wynik: $30! \cdot [z^{30}] P''(z) = 19054894203999260640645120000 = 1.905489420399926064064512 \cdot 10^{28}$.

[Kod programu](ex-1.wls) znajduje się w pliku `ex-1.wls`.

---

## Zadanie 2.

> Ile jest permutacji zbioru $30$-elementowego, składających się z co najwyżej $5$ cykli?

*Implementacja [zadania 2. z listy 4. z ćwiczeń](../../cw/lista-4/lista-4.md#zadanie-2)*.

$$
P'(z) = \sum_{n=0}^5 \frac{\left( \ln \frac{1}{1-z} \right)^n}{n!}
$$

Wynik: $30! \cdot [z^{30}] P'(z) = 222444420953341570876847086387200 = 2.224444209533415708768470863872 \cdot 10^{32}$

[Kod programu](ex-2.wls) znajduje się w pliku `ex-2.wls`.

---

## Zadanie 3.

> Opisując odpowiednie BGF znaleźć wariancję liczby liter $a$ w losowym słowie nad alfabetem $\{a,b,c\}$ długości $n$.

Mówimy tutaj o BGF, czyli o funkcjach generujących dwóch zmiennych:
$$
A(z,u) = \sum_{n,k} a_{n,k} z^n u^k.
$$

Żeby móc określić taką funkcję, musimy oczywiście określić $a_{n,k}$.\
Idea: mówimy tutaj o ciągach (sekwencjach) liter $\{a,b,c\}$. Chcemy w jakiś sposób *oznaczyć* litery $a$ jako specjalne, jako że chcemy policzyć w pewnym sensie, jaka jest szansa na natrafienie na tę literkę.\
Takich słów jest $\binom{n}{k} \cdot 1^k \cdot 2^{n-k}$ bo za każdym razem wybieramy $k$ liter $a$ oraz $n-k$ liter $b$ lub $c$ — co za tym idzie $a_{n,k} = \binom{n}{k} \cdot 2^{n-k}$.

Wówczas
$$
A(z,u) = \sum_{n,k} \binom{n}{k} \cdot z^n \cdot 2^{n-k} \cdot u^k,
$$
a po przekształceniu:
$$
A(z,u) = \sum_{n\ge0} z^n \sum_{k\ge0} \binom{n}{k}u^k 2^{n-k}
$$
a ze znanej równości $\sum_{k=0}^n \binom{n}{k} a^k b^{n-k} = (a+b)^n$ mamy:
$$
A(z,u) = \sum_{n\ge0}z^n (u + 2)^n.
$$

Oczywiście niniejsza funkcja generująca idzie w parze z klasą kombinatoryczną $\mathcal{A} = (\{a,b,c\}, |\cdot|, \chi)$ gdzie $|\cdot|$ to po prostu funkcja długości słowa, a $\chi$ to funkcja określająca liczbę literek $a$ w danym słowie — czyli oznaczamy literkę $a$ jako *specjalną*.

Żeby obliczyć wariancję, musimy uzyskać wartość oczekiwaną oraz *drugi moment* zmiennej losowej $\chi$.

Mamy:
$$
\begin{aligned}
\operatorname{E}(\chi) &= \frac{[z^n]\frac{d}{du} A(z,u) \big|_{u=1}}{[z^n]A(z,1)}\\
\operatorname{E}(\chi^2) &= \frac{[z^n]\frac{d^2}{du^2} A(z,u) \big|_{u=1}}{[z^n] A(z,1)} + \frac{[z^n]\frac{d}{du} A(z,u) \big|_{u=1}}{[z^n]A(z,1)}
\end{aligned}
$$
co daje nam:
$$
\operatorname{Var}(\chi) = \operatorname{E}(\chi^2) - \big(\operatorname{E}(\chi)\big)^2
$$

Pozostaje policzyć $A(z,1)$:
$$
A(z,1) = \sum_{n\ge0} z^n (u + 2)^n = \sum_{n\ge0} z^n \underbrace{3^n}_{\text{super!}}.
$$

Wyniki:
- $\operatorname{E}(\chi) = \frac{n}{3}$
- $\operatorname{Var}(\chi) = \frac{n}{3} + \frac{(n - 1) \cdot n}{9} - \frac{n^2}{9} = \frac{2n}{9}$

[Kod programu](ex-3.wls) znajduje się w pliku `ex-3.wls`.

---

## Zadanie 4.

> Podać wariancję liczby cykli długości $3$ w permutacji o $30$ elementach.

Tak jak w [zadaniu poprzednim](#zadanie-3) oznaczamy wszystkie cykle długości $3$ jako *specjalne*.

Wówczas mamy klasę
$$
\mathcal{C} = \operatorname{SET}\left( \operatorname{CYC}_{\neq3}(\mathcal{Z}) + \underbrace{\operatorname{CYC}_{=3}(\mathcal{Z})}_{\text{oznaczone przy pomocy }\chi\,} \right)
$$
z funkcją generującą
$$
C(z,u) = \exp\left( \sum_{n\ge1}\left( \frac{z^n}{n} \right) - \frac{z^3}{3} + \frac{uz^3}{3} \right)
$$
gdzie właśnie to $u$ odznacza nam te cykle długości $3$, czyli nasza funkcja $\chi$ dla cykli długości $3$ zwraca $1$, kiedy dla pozostałych $0$.

Tak jak w poprzednim zadaniu potrzebujemy jeszcze $C(z,1)$:
$$
C(z,1) = \exp\left( \sum_{n\ge1}\left( \frac{z^n}{n} \right) - \frac{z^3}{3} + \frac{1 \cdot z^3}{3} \right) = \exp\left( \sum_{n\ge1} \left( \frac{z^n}{n} \right) \right) = \exp\left( \ln\frac{1}{1-z} \right) =\\
= \frac{1}{1-z} = \sum_{n\ge0} z^n
$$

Znowu, liczymy tak jak w poprzednim zadaniu wariancję:
$$
\operatorname{Var}(\chi) = \operatorname{E}(\chi^2) - \big(\operatorname{E}(\chi)\big)^2.
$$

Wyniki:
$$
\begin{aligned}
    \operatorname{E}(\chi) &=
    \begin{cases}
        0 & n \le 2\\
        \frac{1}{3} & n > 2
    \end{cases}
    \\[20pt]
    \operatorname{Var}(\chi) &=
    \begin{cases}
        0 & n \le 2\\
        \frac{2}{9} & n \in [3; 5]\\
        \frac{1}{3} & n > 5\\
    \end{cases}
\end{aligned}
$$
czyli dla $n = 30$ wariancja przyjmuje wartość $\frac{1}{3}$.

[Kod programu](ex-4.wls) znajduje się w pliku `ex-4.wls`.

---
