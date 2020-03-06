# Lista 1

## Zadanie 4

*Rando-student:*

$2^{\sqrt{n}},~n\log^3(n),~n^{\frac{4}{3}},~n^{\log(n)},~2^n,~2^{n^2},~2^{2^n}$

$2^{\sqrt{\log(n)}} = O(~n(\log(n))^3~)$\
$log_{2}2^{\sqrt{log(n)}} = O(~log_2(n\log(n))^3~)$\
$\sqrt{n} = O(~\log_2n + 3log_2(\log n)~) = O(~log_2n~)$

$\lim_{n\to \infin} \frac{n(\log n)^3}{n^{\frac{4}{3}}} = \lim_{n \to \infin} \frac{(log n)^3}{n^{\frac{1}{3}}} = \lim_{n\to \infin}(\frac{log n}{n^{\frac{1}{3}}})^3$\
$\lim_{n\to \infin} \frac{log n}{n^{\frac{1}{9}}} = \lim_{n \to \infin} \frac{\frac{1}{n}}{\frac{1}{9}n^{-\frac{8}{9}}} =$\
$9\lim_{n\to \infin}n^{-1} n^{\frac{8}{9}} = 9\lim_{n\to \infin}n^{-\frac{1}{9}} = 0$

$n^{\log n} \le c2^n$, weźmy $n_0 = 1, c = 1$\
$1 < 2$\
$n^{\log n} < 2^n$ nakładamy $log_2(...)$\
$log_2(~n^{\log_2 n}~) \le n$\
$(\log_2 n)(\log_2 n) \le n$\
$(\log_2 n)^2 \le n$\
$log_2 n \le \sqrt{n}$

**Recommended:**

$f(n) = O(~g(n)~) \impliedby \log f(x) = O(~\log g(x)~)$\
$f(n) = O(~g(n)~) \equiv (\exists~c\exists~n_0~\forall n \ge n_0: |f(n)| \le c|g(n)|)$\
$|2^{\sqrt{\log n}}| \le c|n \log n|$\
weźmy $n_0 = 2, c = 1$\
musimy pokazać $2^{\sqrt{\log n}} \le n(~\log n~)^3$ nakładamy na to $\log_2$\
$\sqrt{\log n} \le \log n + 3\log \log n$

$f(n) = O(~g(n)~) \equiv \limsup\limits{n \rightarrow \infin} \frac{|f(n)|}{|g(n)|} < \infin \impliedby \lim_{n \to \infin} \frac{|f(n)|}{|g(n)|} < \infin$

$$
f(n) =
\begin{cases}
  n ~dla~ n~mod~2=0\\
  2n ~dla~ n~mod~2=1
\end{cases}
= O(n)
$$


