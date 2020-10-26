# Metoda bisekcji

*(2020-10-22)*

- [1. Metoda bisekcji (połowienia)](#1-metoda-bisekcji-połowienia)
- [2. Algorytm](#2-algorytm)
- [3. Twierdzenie o zbieżności metody bisekcji](#3-twierdzenie-o-zbieżności-metody-bisekcji)
    - [3.1. D-d](#31-d-d)
    - [3.2. Przykład](#32-przykład)

---

## 1. Metoda bisekcji (połowienia)

Założenia:
- $f$ jest funkcją ciągłą w $[a;b]$
- $f(a) \cdot f(b) < 0$ ($f$ zmienia znak)

![](metoda-bisekcji.png)

$$
c_n = \frac{1}{2} (a_n + b_n) \quad (n\ge 0)
$$

Warunek końca: $|b_n - a_n| \le \delta$, $|f(c_n)| \le \epsilon$

## 2. Algorytm

- *Dane: $a,b,M, \delta, \epsilon$*
- *Wyniki $k, \tilde{r}, f(\tilde{r})$*

1. $u \gets f(a)$
2. $v \gets f(b)$
3. $e \gets b - a$
4. `if` $\operatorname{sgn}(u) = \operatorname{sgn}(v)$:
    1. `return error`
5. `for` $k \gets 1$ `to` $M$:
    1. $e \gets \frac{e}{2}$
    2. $c \gets a + e$
    3. $w \gets f(c)$
    4. `if` $|e| < \delta$ `or` $|w| < \epsilon$:
        1. `return` $k,c,w$
    5. `if` $\operatorname{sgn}(w) \neq \operatorname{u}$:
        1. $b \gets c$
        2. $v \gets w$
    6. `else`
        1. $a \gets c$
        2. $u \gets w$

---

## 3. Twierdzenie o zbieżności metody bisekcji

Niech $[a_0, b_0]; [a_1, b_2]; \dots; [a_n, b_n]; \dots$ będzie ciągiem przedziałów konstruowanych przez metodę bisekcji. Wówczas istnieją granice $\lim_{n \to \infty} a_n$ oraz $\lim_{n \to \infty} b_n$ i są sobie równe, reprezentujące zero $r$ funkcji $f$.

Jeśli $r = \lim_{n \to \infty} c_n$ oraz $c_n = \frac{1}{2}(a_n + b_n)$, wówczas
$$
|r - c_n| \le 2^{-(n+1)} (b_0 - a_0).
$$

### 3.1. D-d

Końce generowanych przedziałów spełniają zależności
$$
a_0 \le a_1 \le a_2 \le \dotsb \le b_0\\
b_0 \ge b_1 \ge b_2 \ge \dotsb \ge a_0\\
$$

$$
b_n - a_n = \frac{1}{2}(b_{n-1} - a_{n-1}) = 2^{-n} (b_0 - a_0)
$$

Ponieważ ciąg $\{ a_n \}$ (odp. $\{ b_n \}$) jest rosnący (odp. malejący) i ograniczony z góry (odp. dołu), więc zbieżny.\
Zatem
$$
\lim_{n \to \infty} b_n - \lim_{n \to \infty} a_n = \lim_{n \to \infty} 2^{-n} (b_0 - a_0) = 0
$$

Stąd $\lim_{n \to \infty} b_n = \lim_{n \to \infty} a_n = r$. Przechodząc do granicy w nierówności $0 \ge f(a_n) \cdot f(b_n)$, otrzymujemy $0 \ge \left( f(r) \right)^2$. Co implikuje $f(r) = 0$ (zbieżność).\
Niech $[a_n, b_n]$ będzie przedziałem wygenerowanym przez metodę bisekcji. Jeśli warunek końca jest już spełniony, oczywiście $r \in [a_n, b_n]$, wówczas najlepszym przybliżeniem pierwiastka $r$ jest środek przedziału $c_n = \frac{a_n + b_n}{2}$.\
Błąd możemy oszacować następująco:
$$
|r - c_n| \le \frac{1}{2} (b_n - a_n) = 2^{-(n+1)} (b_0 - a_0) \quad \blacksquare
$$

---

### 3.2. Przykład

Niech $[50, 63]$ będzie przedziałem, w którym $f$ ma pierwiastek.\
*Jaka jest liczba iteracji metody bisekcji, aby wyznaczyć pierwiastek z błędem względnym $10^{-12}$?*
$$
\frac{|r - c_n|}{|r|} \le \frac{|r - c_n|}{50} \le 2^{-(n+1)} \frac{13}{50} \le 10^{-12}
$$

Rozwiązując powyższą nierówność otrzymujemy $n \ge 37$.

---
