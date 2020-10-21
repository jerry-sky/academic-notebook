# Klasa Kombinatoryczna
*(2020-10-08)*

- [1. DEF: Klasa kombinatoryczna](#1-def-klasa-kombinatoryczna)
- [2. *OGF — ordinary generating function*](#2-ogf--ordinary-generating-function)
- [3. Przykład łączenia dwóch klas](#3-przykład-łączenia-dwóch-klas)
- [4. Przykłady klas](#4-przykłady-klas)
    - [4.1. Przykład](#41-przykład)
    - [4.2. Przykład](#42-przykład)
    - [4.3. Przykład](#43-przykład)
    - [4.4. Przykład](#44-przykład)
    - [4.5. Przykład](#45-przykład)
    - [4.6. Przykład](#46-przykład)
    - [4.7. Przykład](#47-przykład)
    - [4.8. Przykład](#48-przykład)
- [5. Izomorfizm](#5-izomorfizm)

---

## 1. DEF: Klasa kombinatoryczna

$\mathcal{A}(A, |\cdot|$

1. $A \neq \emptyset$
2. $|\cdot|: A \to \mathbb{N}_+$
3. $\{a \in A: |a| = n\} = A_n$

$a_n = |A_n| < \infty$

## 2. *OGF — ordinary generating function*

$A(z) = \sum_{n\ge0} a_n z^n$

$[z^n]A(z) = a_n$

## 3. Przykład łączenia dwóch klas

$\mathcal{A} = (A,|\cdot|_A)$\
$\mathcal{B} = (B,|\cdot|_B)$

$A\cap B = \emptyset$

$\mathcal{A} + \mathcal{B} = (A\cup B, |\cdot|)$

$$
|\cdot| =
\begin{cases}
    |x|_A & x \in A\\
    |x|_B & x \in B
\end{cases}
$$

$(A+B)(z) = \sum_{x \in A\sum B} z^{|x|} = \sum_{x\in A} z^{|x|_A} + \sum_{x \in B} z^{|x|_B} = A(z) + B(z)$

---

## 4. Przykłady klas

### 4.1. Przykład

$\mathcal{A} = (\{\epsilon\}, |\cdot|) \quad |\epsilon| = 0$

$A(z) = \sum_{a\in A} z^{|a|} = z^{|\epsilon|} = z^0 = 1$

---

### 4.2. Przykład

$\mathcal{A} = (\{\circledcirc, \square, \triangle\}, |\cdot| = \{ \circledcirc \to 1, \square \to 1, \triangle \to 0 \}$

$A(z) = 2z + 1 \cdot z^0 = 2z + 1$

$\mathcal{N}(\mathbb{N}, |\cdot|) ~~~~~ |i| = i$

$\mathcal{N}(z) = z^0 + z^1 + \cdots = \frac{1}{1-z}$

---

### 4.3. Przykład

$\mathcal{N} = (\{0,1,2,3,\dots\}, |\cdot|) \quad |i| = i$

$N(z) = \sum_{i\in N} z^{|i|} = \sum_{i\ge0} z^i = \frac{1}{1-z}$

---

### 4.4. Przykład

$\mathcal{N}^+ = (\{1,2,3,\dots\}, |\cdot|) \quad |i| = i$

$\mathcal{N}^+ = \frac{z}{1-z}$

---

### 4.5. Przykład

$\mathcal{N}_{\ge3} = (\{ 3,4,5,6,\dots \}, |\cdot|)$

$\mathcal{N}_{\ge3}(z) = \sum_{x\in N_{\ge3}} z^{|x|} = z^3 + z^4 + z^5 + \cdots = z^3(1+z+\cdots) = z^3 \cdot \frac{1}{1-z} = \frac{z^3}{1-z}$

---

### 4.6. Przykład

$\mathcal{P} = \{\epsilon, 1, 1–2, 2–1, 1–2–3, 1–3–2,3–2–1,\dots\}$

$|P_n| = n!$

$P(z) = \sum_{n\ge 0} n! z^n$ zbieżna tylko dla $z = 0$

---

### 4.7. Przykład

$\mathcal{N}_{Even} = (\{0,2,4,6,8,\dots\}, |\cdot|)$\
$\mathcal{N}_{Odd} = (\{1,3,5,7,\dots\}, |\cdot|)$

$\mathcal{N}_{Even}(z) = z^0 + z^2 + z^4 + \cdots = 1 + z^2 + z^4 + \cdots = \frac{1}{1-z^2}$

$\mathcal{N}_{Odd}(z) = \cdots = z\cdot\mathcal{N}_{Even}(z) = \frac{1}{1-z^2} \cdot z$

$\mathcal{A} \sim A(z) ~~~~~ \mathcal{B} \sim B(z)$\
$\mathcal{A} + \mathcal{B} \sim A(z) + B(z)$

$\mathcal{N}_{Even} + \mathcal{N}_{Odd} \sim \mathcal{N}$

$\mathcal{N}_{Odd}(z) + \mathcal{N}_{Even}(z) = \frac{1}{1-z^2} + \frac{1}{1-z^2} = \frac{1+z}{1-z^2} = \frac{1}{1-z} = 1 + z + z^2 + z^3 + \cdots = \mathcal{N}(z)$

---

### 4.8. Przykład

$\mathcal{W} = (\{\epsilon, 0, 1, 00, 01, 10, 11, 000, 001, 010, 100, 110, \dots\}, |\cdot|)$

$|w| =$ długość ciągu

$W(z) = \sum_{n\ge0} 2^n z^n = \sum_{n\ge0} (2z)^n = \frac{1}{1 - 2z}$

$[z^{1000}]W(z) = 2^1000$

---

## 5. Izomorfizm

Dwie klasy kombinatoryczne $\mathcal{A}$ oraz $\mathcal{B}$ o OGF $A(z)$ oraz $B(z)$ są izomorficzne wtedy i tylko wtedy gdy $A(z) = B(z)$. Wówczas piszemy
$$
\mathcal{A} \cong \mathcal{B}
$$
