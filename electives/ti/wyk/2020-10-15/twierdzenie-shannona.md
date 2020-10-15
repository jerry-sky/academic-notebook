# Twierdzenie Shannon’a

*(2020-10-15)*

- [1. Twierdzenie Shannon’a — dokładniej](#1-twierdzenie-shannona--dokładniej)
    - [1.1. $L$](#11-l)
    - [1.2. Uwaga](#12-uwaga)
    - [1.3. Uwaga](#13-uwaga)
        - [1.3.1. Ćwiczenie](#131-ćwiczenie)
        - [1.3.2. Ćwiczenie](#132-ćwiczenie)
            - [1.3.2.1. Przykład](#1321-przykład)
            - [1.3.2.2. Przykład](#1322-przykład)

---

## 1. Twierdzenie Shannon’a — dokładniej

$H \le L$

Dokładniej:

$X = \{x_1, \dots, x_N\} ~~~~~ p_1, p_2, \dots, p_N$

$H(X) = -\sum_{i=1}^{N} p_i \log_2 p_i$

- kod to jest funkcja $c: X \to \{0,1\}^*$

- $c$ jest iniekcją

- wiemy, że $c$ jest prefiksowy, tzn $\forall~ x, x'~ x \neq x' \implies c(x) \text{ nie jest prefiksem } c(x')$

---

### 1.1. $L$

$L = L(c) = \sum_{i=1}^{N} p_i \underbrace{|c(x_i)|}_{l_i} = \sum_{i=1}^{N} p_i l_i$

### 1.2. Uwaga
- są też kody sufiksowe
- kody jednoznacznie dekodowalne:
    - dla dowolnego ciągu $\{0,1\}^*$ istnieje co najwyżej jeden podział $\sigma = \sigma_1 \frown \sigma_2 \frown \dots \frown \sigma_k$, taki by $\forall i \sigma_i \mathrm{rng}(XXXXXXXXXXXXXXXXXXXXXXXXXX)$

### 1.3. Uwaga

Kody prefiksowe (i też sufiksowe) są jednoznacznie dekodowalne

#### 1.3.1. Ćwiczenie
Znajdź jednoznacznie dekodowalny kod, który nie jest ani sufiksowy ani prefiksowy.

#### 1.3.2. Ćwiczenie
Kiedy co najwyżej można zamienić na dokładnie?
##### 1.3.2.1. Przykład
$\{x_1, x_2\} \qquad c(x_1) = 0 \qquad c(x_2) = 11$


$\sigma = 111$ nie da się podzielić na słowo kodowe

$\hat{c}(x_1) = 0 \qquad \hat{c}(x_2) = 1$ i wtedy O.K.

##### 1.3.2.2. Przykład
Jeśli istnieje $l$ takie, że $\forall i \enspace l_i = l$, to $c$ jest jednoznaczne dekodowalny (prefiksowy).

---
