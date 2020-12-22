# Klasy pomocnicze

*(2020-10-19)*

- [1. DEF $\mathcal{E}$](#1-def-mathcale)
    - [1.1. Przykład zastosowania](#11-przykład-zastosowania)
- [2. DEF $\mathcal{Z}$](#2-def-mathcalz)
    - [2.1. Przykład](#21-przykład)
    - [2.2. Przykład](#22-przykład)
    - [2.3. Przykład](#23-przykład)

---

## 1. DEF $\mathcal{E}$

$\mathcal{E} = (\{ \epsilon \}, \{ \epsilon \to 0 \})$

---

### 1.1. Przykład zastosowania

Normalnie $\mathcal{A} + \mathcal{B}$ działa tylko wtedy kiedy $A \cap B = \emptyset$.

Jeżeli nie mamy tego zapewnionego — kolorujemy klasy przy pomocy $\mathcal{E}_1$ oraz $\mathcal{E}_2$:
$$
\mathcal{A} \cong \mathcal{A} \times \mathcal{E}_1 \quad |(a, \epsilon_1)| = |a| + |\epsilon_1| = |a|\\
\mathcal{B} \cong \mathcal{B} \times \mathcal{E}_2 \quad |(b,\epsilon_2)| = |b| + |\epsilon_2| = |b|
$$
gdzie $\epsilon_i = (\{ \epsilon_i \}, \{ \epsilon_1 \to 0 \})$ dla $i = 1,2$.

(Tak samo dla kwadratu kartezjańskiego — kolorujemy i uzyskujemy osobne dwie klasy.)

---

## 2. DEF $\mathcal{Z}$

$\mathcal{Z} = (\{ \circ \}, \{ \circ \to 1 \})$

---

### 2.1. Przykład

Mamy alfabet $\mathcal{A} = (\{ a, b \}, |a|=|b|=1)$.

Wówczas możemy powiedzieć $\mathcal{A} \cong \mathcal{Z} + \mathcal{Z}$ Jednakże, taki zapis jest nieformalny, formalnie wygląda to tak:
$$
\mathcal{A} \cong (\mathcal{Z} \times \mathcal{E}_1) + (\mathcal{Z} \times \mathcal{E}_2)
$$

Dalej, możemy teraz wykorzystać alfabet do zbudowania wszystkich możliwych słów: $\mathcal{W}_2 \cong \mathrm{SEQ}(\mathcal{A})$.

---

### 2.2. Przykład

Możemy też zbudować liczby naturalne: $\mathcal{N} \cong \mathrm{SEQ}(\mathcal{Z})$.

---

### 2.3. Przykład

$n = x_1 + x_2 + x_3 + \dotsb + x_k \qquad (x_i \ge 1)$

*Ile jest kompozycji liczby $3$?*\
$3 = 1+2 + 2+1 = 1+1+1$ — mamy $4$ takie kompozycje

$\operatorname{SEQ}_{\ge1}(\mathcal{Z}) = \mathcal{Z} + (\mathcal{Z} \times \mathcal{Z}) + \dotsb$\
$\mathcal{Z} \leftrightarrow z$

OGF: $\operatorname{SEQ}_{\ge1}(\mathcal{Z})(z) \leftrightarrow \frac{z}{1-z}$

Czyli w zasadzie $\operatorname{SEQ}_{\ge1}(\mathcal{Z}) \cong \mathcal{N}_{\ge1}$

Zauważmy, że klasą wszystkich kompozycji jest po prostu $\mathcal{C} \cong \operatorname{SEQ}(\operatorname{SEQ}_{\ge1}(\mathcal{Z}))$.

OGF: $C(z) = \frac{1}{1 - \frac{z}{1-z}} = \frac{1-z}{1 - 2z} = \frac{1}{1-2z} - \frac{z}{1-2z}$

$[z^n]C(z) = [z^n]\frac{1}{1-2z} - [z^n]\frac{z}{1-2z} = 2^n - 2^{n-1} = 2^{n-1}$

*Czyli kompozycji liczby $n$ jest $2^{n-1}$.*

Dodatkowo *visual aid*:\
![](kompozycje-visual-aid.png)\
czyli wybieramy gdzie dać przegródki (mamy takich binarnych wyborów $n-1$)

---
