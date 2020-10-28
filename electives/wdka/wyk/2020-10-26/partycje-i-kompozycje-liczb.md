# Partycje i kompozycje liczb

*(2020-10-26)*

- [1. Partycje liczb a kompozycje liczb](#1-partycje-liczb-a-kompozycje-liczb)
- [2. Klasa kombinatoryczna dla partycji liczb](#2-klasa-kombinatoryczna-dla-partycji-liczb)
    - [2.1. OGF](#21-ogf)
    - [2.2. Przykład partycji liczby $3$](#22-przykład-partycji-liczby-3)
- [3. Partycje ograniczone](#3-partycje-ograniczone)
    - [3.1. Przykład partycji ograniczonej](#31-przykład-partycji-ograniczonej)
    - [3.2. Przykład kompozycji ograniczonej](#32-przykład-kompozycji-ograniczonej)
- [4. Kompozycja z podziałem](#4-kompozycja-z-podziałem)
- [5. Partycja z ograniczeniami](#5-partycja-z-ograniczeniami)

---

## 1. Partycje liczb a kompozycje liczb

Partycje liczb to są kompozycje liczb z pewnym ograniczeniem:
$$
n = x_1 + x_2 + x_3 + \dotsb + x_k \qquad x_i \ge 1\\
x_1 \ge x_2 \ge x_3 \ge \dots \ge x_k
$$

---

## 2. Klasa kombinatoryczna dla partycji liczb

Kiedy kompozycje można określić klasą $\mathcal{C} \cong \operatorname{SEQ}(\operatorname{SEQ}_{\ge 1}(\mathcal{Z}))$ to klasę opisującą partycje liczb można określić przez:
$$
\mathcal{P} \cong \operatorname{MSET}(\operatorname{SEQ}_{\ge 1}(\mathcal{Z}))
$$

### 2.1. OGF

$P(z) = \prod_{n=1}^\infty \frac{1}{1 - z^m}$

---

### 2.2. Przykład partycji liczby $3$

- $3 = 2 + 1$
- $3 = 1 + 1 + 1$
- $3 = 3$

---

## 3. Partycje ograniczone

- $\mathcal{P}^{T} \cong \operatorname{MSET}(\operatorname{SEQ}^{T}(\mathcal{Z}))$
- $n = x_1 + x_2 + x_3 + \dotsb + x_k$, gdzie $\forall i \enspace x_i \ge x_{i+1}$ oraz $\forall i\enspace x_i \in T$
- $T \subseteq \mathbb{N}$

---

### 3.1. Przykład partycji ograniczonej

Partycja liczb na $1$ oraz $2$.

$\mathcal{P}^{\left\{1,2\right\}}(z) = \frac{1}{1-z} \cdot \frac{1}{1-z^2}$

---

### 3.2. Przykład kompozycji ograniczonej

- $\mathcal{C}^{\left\{ 1,2 \right\}} \cong \operatorname{SEQ}(\left\{ 1,2 \right\})$
- $\mathcal{C}^{\left\{ 1,2 \right\}}(z) = \frac{1}{1 - z - z^2}$

Swoją drogą to $\mathcal{C}_n^{\left\{ 1,2 \right\}} = F_{n+1}$, bo zachodzi równość $\mathcal{C}_{n+1}^{\left\{ 1,2 \right\}} = \mathcal{C}_{n-1}^{\left\{ 1,2 \right\}} + \mathcal{C}_{n}^{\left\{ 1,2 \right\}}$

*Visual aid* jako przykład dla liczby $9$:\
![](przykład-kompozycji-ograniczonej.png)

---

## 4. Kompozycja z podziałem

Oznaczenie: $\mathcal{C}^{(k)}$ — kompozycja z podziałem na $k$ elementów

$\mathcal{C}^{(k)} \cong \operatorname{SEQ}_k(\mathcal{I}) = (\mathcal{I})^k \quad \mathcal{I} = \mathcal{N}_+$ (w rozumieniu liczby naturalne bez zera)

- $I(z) = \frac{z}{1-z}$
- $[z^n]\left( \frac{z}{1-z} \right)^k = \binom{n-1}{k-1}$

---

## 5. Partycja z ograniczeniami

Przy ustalonym pewnym $k$ mamy
$$
n = x_1 + x_2 + \dotsb + x_k\\
\text{przy czym } x_1 \ge x_2 \ge x_3 \ge \dotsb \ge x_k
$$

- $\mathcal{P}^{(k)} \cong \operatorname{MSET}(\operatorname{SEQ}_{\le k}(\mathcal{Z}))$
- $P^{(k)}(z) = \prod_{m=1}^k \frac{1}{(1-z^m)}$

---
