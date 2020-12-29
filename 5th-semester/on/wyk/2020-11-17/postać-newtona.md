---
lang: 'pl'
title: 'Postać Newtona wzoru interpolacyjnego'
author: 'Jerry Sky'
date: '2020-11-17'
---

---

- [Postać Newtona](#postać-newtona)

---

## Postać Newtona
$$
p_n(x) = \sum_{k=0}^n c_k q_k(x) = \sum_{k=0}^n f[x_0, x_1, \dots, x_k] \prod_{j=0}^{k-1} (x - x_j).
$$

Współczynniki $c_0 = f[x_0],\, c_1 = f[x_0, x_1],\, \dots,\, c_n = f[x_0, x_1, \dots, x_n]$ wyznaczamy, konstruując tablicę trójkątną ilorazów różnicowych. Konstrukcja wielomianu interpolacyjnego $p_{n+1}(x)$:
$$
\begin{aligned}
    p_n(x_i) &= y_i \qquad (0 \le i \le n)\\
    p_{n+1}(x_i) &= y_i \qquad (0 \le i \le n+1)
\end{aligned}
$$

Wielomian $p_{n+1}(x)$ można przedstawić w postaci
$$
p_{n+1}(x) = p_n(x) + c_{n+1}(x - x_0) \dotsb (x - x_n).
$$

Zatem wyznaczenie $p_{n+1}(x)$ na podstawie $p_n(x)$ wymaga wyznaczenia $c_{n+1} = f[x_0, \dots, x_{n+1}]$ (lokalna modyfikacja).

---
