# Liczby Stirlinga II rodzaju

*(2020-11-16)*

- [1. DEF](#1-def)
- [2. Notacja](#2-notacja)
- [3. Przykład](#3-przykład)
- [4. OGF](#4-ogf)

---

## 1. DEF

$S_n^{(r)}$ — liczba partycji zbioru $n$-elementowego na $r$ niepustych podzbiorów.

## 2. Notacja
$$
S_n^{(r)} = {n \brace m} = S(n,r)
$$

## 3. Przykład

Weźmy na przykład zbiór $\left\{ 5,4,2,6,7,1,3 \right\}$. Chcemy go podzielić na 3 podzbiory.

- wybieramy najpierw liderów zbiorów: $1,2,5$
- dobieramy następnych członków danego podzbioru tak, aby nowi członkowie nie byli mniejsi niż lider: $\{1,3,4\}, \{2,6\}, \{5,7\}$

Możemy zobaczyć nasz zbiór z podziałami w wersji posortowanej:\
![](liczby-stirlinga-2-rodzaju-przykład.png)

Ustalmy klasę kombinatoryczną:
$$
S(z) = s_1 \times \operatorname{SEQ}(s_1) \times s_2 \times \operatorname{SEQ}(s_1 + s_2) \times s_3 \times \operatorname{SEQ}(s_1 + s_2 + s_3)
$$
(gdzie $s_i$ to wyznaczone podzbiory)\
czyli OGF:
$$
z \frac{1}{1-z} \cdot z \cdot \frac{1}{1-2z} \cdot z \cdot \frac{1}{1-3z} =\\
z^3 \cdot \frac{1}{(1-z)(1-2z)(1-3z)} = S^{(3)}(z)
$$

Naturalne jest więc, że ${n \brace 3} = [z^n] S^{(3)}(z)$.

## 4. OGF

W wersji ogólnej: $S^{(r)}(z) = z^r \frac{1}{(1 - z)(1-2z)\dotsb(1 - rz)}$.

---
