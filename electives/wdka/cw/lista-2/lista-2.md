---
lang: 'pl'
title: 'Lista-2'
author: 'Jerry Sky'
date: '2020-11-11'
---

---

- [Zadanie 1.](#zadanie-1)
- [Zadanie 2.](#zadanie-2)

---

## Zadanie 1.

> Mamy nieograniczoną liczbę koralików w czterech różnych kolorach. Ile możemy zbudować naszyjników długości $3$? (Policzyć bez komputera!)

Określamy klasę kombinatoryczną:
$$
\mathcal{B} = \Big( \{a,b,c,d\}, |\cdot|: \forall x \enspace |x| = 1 \Big)\\
\mathcal{A} = \operatorname{CYC}(\mathcal{B})
$$
($\mathcal{B}$ to klasa pomocnicza, bazowa; skupiamy się na $\mathcal{A}$)

OGFs:
- $B(z) = 4z$
- $A(z) = \sum_{n\ge1} \frac{\varphi(n)}{n} \ln\frac{1}{1 - B\left( z^n \right)}$ gdzie $\varphi$ to funkcja Eulera

Przed obliczeniem żądanej wartości musimy nieco uprościć wzór OFG:
$$
A(z) = \sum_{n=1}^\infty \frac{\varphi(n)}{n} \ln \frac{1}{1 - 4z^n} =\\
=
\sum_{n=1}^\infty \left( \frac{\varphi(n)}{n} \cdot \sum_{k=1}^\infty \frac{(4z^n)^k}{k} \right)=\\
= \sum_{n=1}^\infty \left( \frac{\varphi(n)}{n} \cdot \sum_{k=1}^\infty \frac{4^k}{k} \cdot z^{n\cdot k} \right) =\\
= \sum_{n \ge 1,~ k \ge 1} \left( \frac{\varphi(n)}{n} \cdot \frac{4^k}{k} \right) \cdot z^{n\cdot k}
$$

Żądana wartość wynosi $[z^3]A(z)$ — czyli musimy znaleźć takie pary $(n,k)$, że $n\cdot k = 3$. Takich par mamy dwie: $(3,1)$ oraz $(1,3)$.

Zatem: $[z^3] A(z) = \frac{\varphi(1)}{1} \cdot \frac{4^3}{3} + \frac{\varphi(3)}{3} \cdot \frac{4}{1} = \frac{\varphi(1) \cdot 4^3 + \varphi(3) \cdot 4}{3} = \frac{64 + 8}{3} = 24$.

---

## Zadanie 2.

> Podaj wzór OGF dla klasy kombinatorycznej opisującej drzewa uporządkowane, takie, że każdy węzeł ma $2$ lub $0$ dzieci.

Klasa kombinatoryczna opisująca [drzewa uporządkowane](../../wyk/2020-10-19/plane-trees.md) gdzie każdy węzeł może mieć zero lub dwóch potomków wygląda następująco:
$$
\mathcal{T} \cong \mathcal{Z} \times \left( \mathcal{E} + \mathcal{T} \times \mathcal{T} \right)
$$
ponieważ zawsze dla każdego drzewa mamy jeden korzeń ($\mathcal{Z}$), który łączymy z zerem lub z dwoma kolejnymi poddrzewami.

OGF dla takiej klasy:
$$
T(z) = z \left( 1 + T^2(z) \right)
$$

Żeby uzyskać wersję OGF bez rekursji, musimy tutaj skorzystać z [Twierdzenia Lagrange’a o inwersji](../../wyk/2020-11-09/tw-lagrangea-o-inwersji.md).\
Niech $\varphi(x) = (1 + x^2)$\
*(wiemy, że jest to funkcja analityczna, bo każdy wielomian jest funkcją analityczną, bo wielomian jest swoim rozwinięciem Taylora)*.

Wówczas mamy:
$$
T(z) = z \cdot \varphi(T(z))
$$

Korzystamy z tego, że:
$$
[z^n] T(z) = \frac{1}{n} [x^{n-1}] \varphi^n(x)
$$
bo musimy w jakiś sposób uzyskać wszystkie współczynniki $a_n$ przy potęgach $z$ w klasycznym wzorze $\sum_{n\ge0} a_n z^n$.
$$
\frac{1}{n} [x^{n-1}] \varphi(x) = \frac{1}{n} [x^{n-1}] (1+x^2)^n =\\
= \frac{1}{n}[x^{n-1}] \sum_{k = 0}^n \binom{n}{k} x^{2k} =
\begin{cases}
    \frac{1}{n} \cdot \binom{n-1}{\frac{n-1}{2}} & n = 2k+1,\enspace k \in \mathbb{N}\\
    0 & \text{oth.}
\end{cases}
$$

Czyli wszystkie współczynniki parzyste musimy wyzerować — do tego użyjemy funkcji pomocniczej:
$$
f(n) = \frac{1}{2} \cdot (1 + (-1)^{n+1})
$$
wówczas
$$
T(z) = \sum_{n\ge0} z^n \cdot \left( f(n) \cdot \frac{1}{n} \cdot \binom{n-1}{\left( \frac{n-1}{2} \right)} \right).
$$

---
