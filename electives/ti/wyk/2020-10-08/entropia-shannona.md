---
lang: 'pl'
title: 'Entropia Shannon’a'
author: 'Jerry Sky'
date: '2020-10-08'
---

---

- [1. DEF: Entropia Shannon’a](#1-def-entropia-shannona)
    - [1.1. Uwaga](#11-uwaga)
    - [1.2. Przykład](#12-przykład)
        - [1.2.1. Jak zakodować informacje $x_1, \dots, x_8$?](#121-jak-zakodować-informacje-x_1-dots-x_8)
        - [1.2.2. Inny sposób](#122-inny-sposób)
    - [1.3. Eureka#1](#13-eureka1)

---

## 1. DEF: Entropia Shannon’a

Niech $X$ będzie dyskretną przestrzenią probabilistyczną\
$P(x_i) = p_i ~~~~~ X = \{x_i: i=1,2,\dots,N\}$

Entropia Shannon’a $H(X)$

$H(X) = \sum_{i=1}^{N} p_i \log_2 \frac{1}{p_i}$

### 1.1. Uwaga
$H(X) = \mathrm{E}I$ gdzie $I: X\to \mathbb{R}$, $I(x_i) = -\log_2 p_i$

### 1.2. Przykład

$X = \{x_1, x_2, \dots, x_8\}$

$p_1 = \frac{1}{2},~ p_2 = \frac{1}{8},~ p_3 = p_4 = \dots = p_8 = \frac{1}{16}$

$H(X) = \frac{1}{2}\log_2(2) + \frac{1}{8}\log_2(8) + 6 \cdot \frac{1}{16} \log_2(16) = \frac{1}{2} + \frac{3}{8} + \frac{3}{8}\cdot 4 = \frac{1}{2} + \frac{15}{8} = 2\frac{3}{8}$


#### 1.2.1. Jak zakodować informacje $x_1, \dots, x_8$?

$c(x_i) = (i-1)$ w systemie binarnym

każdy kod ma 3 bity

$c(x_1) = 000$\
$c(x_2) = 001$\
$\dots$

Głupie pytanie: **ile średnio zużywamy bitów?**\
**3!**

#### 1.2.2. Inny sposób

$\widetilde{c}(x_1) = 0$\
$\widetilde{c}(x_2) = 10$\
$\widetilde{c}(x_3) = 11\sqcup\sqcup\sqcup$\
$\dots$\
$x_8$

---
**A co teraz? Jaka średnia?**

$\widetilde{L}: X \to \mathbb{N}$\
$\widetilde{L}(x_i) =$ długość kodu $\widetilde{c}(x_i)$

$\mathrm{E}\widetilde{L} = ?$

$\mathrm{E}\widetilde{L} = \frac{1}{2}\cdot 1 + \frac{1}{8} \cdot 2 + 6 \frac{1}{16}\cdot 5 = \frac{3}{4} + \frac{15}{8} = \frac{21}{8} < 3$

---

$$
\underset{= \frac{19}{8}}{H(X)} \le \underset{= \frac{21}{8}}{\widetilde{L}(X)} \le \underset{= 3}{L(X)}
$$

### 1.3. Eureka#1
**Nasze kody są prefiksowe!**
