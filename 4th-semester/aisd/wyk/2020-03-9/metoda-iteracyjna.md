# Metoda iteracyjna
*(2020-03-9)*

$T(n) = 3T(\frac{n}{4}) + n$, $T(1) = \Theta(1)$

$$
= n+ 3(\frac{n}{4} + 3(\frac{n}{4^2} + 3T(\frac{n}{4}))) =
$$
$$
n + \frac{3}{4}n + (\frac{3}{4})^2n+ 3^3T(\frac{n}{4^3}) = (*)
$$

chcemy $\frac{n}{4^x}$ czyli $x = \log_2 n$

$$
(*) =n\sum_{k=0}^{\log n}(\frac{3}{4})^k = (**) \le n\sum_{k=0}^{\infin}(\frac{3}{4})^k = 4n
$$
czyli $T(n) = O(n)$

$$
(**) = n + (\frac{3}{4})n + (\frac{3}{4})^2n + ... + 3^{\log_2 n} \cdot T(1)
$$
wiemy, że $T(1) = \Theta(1)$\
oraz $a^{\log_b n} = b^{\log_b a^{\log_b n}} = b^{(\log_b n) \cdot (\log_b a)} = n^{\log_b a}$
$$
= n + (\frac{3}{4})n +(\frac{3}{4})^2n + ... + n^{\log_4 3} \cdot \Theta(1) \le
$$
przy czym $n^{\alpha},~\alpha < 1$
$$
\le n\sum_{k=0}^{\infin}(\frac{3}{4})^k + \Theta(n^2) = \bold{O(n)}
$$

