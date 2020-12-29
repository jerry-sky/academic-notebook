---
lang: 'pl'
title: 'Lista 2'
author: 'Jerry Sky'
---

---

- [Zadanie 1](#zadanie-1)
- [Zadanie 3](#zadanie-3)
- [Zadanie 4](#zadanie-4)

---

## Zadanie 1

*side-note:* $\sum_{k=0}^{n}c^k \le \sum_{k=0}^{\infin}c^k = \frac{1}{1-c}$ dla $|c| < 1$

$g(n) = 1 + c + c^2 + ... + c^n, ~ c>0$

1. $\Theta(1)$ jeśli $c<1$
    - $0<c<1$\
    $g(n) = 1 \frac{1-c^{n+1}}{1 - c} = \frac{1 - c^{n+1}}{1-c}$\
    $\lim_{n\to \infin}\frac{\frac{1-c^{n+1}}{1-c}}{1} = \lim_{n\to \infin}\frac{1 - c^{n+1}}{1-c} = \frac{1}{1-c}\lim_{n\to \infin}(1 - c^{n+1}) = \frac{1}{1-c} \cdot 1 = \frac{1}{1-c}$
2. $\Theta(n)$ jeśli $c = 1$
   - $g(n) = 1+n$\
     $\lim_{n\to \infin}\frac{1+n}{n} = 1$
3. $\Theta(c^n)$ jeśli $c > 1$
   - $\lim_{n\to \infin}\frac{1 + c + c^2 + ... + c^n}{c^n} =$\
   $\lim_{n\to \infin}(\frac{1}{c^n} + \frac{c}{c^n} + \frac{c^2}{c^n} + ... + \frac{c^n}{c^n}) =$\
   $\lim_{n\to \infin}\frac{\frac{1 - c^{n+1}}{1-c}}{c^n}=$\
   $\lim_{n\to \infin}(\frac{1 - c^{n+1}}{(1-c)c^n})=$\
   $\frac{1}{1-c}\lim_{n\to \infin}(\frac{1-c^{n+1}}{c^n}) =$\
   $\frac{1}{1-c}\lim_{n\to\infin}(\frac{1}{c^n}-c)=$\
   $\frac{1}{1-c}\cdot(-c) = \bold{\frac{c}{c-1}}$

    3'. *(końcówka)*\
    $c > 1$\
    $g(n) = \frac{1 - c^{n-1}}{1- c} = (*) = \Theta(c^n)$\
    $f(n) = \Theta(~h(n)~) \equiv (\exists d_1, d_2 \exists n_0 \forall n \ge n_0 d_1|h(n)| \le |f(n)| \le d_2|h(n)|)$\
    $(*) = \frac{1}{1-c} + \frac{c}{c-1}c^n$\
    $d_1 = 1 = \frac{1-c}{1-c} = \frac{c}{c-1} + \frac{1}{1-c},~ d_2 = \frac{c}{c-1},~ n_0 =10$\
    $1*c^n \le c^n\frac{c}{c-1} + \frac{1}{1-c} \le \frac{c}{c-1}c^n$ przy czym $\frac{1}{1-c}$ jest ujemne\
    $\frac{c}{c-1}c^n + \frac{1}{c-1}c^n \le \frac{c}{c-1}c^n + \frac{1}{1-c}$ dzielimy obie strony przez $\frac{1}{1-c}$\
    $c^n \ge 1$

## Zadanie 3

Udowodnij, że $\max\{ f(n), g(n) \} = \Theta(~f(n) + g(n)~)$

$\max\{ f(n), g(n) \} \le f(n) + g(n) =$\
$\max\{ f(n), g(n) \} + \min\{ f(n), g(n) \}$ przy czym $\max\{ f(n), g(n) \} \le 0$ oraz $\min\{ f(n), g(n) \} \le 0$

$c(f(n) + g(n)) \le \max\{ f(n), g(n) \}$, BSO $\max\{ f(n), g(n) \} = f(n)$\
$c \le \frac{f(n)}{f(n) + g(n)} = \frac{1}{1 + \frac{g(n)}{f(n)}} \in [\frac{1}{2}, 1)$ przy czym $\frac{g(n)}{f(n)} \in (0,1]$\
np $c = \frac{1}{4}$

$\upuparrows$ to wszystko od jakiegoś $n_0$

## Zadanie 4

Udowodnij, że $n! = o(n^n)$

$f(n) = o(g(n) \equiv (\forall \epsilon > 0)(\exists n_0)(\forall n \ge n_0)(|f(n)| \le c*g(n))$

$\lim_{n\to\infin} \frac{f(n)}{g(n)} = 0 \equiv (\forall \epsilon > 0)(\exists n_0)(\forall n \ge n_0)(|\frac{f(n)}{g(n)}| \le \epsilon)$\
$n! \sim (\frac{n}{2})^2\sqrt{2\pi n}$\
$\lim_{n\to\infin}\frac{n!}{(\frac{n}{3})^n\sqrt{2\pi n}} = 1$

$\lim_{n\to\infin}\frac{n!}{n^n} = \lim_{n\to\infin}\frac{(\frac{n}{e})^n\sqrt{2\pi n}}{n^n} = \lim_{n\to\infin}\frac{\frac{n^n}{e^n}\sqrt{2\pi n}}{n^n} = \lim_{n\to\infin}\frac{\sqrt{2\pi n}}{e^n} = 0$

$n! \le n^n$

*side-note without Stirling's approximation:*

$\lim_{n\to\infin}\frac{n!}{n^n}$

$\frac{1 * 2 * 3 * ... * n}{n * n * n * ... * n}$\
$0 \le \frac{n!}{n^n} \le \frac{1}{n}$ z twierdzenia o trzech ciągach $\lim_{n\to\infin}\frac{n!}{n^n} = 0$
