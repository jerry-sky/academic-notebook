# IEEE-754

*(2020-10-06)*

---

## 1. Reprezentacja liczby rzeczywistej w IEEE-754

Liczbę rzeczywistą $x \neq 0$, zgodnie ze standardem IEEE-754 zapiszemy:
$$
x = \plusmn m\cdot 2^c = \plusmn (1.f)_2 \cdot 2^c = \plusmn (1.a_1,a_2,\dots) \cdot 2^c
$$
gdzie
- $m \in [1; 2)$, $f$ jest częścią ułamkową mantysy, $(f)_2 < 1$
- $c \in \mathbb{Z}$
- $\forall i \enspace a_i \in \{0,1\}$

Niech
- $t-1$ będzie liczbą bitów przeznaczoną na zapisanie $f$
- $d$ będzie liczbą bitów przeznaczoną na zapisanie cechy $c$
- $c \in [-2^{d-1} + 1; 2^{d-1}]$

---

### 1.1. Cecha

Stosowany jest kod z nadmiarem w zapisie $c$:
$$
c_{KN} = c + \mathrm{bias} = c + 2^{d-1} - 1
$$
stąd
$$
0 \le c_{KN} \le 2^d - 1\\
c = c_{KN} - \mathrm{bias}
$$

![schemat formatu ieee754](format-ieee-754.png)

---

### 1.2. Wartości brzegowe
- $c_{KN}$:
    - $0$
    - $2^d - 1$

$1 \le c_{KN} \le 2^d - 2$, ponieważ $c = c_{KN} - \mathrm{bias} = c_{KN} - (2^{d-1} - 1)$

Ostatecznie rzeczywisty zakres cechy jest następujący:
$$
c_{\min} = -2^{d-1} + 2 \le c \le 2^{d-1} - 1 = c_{\max}
$$

$\mathrm{MIN}_{sub} = 2^{-(t-1)} \cdot 2^{c_{\min}} < \mathrm{MIN}_{nor} = 2^{c_{\min}} \le |rd(x)| \le (2 - 2^{-(t-1)}) \cdot 2^{c_{\max}} = \mathrm{MAX}$

---

Niech $x^- = m_{t-1}^- 2^c$ oraz $x^+ = m^+_{t-1} 2^c$ będą sąsiadującymi liczbami maszynowymi. Wówczas:
$$
x^+ = (m^-_{t-1} + 2^{-(t-1)})2^c, \qquad x^- = m_{t-1}^- 2^c
$$
$$
|x^+ - x^-| = 2^{-(t-1)}2^c = 2^{c - (t-1)}
$$

$$
|\delta| = \frac{|rd(x) - x|}{|x|} \le \frac{1}{2} \frac{|x^+ - x^-|}{|x|} = \frac{1}{2}\frac{2^{c-(t-1)}}{|m_x 2^c|} \le \frac{1}{2} \frac{2^{-(t-1)}}{1} = 2^{-t} = \epsilon
$$

| format   | d    | t    | $\mathrm{MIN}_{sub}$  | $\mathrm{MIN}_{nor}$  | $\mathrm{MAX}$       | $\epsilon = 2^{-t}$   |
| -------- | ---- | ---- | --------------------- | --------------------- | -------------------- | --------------------- |
| `single` | $8$  | $24$ | $1.4 \cdot 10^{-45}$  | $1.2 \cdot 10^{-38}$  | $3.4 \cdot 10^{38}$  | $5.96 \cdot 10^{-8}$  |
| `double` | $11$ | $53$ | $4.9 \cdot 10^{-324}$ | $2.2 \cdot 10^{-308}$ | $1.8 \cdot 10^{308}$ | $1.11 \cdot 10^{-16}$ |

---

### 1.3. Przykład

Wyznacz reprezentację $x = \frac{2}{3}$ w formacie `single` ($t-1 = 23,~ d = 8$).

$$
\frac{2}{3} = (0.10101010\dots)_2 \approx (1.0101010\dots11)_2 \cdot 2^{-1}
$$

$c = -1,~ c_{KN} = c + \mathrm{bias} = c + 127; \quad c_{KN} = 126 = (01111110)_2$

$$
\frac{2}{3} \approx [0 ~|~ 01111110 ~|~ 01010101010101010101011 ]
$$

*Julia lang*: `bitstring(Float32(2/3))`

---

## 2. Symbole specjalne

(*w nawiasach podane są wielkości w formacie `single`*)

### 2.1. Zera
$c_{KN} = 0, f = 0$

- $+0 \enspace ([0 ~|~ 00000000 ~|~ 00000000000000000000000])$
- $-0 \enspace ([1 ~|~ 00000000 ~|~ 00000000000000000000000])$
- $-0$ lub $+0$ jest w szczególności skutkiem niedomiaru ($|x| < 2^{-23} \cdot 2^{-126} - \mathrm{MIN}_{sub}$)

### 2.2. Nieskończoności

- $+\infty ([0 ~|~ 11111111 ~|~ 00000000000000000000000])$
- $-\infty ([1 ~|~ 11111111 ~|~ 00000000000000000000000])$
- $+\infty$ jeśli wystąpił nadmiar, $x + \infty = +\infty$, $x \cdot \infty = +\infty$, $\frac{\infty}{x} = +\infty$ dla $x > 0$

### 2.3. `NaN`
($c_{KN} = 255,~ f \neq 0$)

($[0 ~|~ 11111111 | 10000000000000000000000]$)

`NaN` pojawia się w sytuacjach:
- $\frac{0}{0}$
- $\infty - \infty$
- `NaN` $+ x$

### 2.4. Liczby denormalizowane
$x \in (-\mathrm{MIN}_{nor};~-\mathrm{MIN}_{sub}] \cup [\mathrm{MIN}_{sub};~ \mathrm{MIN}_{nor})$

($c_{KN} = 0,~ f \neq 0$)

- $x = 2^{-23} \cdot 2^{-126} \quad ([0 ~|~ 00000000 ~|~ 00000000000000000000001])$
- $x = -2^{-23} \cdot 2^{-126} \quad ([1 ~|~ 00000000 ~|~ 00000000000000000000001])$

---

## 3. Zaokrąglenie (Przykład)

Rozważamy arytmetykę `single`.

$$
x = (1 + 2^{-24}) \cdot 2^0
$$

Sąsiednie liczby maszynowe
- $x^- = 1$
- $x^+ = (1 + 2^{-23}) \cdot 2^0$
- $x \in (x^-;~ x^+)$
- $|x^+ - x^-| = 2^{-23}$
- $|x^+ - x| = 2^{-24}$
- $|x - x^-| = 2^{-24}$

$$
\begin{aligned}
    x^- & = 1 \cdot 2^0 \quad ([0 ~|~ 01111111 ~|~ 00000000000000000000000])\\
    x & = (1 + 2^{-24}) \cdot 2^0 \quad ([0 ~|~ 01111111 ~|~ 00000000000000000000000 ~|~ \bold{1}00 \dots])\\
    x^+ & = (1 + 2^{-23}) \cdot 2^0 \quad ([0 ~|~ 01111111 ~|~ 0000000000000000000000\bold{1}])
\end{aligned}
$$

$rd(x) = x^- = 1$

---
