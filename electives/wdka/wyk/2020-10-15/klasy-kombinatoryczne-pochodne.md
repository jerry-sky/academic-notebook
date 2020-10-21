# Klasy kombinatoryczne pochodne

*(2020-10-15)*

- [1. Suma](#1-suma)
    - [1.1. OGF](#11-ogf)
    - [1.2. Przykład](#12-przykład)
- [2. Produkt kartezjański](#2-produkt-kartezjański)
    - [2.1. OGF](#21-ogf)
    - [2.2. Przykład](#22-przykład)
    - [2.3. Przykład](#23-przykład)
- [3. $\mathrm{SEQ}$](#3-mathrmseq)
    - [3.1. OGF](#31-ogf)
    - [3.2. Przykład](#32-przykład)
    - [3.3. Przykład](#33-przykład)
    - [3.4. Przykład](#34-przykład)
    - [3.5. Przykład](#35-przykład)
- [4. $\mathrm{PSET}$](#4-mathrmpset)
    - [4.1. OGF](#41-ogf)
    - [4.2. Przykład](#42-przykład)
    - [4.3. Przykład](#43-przykład)
    - [4.4. Przykład](#44-przykład)
- [5. $\mathrm{MSET}$](#5-mathrmmset)
    - [5.1. OGF](#51-ogf)
    - [5.2. Przykład](#52-przykład)
    - [5.3. Przykład](#53-przykład)
- [6. - …](#6---)

---

## 1. Suma

- $\mathcal{A} = \mathcal{B} + \mathcal{C}$
- $\mathcal{C}, \mathcal{B}$ mają zbiory $C$, $B$
- $\mathcal{A} = (B \cup C, |\cdot|)$

### 1.1. OGF
$A(z) = B(z) + C(z)$

### 1.2. Przykład

Mamy $\mathcal{A} = (\{ \triangle, \vert \}, |\cdot|_\mathcal{A})$ oraz $\mathcal{B} = (\{ 1,2 \}, |\cdot|_\mathcal{B})$.

Suma $\mathcal{C} = \mathcal{A} + \mathcal{B}$ czyli
$\mathcal{C} = (\{ \triangle, \vert, 1, 2 \}, |\cdot|)$.

---

## 2. Produkt kartezjański

$\mathcal{A} \times \mathcal{B} = (A \times B, |\cdot|) \quad |(a,b)| = |a|_A + |b|_B$

### 2.1. OGF
- $(A \times B) (z) = \sum_{n} |(A \times B)_n|z^n$
- $(A\times B)_n = \{ (a,b) \in A\times B: |a|_A + |b|_B = n \} = \bigcup_{k=0}^{n} \{ (a,b) \in A \times B: |a|_A = k \land |b|_B = n-k \} = \bigcup_{k=0}^{n} A_k \times B_{n-k} = (*)$; $|(*)| = \sum_{k=0}^{n} |A_k| \cdot |B_{n-k}| = |(A\times B)_n|$
- czyli wracając $(A \times B) (z) = \sum_{n} \left( \sum_{k=0}^{\infty} a_k \cdot b_{n-k} \right) z^n = A(z) \cdot B(z)$

---

### 2.2. Przykład
$\{ \triangle, \vert \} \times \{ 1,2 \} \to \{ (\triangle, 1), (\triangle, 2), (\vert, 1), (\vert,2) \}$

---

### 2.3. Przykład

$\mathcal{N} = (\{ 0,1,2,3,\dots, \}, |\cdot|: i \to |i|) \quad N(z) = \frac{1}{1-z}$

$\mathcal{N} \times \mathcal{N} \quad |(n_1, n_2)| = n_1 + n_2$\
dla przykładu $n=3 \qquad (\mathcal{N} \times \mathcal{N})_3 = \{ (0,3), (1,2), (2,1), (3,0) \}$

OGF dla $\mathcal{N} \times \mathcal{N}$: $(N\times N)(z) = \frac{1}{(1-z)^2}$

ile mamy takich par, że suma daje $3$? — $[z^3] \frac{1}{(1-z)^2} = (*)$\
*korzystamy z faktu z [wcześniejszego wykładu](../2020-10-05/powtórka-z-dyskretnej-i-analizy.md#fakt2)*\
$[z^3]\sum_{n\ge0} \binom{n+1}{1}z^n = [z^3] \sum_{n} (n+1) z^n = 4$ — zgadza się liczebność

---

## 3. $\mathrm{SEQ}$

$\mathcal{A} = (A,|\cdot|) \qquad A_0 = \emptyset, \enspace (a_0 = 0)$

$\mathrm{SEQ}(\mathcal{A}) = \underset{= \epsilon}{\mathcal{A}_0} + \mathcal{A} + (\mathcal{A} \times \mathcal{A}) + (\mathcal{A} \times \mathcal{A} \times \mathcal{A}) + \dotsb$

### 3.1. OGF

- $\alpha = (\alpha_1, \alpha_2, \dots, \alpha_k)$
- $|\alpha| = |\alpha_1| + |\alpha_2| + \dotsb + \dotsb + |\alpha_k|$
- $\mathrm{SEQ}(\mathcal{A}) \leftrightarrow \frac{1}{1 - A(z)}$

---

### 3.2. Przykład
$\mathrm{SEQ}(\{ 1,2 \}) \rightarrow \{ \epsilon, 1, 2, 11, 12, 21, 22 \}$

### 3.3. Przykład

$\mathcal{A} = (\{ \circ \}, |\cdot|), \quad |\circ| = 1, \quad A(z) = z$

- $\mathrm{SEQ}(\mathcal{A}) = \mathcal{A}_0 + \mathcal{A} + (\mathcal{A} \times \mathcal{A}) + (\mathcal{A} \times \mathcal{A} \times \mathcal{A}) + \dotsb$
- $\epsilon, (\circ), (\circ, \circ), (\circ, \circ, \circ), \dots$
- $0,1,2,3,\dots$

---

- $\mathrm{SEQ}(\mathcal{A})(z) = \frac{1}{1 - A(z)} = \frac{1}{1 - z} = \sum_{n\ge 0} z^n = N(z) \sim \mathcal{N}$
- $\mathrm{SEQ}(\mathcal{A})(z) \cong \mathcal{N}(z)$

---

### 3.4. Przykład

$\mathcal{a} = (\{ \leftarrow, \rightarrow \}, |\cdot|), \quad |\leftarrow| = |\rightarrow| = 1, \quad A(z) = 2z$

- $\mathrm{SEQ}(\mathcal{A})$ ma zbiór $\{ \emptyset, \leftarrow, \rightarrow, \rightarrow\rightarrow, \leftarrow\leftarrow, \leftarrow\rightarrow, \dotsb \}$
- $\mathrm{SEQ}(\mathcal{A})(z) = \frac{1}{1 - 2z} = \sum_{n \ge 0} (2n)^n = \sum_{n \ge 0} 2^n z^n$

---

### 3.5. Przykład

$\mathcal{Z} = (\{ 1, 2 \}, |\cdot|), \quad |1| = 1,~ |2| = 2$

- $Z(z) = z + z^2$
- $|(1,1,1,2,2,1)| = 8$zł (rozróżniamy kolejność monet)
- $\mathrm{SEQ}(\mathcal{Z})(z) = \frac{1}{1 - z - z^2}$
- $[z^8] \frac{1}{1-z-z^2}$

---

## 4. $\mathrm{PSET}$

$\mathcal{A} = (A, |\cdot|) \qquad |A| < \infty$

$\mathrm{PSET}(\mathcal{A}) = \prod_{\alpha \in A} (\{ \epsilon \} + \{ \alpha \})$

### 4.1. OGF
$\mathrm{PSET}(\mathcal{A})(z) = \prod_{n} (1 + z^n)^{B_n}$

Możemy OGF zapisać nieco inaczej.

Wykorzystamy:
$$
\ln(1+u) = \frac{u}{1} - \frac{u^2}{2} + \frac{u^3}{3} - \dotsb = \sum_{i} \frac{u^i}{i} \cdot (-1)^{i+1}
$$

Wówczas:
$$
A(z) = \prod_{n} (1 + z^n)^{a_n} = \exp\left( \ln(\prod_n (1+z^n)^{a_n}) \right) =\\
= \exp\left( \sum_{n \ge 1}^{\infty} a_n \sum_{k = 1}^{n} (-1)^{k-1} \cdot \frac{z^{n\cdot k}}{k} \right) =\\
exp\left( \frac{A(z)}{1} - \frac{A(z^2)}{2} + \frac{A(z^3)}{3} - \dotsb \right)
$$

---

### 4.2. Przykład

$\mathrm{PSET}(\{ 1,2 \}) \rightarrow \{ \emptyset, \{ 1 \}, \{ 2 \}, \{ 1,2 \} \}$

### 4.3. Przykład

- $A = \{ \heartsuit, 1, 2 \}$
- $\mathcal{P}(A) = \{ \emptyset, \{ \heartsuit \}, \dots, \{ \heartsuit, 1, 2 \} \}$
- $|A| = n \qquad |\mathcal{P}(A)| = 2^n$
- $A' \subseteq A$
- $|\{ \alpha_1, \alpha_2, \dots, \alpha_n \}| = |\alpha_1| + |\alpha_2| + \dotsb + |\alpha_n|$
- $\mathrm{PSET}(\mathcal{A}) = \prod_{\alpha \in A} (\{ \epsilon \} + \{ \alpha \})$
- $\mathrm{PSET}(\{ \heartsuit, 1, 2 \}) = (\{ \epsilon \} + \{ \heartsuit \}) \cdot (\{ \epsilon \} + \{ 1 \}) \cdot (\{ \epsilon \} + \{ 2 \})$
- $\mathrm{PSET}(\mathcal{A})(z) = \prod_{\alpha \in A} (1 + z^{|\alpha|}) = \prod_{n} (1+z^n)^{a_n}$

---

### 4.4. Przykład

Mamy:
- 50 banknotów po $1
- 10 banknotów po $2
- 10 banknotów po $5
- 10 banknotów po $20

które są rozróżnialne.

*Na ile sposobów można wypłacić $202?*

- $A(z) = 50z + 10 \cdot z^2 + 10 \cdot z^5 + 10 \cdot z^{20}$
- $\mathrm{PSET}(\mathcal{A})(z) = (1 + z)^{50} \cdot (1 + z^2)^{10} \cdot (1 + z^5)^{10} \cdot (1 + z^{20})^{10}$
- $[z^{202}] \mathrm{PSET}(\mathcal{A})(z)$

---

## 5. $\mathrm{MSET}$

$\mathcal{A} = (A, |\cdot|) \qquad |A| < \infty$

$\mathrm{MSET}(\mathcal{A}) \cong \mathrm{SEQ}(\mathcal{A})_{/R}$\
gdzie $R$ jest pewną relacją taką, że:
$$
(\alpha_1, \alpha_2, \dots, \alpha_k) R (\alpha_1', \alpha_2', \dots, \alpha_k')\\
\iff\\
\exists \text{ permutacja }\sigma \enspace \forall i \in [1;k] \enspace \alpha_i = \alpha_{\sigma(i)}'
$$

Inaczej: $\mathrm{MSET}(\mathcal{A}) = \prod_{\alpha \in A} \mathrm{SEQ}(\{ \alpha \})$

### 5.1. OGF

$\mathrm{MSET}(\mathcal{A})(z) = \prod_{\alpha \in A} \frac{1}{1 - z^{|\alpha|}} = \prod_{n \ge 0} (1 - z^{n})^{-a_n}$

Alternatywnie:\
$\mathrm{MSET}(\mathcal{A})(z) = \exp\left( \sum_{k=1}^{\infty} \frac{A\left( z^k \right)}{k} \right)$

---

### 5.2. Przykład

$\mathrm{MSET}(\{ 1,2 \}) \rightarrow \{ \emptyset, \{ 1 \}, \{ 1,1 \}, \{ 1,1,1 \} \dots \{ 1,2,2 \}, \{ 1,2,2,2 \} \dots \}$

Warto zauważyć, że zamiast zapisywać całej zawartości danego multizbioru (będącego elementem klasy komb.), można zapisać jako parę określającą liczebność każdego z elementów w tym multizbiorze.

Przykładowo, zamiast $\{ 1,1,1,2,2 \}$ można zapisać $(3,2)$, jako że występują trzy jedynki oraz dwie dwójki.\
*Trzeba jedynie ustalić kolejność opisywania liczebności.*

### 5.3. Przykład

*Na ile sposobów można wydać $101$zł monetami w nominałach $1$, $2$, $5$?*

---
Najpierw mniejszy przykład — 6zł:
- $(6, 0, 0)$
- $(4,1,0)$
- $(2,2,0)$
6. - …
---

- $A(z) = z + z^2 + z^5$
- $\mathrm{MSET}(\mathcal{A})(z) = \frac{1}{1-z} \cdot \frac{1}{1 - z^2} \cdot \frac{1}{1 - z^5}$
- $[z^{110}] \mathrm{MSET}(\mathcal{A})(z)$

---
