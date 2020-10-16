# Numeryczna reprezentacja liczb
*(2020-10-06)*

- [1. Postać znormalizowana](#1-postać-znormalizowana)
    - [1.1. Przykłady](#11-przykłady)
- [2. Arytmetyka zmiennopozycyjna (*fl*)](#2-arytmetyka-zmiennopozycyjna-fl)
- [3. Zaokrąglenie i obcięcie](#3-zaokrąglenie-i-obcięcie)
    - [3.1. Przykład — zaokrąglenie dla baz $2$ i $10$](#31-przykład--zaokrąglenie-dla-baz-2-i-10)
    - [3.2. Błąd względny i precyzja](#32-błąd-względny-i-precyzja)
- [4. *MIN* oraz *MAX*](#4-min-oraz-max)
    - [4.1. Przykład](#41-przykład)
- [5. Przykład reprezentacji liczby](#5-przykład-reprezentacji-liczby)
- [- $t = 6$](#ullit--6liul)

---

## 1. Postać znormalizowana

Każdą liczbę rzeczywistą $x \neq 0$ można zapisać w postaci *znormalizowanej*:
$$
x = \plusmn m \cdot \beta^c = \plusmn(0.a_1,a_2,\dots)_\beta \cdot \beta^c
$$
gdzie:
- $\beta$ jest bazą
- $m \in \left[\frac{1}{\beta};1\right)$ jest mantysą
- $c \in \mathbb{Z}$ jest cechą (rząd wielkości)
- $\forall i ~ a_i \in \{0,1,\dots, \beta-1\},~ a_1 \neq 0$

### 1.1. Przykłady

1. $\beta = 10$\
    $732.5051 = 0.7325051 \cdot 10^3$\
    $-0.005612 = -0.5612 \cdot 10^{-2}$

2. $\beta = 2$\
    $(1001.11101)_2 = (0.100111101)_2 \cdot 2^4$\
    $(0.0010111)_2 = (0.10111)_2 \cdot 2^{-2}$

---

## 2. Arytmetyka zmiennopozycyjna (*fl*)

Bierzemy postać znormalizowaną i narzucamy pewne ograniczenia:
$$
rd(x) = \plusmn m_t \cdot \beta^c = \plusmn (0,a_1,a_2,\dots,a_t)_\beta \cdot \beta^c
$$
gdzie:
- $t$ jest stałą liczbą cyfr mantysy
- cecha $c \in [c_{\min}; c_{\max}] \cap \mathbb{Z}$

Powyższą arytmetykę nazywany **arytmetyką zmiennopozycyjną** (*fl*).

Reprezentacja liczby $x$ w *fl*:
- $rd(x)$
- $\widetilde{x}$

---

## 3. Zaokrąglenie i obcięcie

1. Przedstaw $x$ w postaci $x = \plusmn m \beta^c,~ m\in \left[\frac{1}{\beta}; 1\right)$
2. zaokrąglij mantysę $m$ do najbliższej liczby $t$-cyfrowej (w przypadku obcięcia rozwinięcie mantysy obcinamy po $t$ cyfrach), otrzymując $rd(m)$
3. Podstaw $rd(x) := \plusmn rd(m)\beta^c = \plusmn m_t \beta^c$.

*Zakłada się, że zaokrąglenie jest domyślnym sposobem otrzymania przybliżenia $rd(x)$ liczby $x$.*

### 3.1. Przykład — zaokrąglenie dla baz $2$ i $10$

$$
rd(m) :=
\begin{cases}
    0,a_1,\dots,a_t & \text{jeśli } a_{t+1} \le 4\\
    0,a_1,\dots,a_t + 10^{-t} & \text{jeśli } 5 \le a_{t+1} \le 9
\end{cases}
$$

$$
rd(m) :=
\begin{cases}
    0,a_1,\dots,a_t & \text{jeśli } a_{t+1} = 0\\
    (0,a_1,\dots,a_t)_2 + 2^{-t} & \text{jeśli } a_{t+1} = 1
\end{cases}
$$

### 3.2. Błąd względny i precyzja

Weźmy dwie sąsiadujące niezerowe liczby (liczby maszynowe) $x^- = m_t^- \beta^c$ oraz $x^+ = m_t^+ \beta^c$ przy czym $x^+ = (m_t^- + \beta^{-t})\beta^c$.

Wówczas
$$
|x^+ - x^-| = \beta^{-t} \beta^c = \beta^{c-t}
$$

Oszacujmy więc, błąd względny dla zaokrąglenia:
$$
|\delta| = \frac{|rd(x) - x|}{|x|} \le \frac{1}{2} \frac{|x^+ - x^-|}{|x|} = \frac{1}{2}\frac{\beta^{c-t}}{|m_x \beta^c} \le \frac{1}{2} \frac{\beta^{-t}}{\beta^{-1}} = \frac{1}{2}\beta^{1-t}
$$

gdzie $x^-$, $x$ oraz $x^+$ są sąsiadującymi liczbami.\
*Dla obcięcia $|\delta| \le \beta^{1-t}$.*

---

$|\delta| = \frac{|rd(x) - x|}{|x|}$
lub inaczej
$rd(x) = x(1 + \delta)$, $|\delta| \le \epsilon$, $\epsilon = 0.5\cdot \beta^{1-t}$.

Liczbę $\epsilon$ nazywamy **precyzją arytmetyki**.

---

## 4. *MIN* oraz *MAX*

![](siatka-symetryczna.png)

Z założenia, że $m_t \in \left[\frac{1}{\beta}; 1\right)$ wynika, że w arytmetyce *fl* możemy reprezentować liczby $x$ spełniające zależność:
$$
\mathrm{MIN} = \frac{1}{\beta} \beta^{c_{\min}} \le |X| \le (1 - \beta^{-t}) \beta^{c_{\max}} = \mathrm{MAX}
$$

Jeśli $|x| > \mathrm{MAX}$, to mówimy o *nadmiarze* (mogą być przerwane obliczenia).

Jeśli $|x| < \mathrm{MIN}$, to $rd(x) = 0$ i mówimy o *niedomiarze*. Błąd tej reprezentacji jest równy $100\%$.

---

### 4.1. Przykład

Rozważmy arytmetykę dwójkową ($\beta = 2$), w której:
- 1 bit przeznaczono na zapis znaku $s$ liczby $x$
- 6 bitów przeznaczono na zapis cechy $c$ (wraz z bitem znaku) ($c \in [-31, 32]$)
- 16 bitów przeznaczono na zapis mantysy  ($t = 16$)

wówczas
$$
\mathrm{MIN} = \frac{1}{2}2^{-31} \approx 4.66 \cdot 10^{-10}\\
\mathrm{MAX} = (1 - 2^{-16})2^{32} \approx 4.29 \cdot 10^9
$$

---

## 5. Przykład reprezentacji liczby

- liczba $x = 9.13$ w arytmetyce *fl*
- $\beta = 2$
- $t = 6$
---
$\epsilon = 1.56 \cdot 10^{-2}$

$x = 9.13 = (1001.0010\dots)_2 \overset{\text{normalizacja}}{=} (0.10010010\dots)_2 \cdot 2^4 \overset{\text{zaokrąglenie}}{\longrightarrow} rd(x) = (0.100101)_2 \cdot 2^4$.

$|\delta| = \frac{|rd(x) - x|}{|x|} \approx 1.32 \cdot 10^{-2}$.

---
