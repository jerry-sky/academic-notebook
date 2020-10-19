# Powtórka z Dyskretnej i Analizy

*(2020-10-05)*

- [Iloczyn Cauchy’ego](#iloczyn-cauchyego)
- [Liczebność w zbiorach $(n+m)$–elementowych](#liczebność-w-zbiorach-nmelementowych)
- [Funkcje dwóch zmiennych](#funkcje-dwóch-zmiennych)
    - [Fakt#1](#fakt1)
- [Fakt#2](#fakt2)

---

## Iloczyn Cauchy’ego

$$
\left(\sum_{n\ge 0} a_n x_n\right)\left(\sum_{n\ge0} b_n x_n \right) = \sum_{n \ge 0} (a_nb_0 + a_{n-1}b_1 + a_{n-2}b_2 + \dotsb + a_0b_n)x^n=\\
= \sum_{n\ge0}\left(\sum_{k=0}^n a_k b_{n-k}\right)x^n
$$

---

## Liczebność w zbiorach $(n+m)$–elementowych

Mając
$$
(1 + x)^n = \sum_{k=0}^n x^k \binom{n}{k}\\
(1 + x)^m = \sum_{k=0}^n x^k \binom{m}{k}
$$
możemy obliczyć
$$
(1 + x)^n \cdot (1 + x)^m = \sum_{k=0}^n\left( \sum_{j=0}^k \binom{n}{j}\binom{m}{k-j} \right)x^k
$$

Przez to, że
$$
(1 + x)^{n+m} = \sum_{k=0}^n \binom{n+m}{k}x^k
$$
wówczas
$$
\binom{n+m}{k} = \sum{j=0}^k \binom{n}{j}\binom{m}{k-j}
$$

---

## Funkcje dwóch zmiennych

$$
f(x,y) = \frac{1}{1-y(1+x)} = \frac{1}{1-y}\sum_{n\ge0}\left(\frac{xy}{1-y}\right)^n = \sum_{n\ge0}x^n\frac{y^n}{(1-y)^{n+1}}
$$

$$
f(x,y) = \sum_{n\ge0}(y(1+x))^n = \sum_{n\ge0} y^n (1+x)^n = \sum_{n\ge0}y^n\left( \sum_{k=0}^n \binom{n}{k} x^k \right) =\\
\sum_{n\ge0}\sum_{k\ge0}\binom{n}{k} x^k y^n
$$

---

### Fakt#1

$$
\frac{y^k}{(1-y)^{k+1}} = \sum_{n\ge0} \binom{n}{k} y^n
$$

---

## Fakt#2

$$
\frac{\bold{y^k}}{(1-y)^{k+1}} = \sum_{n\ge k} \binom{n}{k} y^n = (*)
$$
podstawiamy $n = k+a$ przy czym $a \ge 0$.
$$
(*) = \sum_{a\ge 0} \binom{k+a}{k} y^{k+a} = \bold{y^k} \sum_{a \le 0} \binom{k+a}{k} y^a
$$

Skracając $\bold{y^k}$ po obu stronach otrzymujemy:
$$
\sum_{a\ge 0} \binom{k+a}{k}y^2 = \frac{1}{(1-y)^{k+1}}
$$

---
