# Rekurencja
###### 2-03-2020

## $1\degree$ Metoda indukcyjna

$$
T(n) = 4T(\frac{n}{2}) + n
$$
$$
T(1) = \Theta(1)
$$
*Założenie indukcyjne:*
$$
\forall{k<n}: T(k) \le c*k^3
$$
Robimy krok indukcyjny
$$
T(n) = 4T(\frac{n}{2}) + n \le 4c*\frac{n^3}{2^3} + n =
$$
$$
= c*n^3 + ( -\frac{c*n^3}{2} + n ) \le c*n^3
$$
$$
( -\frac{c*n^3}{2} + n )
$$

$$
-\frac{cn^3}{2} + n \le 0
$$
$$
\frac{cn^2}{2} \ge 1
$$

$$
c = 2, n_0 = 1
$$
$$
T(n) = O(n^3)
$$
---
$$
T(n) = O(n^2)
$$
*Założenie indukcyjne*
$$
\forall{k < n>}: T(k) \le ck^2
$$
Krok indukcyjny
$$
T(n) \le 4\frac{cn^2}{2^2} + n = cn^2 + n \le cn^2
$$

---
*Założenie indukcyjne*
$$
\forall{k < n }: T(k) \le c_1k^2 - c_2k
$$
$$
T(n) \le 4( c_1\frac{n^2}{4} - c_2 \frac{n}{2} ) + n =
$$
$$
= c_1n^2 - 2c_2n + n = (*) \le c_1n^2 - c_2n
$$
$$
(*) = c_1n^2 - c_2n + (c_2n + n) \le c_1n^2 - c_2n
$$
$$
(c_2n + n) \le 0
$$

$$
-c_2n + n \le 0
$$
$$
c_2 \ge 1
$$
$$
T(1) \le c_1 - c_2 \ge 0
$$

$$
T(n) = O(n^2)
$$
