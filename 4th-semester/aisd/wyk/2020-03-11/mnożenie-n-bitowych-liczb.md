---
lang: 'pl'
title: 'Mnożenie $n$-bitowych liczb naturalnych'
author: 'Jerry Sky'
date: '2020-03-11'
---

---

- [Algorytm mnożenia $n$-bitowych liczb naturalnych $x \cdot y$](#algorytm-mnożenia-n-bitowych-liczb-naturalnych-x-cdot-y)
- [Złożoność obliczeniowa](#złożoność-obliczeniowa)

---

## Algorytm mnożenia $n$-bitowych liczb naturalnych $x \cdot y$

Możemy przedstawić liczby $x$ i $y$ jako ciągi binarne, które potem możemy podzielić na pół tak, że
$$
x = 2^{\frac{n}{2}} x_L + x_R
\\
y = 2^{\frac{n}{2}} y_L + y_R
$$

Przykładowo: $x = (1011~0110)_2$, wówczas $x_L = (1011)_2$, $x_R = (0110)_2$

Następnie zauważmy, że $x \cdot y = 2^n x_L y_L + 2^{\frac{n}{2}} \left( x_L y_R + x_R y_L \right) + x_R y_R$.\
Niestety algorytm typu [Divide & Conquer](../2020-03-09/divide-and-conquer.md) wykorzystujący powyższy podział i połączenie pod-problemów nie ma lepszej złożoności obliczeniowej od standardowego mnożenia, czyli $O(n^2)$. Natomiast jeśli zauważymy, że $x_L y_R = (x_L + x_R)(y_L + y_R) - x_L y_L - x_R y_R$ wtedy dostajemy trzy $\frac{n}{2}$-bitowe *(a nie cztery jak wcześniej)* pod-problemy:\
$x_L y_L$, $x_R y_R$, $(x_L + x_R)(y_L + y_R)$ co skutkuje złożonością $O\big(n^{\log_2 3}\big)$, gdzie $\log_2 3 \approx 1.59$.

## Złożoność obliczeniowa

Zamiast
$$
T(n) = \bold4 \cdot T\Big(\frac{n}{2}\Big) + O(n)
$$
mamy
$$
T(n) = \bold3 \cdot T\Big(\frac{n}{2}\Big) + O(n)
$$
co daje nam złożoność jedynie $O\big(n^{1.59}\big)$.

Całkowity czas spędzony na poziomie $k$ w drzewie rekursji wynosi
$$
3^k \cdot O\Big(\frac{n}{2^k}\Big) = \Big(\frac{3}{2}\Big)^k \cdot O(n).
$$
ponieważ każdy pod-problem $k$ tworzy trzy pod-pod-problemy o rozmiarze $\frac{n}{2^k}$.

Warto zauważyć, że $O\big(3^{\log_2n}\big) = O\big(n^{\log_23}\big)$, ponieważ
$$
3^{\log_2 n} =
\Big(n^{\log_n 3} \Big)^{\log_2 n} =
n^{\log_n3~\cdot~\log_2n} =
n^{\log_2(n^{\log_n3})} =\\
n^{\log_23}.
$$

Pseudokod:

`function multiply(`$x,y$`)`:\
input: $x,y \in \natnums$ w kodzie binarnym o długości $n$\
output: `multiply(`$x,y$`)`$= x \cdot y$
- $n = \max(size~of~x,~size~of~y)$
- `if` $n=1$:
  - `return` $x\cdot y$
- $x_L, x_R =$ `leftmost` $\lceil \frac{n}{2}\rceil$, `rightmost` $\lfloor\frac{n}{2}\rfloor$ bits of x
- $y_L, y_R =$ `leftmost` $\lceil \frac{n}{2}\rceil$, `rightmost` $\lfloor\frac{n}{2}\rfloor$ bits of y
- $P_1 =$ `multiply(`$x_L,y_L$`)`
- $P_2 =$ `multiply(`$x_R,y_R$`)`
- $P_3 =$ `multiply(`$x_L + x_R, y_L + y_R$`)`
- `return` $P_1 \cdot 2^n + (P_3 - P_1 - P_2) \cdot 2^{\frac{n}{2}} + P_2$

Source: [Algorithms: Dasgupta, Papadimitriou, Vazirani](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) - paragraph 2.1
