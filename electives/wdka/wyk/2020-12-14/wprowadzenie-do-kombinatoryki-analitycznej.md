# Wprowadzenie do kombinatoryki analitycznej

*(2020-12-14)*

- [1. Przykład (jawna postać OGF oraz współczynniki)](#1-przykład-jawna-postać-ogf-oraz-współczynniki)
- [2. Przykład (nieporządki)](#2-przykład-nieporządki)
- [Idea](#idea)

---

## 1. Przykład (jawna postać OGF oraz współczynniki)

*W jaki sposób możemy szybko uzyskać jawną postać OGF oraz jego współczynniki?*

Przykład: [*Drzewa Catalana (uporządkowane)*](../2020-10-19/plane-trees.md)

1. $\mathcal{T} = \mathcal{Z} \times \operatorname{SEQ}(\mathcal{T})$ *specyfikacja*
2. $T(z) = \frac{z}{1 - T(z)}$ *równanie OGF $T - T^2 = z$*
3. $T(z) = \frac{1 + \sqrt{1 - 4z}}{2}$ OGF w postaci jawnej
4. $T(z) = -\frac{1}{z} \sum_{n\ge0} \binom{\frac{1}{2}}{n} (-4z)^n$ rozwinięcie
5. $t_n = \frac{1}{n}\binom{2n-2}{n-1}$
6. $t_n \sim \frac{4^{n-1}}{\sqrt{\pi n^2}}$ (wzór Stirlinga)

Pytanie: *czy jesteśmy w stanie przejść z 1. do 6. od razu?*

---

## 2. Przykład (nieporządki)
*derangements*

1. $\mathcal{D} = \operatorname{SET}(\operatorname{CYC}_{>1}(\mathcal{Z}))$ (mówimy tutaj o EGF i strukturach etykietowanych oczywiście)
2. $D(z) = e^{\ln \frac{1}{1-z} - z} = \frac{e^{-z}}{1-z}$
3. $D(z) = \left( \sum_{k\ge0} \frac{(-2)^k}{k!} \right)\left( \sum_{n\ge0} z^n \right)$
4. $d_n = \sum_{0 \le k \le n} \frac{(-1)^k}{k!} \sim \frac{1}{e}$

## Idea

*Patrzymy na OGF/EGF jak na zwykłe funkcje z analizy matematycznej.*

Czyli mając na przykład $A(z) = \frac{1}{1-2z}$ wiadomo ile wynosi $a_n$, ale my chcemy bez tej wiedzy wcześniejszej na temat funkcji generujących określić, przybliżyć ile wynosi ten ciąg $a_n \sim 2^n$.



---
