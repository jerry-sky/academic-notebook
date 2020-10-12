# Miara Informacji Hartley’a
*(2020-10-08)*

- [1. „Addytywność” owej miary](#1-addytywność-owej-miary)
- [2. DEF: **Miara ilości informacji**](#2-def-miara-ilości-informacji)
    - [2.1. Uwaga](#21-uwaga)
    - [2.2. Uwaga](#22-uwaga)
    - [2.3. Własności $I$](#23-własności-i)
- [3. Twierdzenie#1](#3-twierdzenie1)
    - [3.1. D-d Twierdzenie#1](#31-d-d-twierdzenie1)
        - [3.1.1. Eureka#1](#311-eureka1)
        - [3.1.2. Eureka#2](#312-eureka2)
        - [3.1.3. Kontynuacja D-d Twierdzenie#1](#313-kontynuacja-d-d-twierdzenie1)
        - [3.1.4. Zatem](#314-zatem)

---

Mamy zbiór $X$ $N$-elementowy (elementy $X$ są jednakowo prawdopodobne)

$I_H(X) = \log_2N$

## 1. „Addytywność” owej miary

$X = \{x_1, x_2, \dots, x_{N\cdot M}\} ~~~ |X| = N\cdot M$

$\widetilde{X} = \{X_1, X_2, \dots, X_M\}$\
$X_1 = \{x_1, \dots, x_N\}$\
$X_j = \{x_{(j-1)\cdot N +1}, \dots, x_{(j-1)\cdot N + N}\}$\
$\dotsc$\
$X_M$

$I_H(X_j) = \log_2 N$\
$I_H(\widetilde{X}) = \log_2 M$

$\bold{I_H(X) = \log_2(NM) = \log_2 N + \log_2 M = I_H(X_j) + I_H(\widetilde{X}).}$

---

$\widetilde{X} = \{X_1, X_2, \dots, X_N\}$\
$X = \dot{\bigcup}_{i=1}^N X_i ~~~ |X_i| = M_i$ (w całym $X$ elementy są jednakowo prawdopodobne)

$I_H(X_j) = \log_2 M_j ~~~|~~~ I_H(X) = \log_2(\sum_{i=1}^N M_i)$

$I_{?j}(\widetilde{X}) = I_H(X) - I_H(X_j) = \log_2\left( \frac{\sum_{i=1}^{N}}{M_j} \right) = \log_2 \frac{1}{p_j}$ gdzie $p_j$ to p-o zdarzenia $X_j$.

---

## 2. DEF: **Miara ilości informacji**
$\bold{I: X \to \mathbb{R}}$ gdzie $X = \{x_1, \dots, x_N\}$ jest dyskretną przestrzenią probabilistyczną

$P(x_i) = p_i ~~~~~ I(x_i) = -\log_2 p_i$.

### 2.1. Uwaga
Ową definicję stosujemy też gdy $X$ jest (dyskretną) zmienną losową.

### 2.2. Uwaga
$I: (0, 1] \to \mathbb{R}$ też ma sens.

$I(x_i) ~~„=”~~ I(p_i) = -\log_2 p_i$

### 2.3. Własności $I$

1. $I(1) = 0, I\left(\frac{1}{2}\right) = 1$, $\lim_{i\to 0^+} I(p) = +\infty$
2. $I(pq) = I(p) + I(q)$\
    mamy zdarzenie $X\cap Y$, gdzie $X,Y$ niezależne, $P(X) = p, P(Y) = q$\
    (coś jak [„addytywność”](#1-addytywność-owej-miary) wcześniej)
3. $I$ jest różniczkowalna

---

## 3. Twierdzenie#1

Jeśli $I: (0,1] \to \mathbb{R}$ jest różniczkowalną funkcją spełniającą [2.3.2.](#23-własności-i) oraz $I(\frac{1}{2}) = 1$,\
to $I(p) = -\log_2p$.

### 3.1. D-d Twierdzenie#1

$$
I'(p) = \lim_{\epsilon \to 0^-} \frac{I(p+\epsilon) - I(p) - I(p)}{\epsilon} =\\
\lim_{\epsilon \to 0^-} \frac{I(p+\epsilon p) - I(p)}{\epsilon p} = \text{(ponieważ 2.3.2.)}\\
\lim_{\epsilon \to 0^-} \frac{I(p) + I(1+\epsilon) - I(p)}{\epsilon p} =\\
\frac{1}{p}\lim_{\epsilon \to 0^-} \frac{I(1+\epsilon)}{\epsilon}
$$

#### 3.1.1. Eureka#1
$\lim$ istnieje!
#### 3.1.2. Eureka#2
$\lim_{\epsilon \to 0^-} I(1+\epsilon) = 0$, czyli z ciągłości $I(1) = 0$.

#### 3.1.3. Kontynuacja D-d Twierdzenie#1

Niech $C = \lim_{\epsilon \to 0^-} \frac{I(1+\epsilon)}{\epsilon}$

$I'(p) = \frac{1}{p} \cdot C$\
stąd $I(p) = \int{ \frac{C}{p}\, dp} = C\cdot \ln p + D$

Z [Eureka#2](#312-eureka2) mamy $I(1) = 0 = C\cdot \ln(1) + D = 0$ czyli $D = 0$.

Za to $I(\frac{1}{2}) = 1 = C\cdot \ln(\frac{1}{2})$ czyli $C = -\frac{1}{\ln 2}$.

#### 3.1.4. Zatem

$I(p) = \frac{- \ln p}{\ln 2} = \frac{- \ln 2 \log_2 p}{\ln 2} = -\log_2 p$.\
$\blacksquare$
