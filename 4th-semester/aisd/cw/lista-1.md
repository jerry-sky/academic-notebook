# Lista 1

## Zadanie 1

> Jaka jest najmniejsza wartość $n$, dla której algorytm o złożoności $100n^2$ działa (na tej samej maszynie) szybciej od algorytmu o złożoności $2^n$?

$100n^2 < 2^n$ | $\lg$\
$2\lg(10n^2) < n = \lg 2^n$ | $$

---

Założenie indukcyjne: $\forall_{15\le k\le n}~100k^2 < 2^k$

$100(n+1)^2 < 2^{n+1}$\
$100(n^2 + 2n + 1) < 2^{n+1}$\
$100n^2 + (2n+1)\cdot100 < 2^n + 2^n \impliedby 200n + 100 < 2^n$

$n=15$\
$3100 < 2^{15}$

---

$n \ge 15$

$200n + 100 < 2^n$\
$200n + 100 \ge 100n^2 < 2^n$\
$2n + 1 \le n^2$ — trywialne

## Zadanie 2

|              - | 1s               |
| -------------: | ---------------- |
|       $\log n$ | $10^{10^6}$      |
|     $\sqrt{n}$ | $10^{12}$        |
|            $n$ | $10^6$           |
| $n\cdot\log n$ | $1,9 \cdot 10^5$ |
|          $n^2$ | $10^3$           |
|          $n^3$ | $10^2$           |
|          $2^n$ | $5\cdot\lg 10$   |
|           $n!$ | $\sim9,5$        |

## Zadanie 3

| lp. | funkcja         | złożoność                |
| --- | --------------- | ------------------------ |
| a   | $e^\pi$         | $O(1)$                   |
| b   | $(\log n)^{11}$ | $?$                      |
| c   | $\sqrt{2\pi n}$ | $O\left(\sqrt{n}\right)$ |
| d   | $n + 13$        | $O(n)$                   |
| e   | $n^2 \log n$    | $O(n^2\log n)$           |
| f   | $n^\pi$         | $O(n^x)$                 |
| g   | $10^n$          | $O(x_1^n)$               |
| h   | $33^n$          | $O(x_2^n)$               |

**g-h**:
$$
\frac{10^n}{33^n} = \left(\frac{10}{33}\right)^n \xrightarrow{n\to \infty} 0 < \infty
$$
$$
\implies 10^n = O(33^n)
$$

**f-g**:
$$
\frac{n^\pi}{10^n} = \frac{\pi n^{\pi -1}}{10^n\cdot\ln10} = \frac{\pi}{\ln10}\cdot\frac{n^{\pi -1}}{10^n} = C\cdot\frac{n^{\pi-3}}{10^n}\xrightarrow{n\to\infty}0 < \infty
$$

**b-c**:
$$
\frac{(\ln n)^{11}}{\sqrt{2\pi n}} = C\cdot\frac{(\ln n)^{11}}{\sqrt{n}} = C\cdot\frac{11(\ln n)^{10}\cdot\frac{1}{n}}{-\frac{1}{2\sqrt{n}}} =\\
= C \cdot \frac{-11(\ln n)^{10} \cdot2\sqrt{n}}{n} =\\
=D\frac{\ln n}{\sqrt{2}} = E\frac{1}{n\frac{1}{\sqrt{n}}} = \frac{F}{\sqrt{n}} \xrightarrow{n\to\infty} 0 < \infty
$$

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


