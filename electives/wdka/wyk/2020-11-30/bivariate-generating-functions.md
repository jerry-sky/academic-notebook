# Bivariate generating functions (BGF)

*(2020-11-30)*

- [1. Klasa kombinatoryczna (zmodyfikowana)](#1-klasa-kombinatoryczna-zmodyfikowana)
- [2. Przykład](#2-przykład)
- [3. Przykład](#3-przykład)
- [Liczba elementów wagi $a_n$](#liczba-elementów-wagi-a_n)

---

## 1. Klasa kombinatoryczna (zmodyfikowana)

Tym razem oprócz funkcji rozmiaru $|\cdot|$ mamy drugą funkcję wagi $\chi$. Czyli mamy trójkę\
$\mathcal{A} = (A, |\cdot|, \chi)$\
z BGF $A(z,u) = \sum_{n,k} a_{n,k} z^n u^k$,\
gdzie $a_{n,k} = \left\lvert \left\{a \in A: |a| = n \land \chi(a) = k\right\} \right\rvert$.

- $A(z,u) = \sum_{a \in A} z^{|a|} u^{\chi(a)}$

---

## 2. Przykład

Mamy elementy:
- waga 1kg, cena 3zł,
- waga 1kg, cena 2zł,
- waga 2kg, cena 10zł.

Wówczas BGF: $f(u,z) = z u^3 + zu^2 + z^2 u^{10}$.

---

## 3. Przykład

Mamy alfabet $\{0,1\}$ z funkcjami wag:
- $|\cdot|$ — długość ciągu,
- $\chi$ — waga Hamminga.

$$
W(z,u) = \sum_{k,n}\binom{n}{k} z^n u^k = \sum_{n} z^n \left( \sum_{k} \binom{n}{k} u^k \right)=\\
= \sum_n z^n (1 + u)^n = \frac{1}{1 - z(1+u)}
$$

Ustalmy sobie pewne $k$:
$$
W^{(k)}(z) = \sum_n \binom{n}{k} z^n = \frac{z^k}{(1-z)^{k+1}}\\
W(z,u) = \sum_k u^k \cdot \frac{z^k}{(1-z)^{k+1}} = \frac{1}{1-z} \sum_k \frac{(zu)^k}{(1-z)^k} = \frac{1}{1-z} \cdot \frac{1}{1 - \frac{zu}{1-z}} =\\
= \frac{1}{1-z(1+u)}
$$

---

## Liczba elementów wagi $a_n$

- $A(z,u) = \sum_{n,k} a_{n,k} z^n u^k$
- $a_n = \left\lvert \left\{ a \in A: |a| = n \right\} \right\rvert$
- $[z^n] A(z,1) = [z^n] \sum_{n,k} a_{n,k} \cdot z^n = \sum_{k} a_{n,k}$

---
