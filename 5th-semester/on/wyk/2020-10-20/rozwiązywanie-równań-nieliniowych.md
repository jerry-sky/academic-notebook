# Rozwiązywanie równań nieliniowych

*(2020-10-20)*

- [1. Problem](#1-problem)
- [2. Podejście](#2-podejście)
- [3. Metody](#3-metody)

---

## 1. Problem

Dana jest funkcja $f: \mathbb{R} \to \mathbb{R}$ (np.: $f(x) = x - \tg(x)$).\
Szukamy takie $r \in \mathbb{R}$, dla którego
$$
f(r) = 0.
$$

## 2. Podejście

Będziemy rozważać *metody iteracyjne*. Metody te konstruują ciąg przybliżeń $x_0, x_1, x_2, \dots$ według reguły
$$
x_{n+1} := \Phi(x_n)
$$
taki, że
$$
\lim_{n\to \infty} x_n = r
$$

Mówimy o metodzie, że jest *zbieżna globalnie*, jeśli konstruowany ciąg przybliżeń $\{ x_n \}$ jest zbieżny do $r$ przy dowolnych przybliżeniach początkowych.

---

## 3. Metody

1. [Metoda bisekcji](metoda-bisekcji.md)
2. [Metoda Newtona](metoda-newtona.md)
3. [Metoda siecznych](metoda-siecznych.md)

| metoda    |     | zbieżność | wykładnik $\alpha$                     | uwagi                        |
| --------- | --- | --------- | -------------------------------------- | ---------------------------- |
| bisekcji  |     | globalna  | $1$                                    | stosować hybrydowo           |
| Newtona   |     | lokalna   | $2$                                    | konieczność liczenia $f'(x)$ |
| siecznych |     | lokalna   | $\frac{1 + \sqrt{5}}{2} \approx 1.618$ |                              |

---
