# Języki

*(2020-10-26)*

- [1. Słowa](#1-słowa)
- [2. Przykład języka](#2-przykład-języka)
- [3. Przykład języka](#3-przykład-języka)

---

## 1. Słowa

Mamy $\mathcal{A} = (\left\{ a_1, a_2, \dots, a_m \right\}, |\cdot|)$, gdzie $\forall i \enspace |a_i| = 1$.

Wówczas $\mathcal{W} = \operatorname{SEQ}(\mathcal{A})$\
oraz $W(z) = \frac{1}{1 - mz}$, bo $A(z) = m\cdot z$.

---

## 2. Przykład języka

*Ile jest słów długości $n$ takich, że *nie ma* $k$ liter $a$ z rzędu?*\
$n=4,~ k=2 \qquad bbbb \quad abbb \quad abab \quad baba \quad \dots$

- $\mathcal{L} \cong a^{<k} \operatorname{SEQ}(b \cdot a^{<k})$
- $a^{<k} = \epsilon, a, aa, aaa, \dots, \underbrace{a\dots a}_{k-1}$
- $a^{<k}(z) = \frac{1 - z^k}{1-z}$
- $b\cdot a^{<k}(z) = \frac{z(1 - z^k)}{1-z}$
- $L(z) = \frac{1 - z^k}{1-z} \cdot \frac{1}{1 - \frac{z\cdot(1-z^k)}{1-z}} = \frac{1-z^k}{1 - 2z + z^{k-1}}$

---

## 3. Przykład języka

*Co, gdy chcemy policzyć, ile jest słów takich, że jest co najwyżej $k$ liter $a$ oraz $b$ z rzędu.*

- $\mathcal{W}^{(k,k)} \cong \operatorname{SEQ}_{\le k}(b) \cdot \operatorname{SEQ}(a \cdot \operatorname{SEQ}_{<k}(a) \cdot b \cdot \operatorname{SEQ}_{<k}(b)) \cdot \operatorname{SEQ}_{\le k}(a)$
- $W^{(k,k)}(z) = \left( \frac{1 - z^{k+1}}{1-z} \right)^2 \cdot \left( \frac{1}{1 - \frac{z^2}{\left( 1 - \left( \frac{1 - z^k}{1-z} \right) \right)^2}} \right)$
- jeżeli chcemy policzyć, ile jest ciągów, w których mamy dokładnie $k$-literowych podciągów naszych liter robimy: $W^{(k,k)}_n - W^{(k - 1, k - 1)}_n$

---
