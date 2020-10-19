# Klasa Kombinatoryczna
*(2020-10-08)*

- [1. DEF: Klasa kombinatoryczna](#1-def-klasa-kombinatoryczna)
- [1.1. *OGF — ordinary generating function*](#11-ogf--ordinary-generating-function)
- [1.2. Przykład łączenia dwóch klas](#12-przykład-łączenia-dwóch-klas)
- [1.3. Przykłady klas](#13-przykłady-klas)
    - [1.3.1. Przykład](#131-przykład)
    - [1.3.2. Przykład](#132-przykład)
    - [1.3.3. Przykład](#133-przykład)
    - [1.3.4. Przykład](#134-przykład)
    - [1.3.5. Przykład](#135-przykład)
    - [1.3.6. Przykład](#136-przykład)
    - [1.3.7. Przykład](#137-przykład)
    - [1.3.8. Przykład](#138-przykład)

---

## 1. DEF: Klasa kombinatoryczna

$\mathcal{A}(A, |\cdot|$

1. $A \neq \emptyset$
2. $|\cdot|: A \to \mathbb{N}_+$
3. $\{a \in A: |a| = n\} = A_n$

$a_n = |A_n| < \infty$

## 1.1. *OGF — ordinary generating function*

$A(z) = \sum_{n\ge0} a_n z^n$

$[z^n]A(z) = a_n$

## 1.2. Przykład łączenia dwóch klas

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

## 1.3. Przykłady klas

### 1.3.1. Przykład

$\mathcal{A} = (\{\epsilon\}, |\cdot|) \quad |\epsilon| = 0$

$A(z) = \sum_{a\in A} z^{|a|} = z^{|\epsilon|} = z^0 = 1$

---

### 1.3.2. Przykład

$\mathcal{A} = (\{\circledcirc, \square, \triangle\}, |\cdot| = \{ \circledcirc \to 1, \square \to 1, \triangle \to 0 \}$

$A(z) = 2z + 1 \cdot z^0 = 2z + 1$

$\mathcal{N}(\mathbb{N}, |\cdot|) ~~~~~ |i| = i$

$\mathcal{N}(z) = z^0 + z^1 + \cdots = \frac{1}{1-z}$

---

### 1.3.3. Przykład

$\mathcal{N} = (\{0,1,2,3,\dots\}, |\cdot|) \quad |i| = i$

$N(z) = \sum_{i\in N} z^{|i|} = \sum_{i\ge0} z^i = \frac{1}{1-z}$

---

### 1.3.4. Przykład

$\mathcal{N}^+ = (\{1,2,3,\dots\}, |\cdot|) \quad |i| = i$

$\mathcal{N}^+ = \frac{z}{1-z}$

---

### 1.3.5. Przykład

$\mathcal{N}_{\ge3} = (\{ 3,4,5,6,\dots \}, |\cdot|)$

$\mathcal{N}_{\ge3}(z) = \sum_{x\in N_{\ge3}} z^{|x|} = z^3 + z^4 + z^5 + \cdots = z^3(1+z+\cdots) = z^3 \cdot \frac{1}{1-z} = \frac{z^3}{1-z}$

---

### 1.3.6. Przykład

$\mathcal{P} = \{\epsilon, 1, 1–2, 2–1, 1–2–3, 1–3–2,3–2–1,\dots\}$

$|P_n| = n!$

$P(z) = \sum_{n\ge 0} n! z^n$ zbieżna tylko dla $z = 0$

---

### 1.3.7. Przykład

$\mathcal{N}_{Even} = (\{0,2,4,6,8,\dots\}, |\cdot|)$\
$\mathcal{N}_{Odd} = (\{1,3,5,7,\dots\}, |\cdot|)$

$\mathcal{N}_{Even}(z) = z^0 + z^2 + z^4 + \cdots = 1 + z^2 + z^4 + \cdots = \frac{1}{1-z^2}$

$\mathcal{N}_{Odd}(z) = \cdots = z\cdot\mathcal{N}_{Even}(z) = \frac{1}{1-z^2} \cdot z$

$\mathcal{A} \sim A(z) ~~~~~ \mathcal{B} \sim B(z)$\
$\mathcal{A} + \mathcal{B} \sim A(z) + B(z)$

$\mathcal{N}_{Even} + \mathcal{N}_{Odd} \sim \mathcal{N}$

$\mathcal{N}_{Odd}(z) + \mathcal{N}_{Even}(z) = \frac{1}{1-z^2} + \frac{1}{1-z^2} = \frac{1+z}{1-z^2} = \frac{1}{1-z} = 1 + z + z^2 + z^3 + \cdots = \mathcal{N}(z)$

---

### 1.3.8. Przykład

$\mathcal{W} = (\{\epsilon, 0, 1, 00, 01, 10, 11, 000, 001, 010, 100, 110, \dots\}, |\cdot|)$

$|w| =$ długość ciągu

$W(z) = \sum_{n\ge0} 2^n z^n = \sum_{n\ge0} (2z)^n = \frac{1}{1 - 2z}$

$[z^{1000}]W(z) = 2^1000$

---
