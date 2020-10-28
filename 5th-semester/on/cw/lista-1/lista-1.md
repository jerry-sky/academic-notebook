# Lista-1

- [Zadanie 1.](#zadanie-1)
- [Zadanie 2.](#zadanie-2)
    - [2.(a)](#2a)
    - [2.(b)](#2b)
- [Zadanie 4.](#zadanie-4)
- [Zadanie 5.](#zadanie-5)
    - [5.a1.](#5a1)
    - [5.b1.](#5b1)
    - [5.c1.](#5c1)
    - [5.a2.](#5a2)
    - [5.b2.](#5b2)
    - [5.c2.](#5c2)

---

## Zadanie 1.

> Obliczyć sumę poniższych liczb wykonując obliczenia w systemie zmiennopozycyjnym dziesiętnym z dwucyfrową mantysą z zaokrągleniem $(z = \plusmn m_z 10^c,~ m_z \in [0.1;1))$:
> $$
> a_1 = 0.25, \enspace a_2 = 0.0046, \enspace a_3 = 0.00079, \enspace a_4 = 0.061
> $$
> tj. $((\tilde{a}_1 \oplus \tilde{a}_2) \oplus \tilde{a}_3) \oplus \tilde{a}_4$. Powtórzyć obliczenia po uporządkowaniu liczb rosnąco (od najmniejszej do największej). Porównać z sumą dokładną.

Suma po kolei:

1. $\tilde{a}_1 \oplus \tilde{a}_2 = 0.25 \cdot 10^{0} \oplus 0.46 \cdot 10^{-2} = 0.25 \cdot 10^{0} \oplus 0.00 \cdot 10^{0} = 0.25 \cdot 10^{0} = A$
2. $A \oplus \tilde{a}_3 = 0.25 \cdot 10^{0} \oplus 0.79 \cdot 10^{-3} = 0.25 \cdot 10^{0} \oplus 0.00 \cdot 10^{0} = 0.25 \cdot 10^0 = B$
3. $B + \tilde{a}_4 = 0.25 \cdot 10^{0} + 0.61 \cdot 10^{-1} = 0.25 \cdot 10^0 + 0.06 \cdot 10^0 =0.31 \cdot 10^0$

Suma od najmniejszej do największej ($a_3, a_2, a_4, a_1$):

1. $\tilde{a}_3 \oplus \tilde{a}_2 = 0.79 \cdot 10^{-3} \oplus 0.46 \cdot 10^{-2} = 0.08 \cdot 10^{-2} \oplus 0.46 \cdot 10^{-2} = 0.54 \cdot 10^{-2} = C$
2. $C \oplus \tilde{a}_4 = 0.54 \cdot 10^{-2} \oplus 0.61 \cdot 10^{-1} = 0.05 \cdot 10^{-1} \oplus 0.61 \cdot 10^{-1} = 0.66 \cdot 10^{-1} = D$
3. $D \oplus 0.25 \cdot 10^0 = 0.66 \cdot 10^{-1} \oplus 0.25 \cdot 10^0 = 0.07 \cdot 10^0 \oplus 0.25 \cdot 10^0 = 0.32 \cdot 10^0$

Suma zwykła:
$\sum_{i=1}^4 a_i = 0.31639 \cdot 10^0 \approx 0.32 \cdot 10^0$

---

## Zadanie 2.

### 2.(a)

> Niech $x = 0.54617,\enspace y = 0.54601$. Jaka jest reprezentacja liczb $x$ oraz $y$ w arytmetyce zmiennopozycyjnej dziesiętnej z czterocyfrową mantysą z zaokrągleniem? Niech $\tilde{x} = rd(x), \enspace \tilde{y} = rd(y), \enspace r = x-y, \enspace, \tilde{r} = \tilde{x} \circleddash \tilde{y}$. Obliczyć $\frac{| r - \tilde{r} |}{|r|}$. Jaka jest precyzja arytmetyki (błąd reprezentacji) $\epsilon$?

- $x = 0.54617$
- $y = 0.54601$
- $\tilde{x} = 0.5462$
- $\tilde{y} = 0.5460$
- $r = x - y = 0.00016$
- $\tilde{r} = \tilde{x} - \tilde{y} = 0.0002$
- $\frac{|r - \tilde{r}|}{|r|} = \frac{0.00004}{0.00016} = 0.25$
- $\epsilon = \frac{1}{2} \cdot 10^{1-4} = 0.5 \cdot 10^{-3}$

*błąd jest znacznie wyższy niż $\epsilon$*

---

### 2.(b)

> Dana jest arytmetyka zmiennopozycyjna dziesiętna z trzycyfrową mantysą z zaokrągleniem. Niech $\tilde{b} = 3.34, \enspace \tilde{a} = 1.22$ oraz $\tilde{c} = 2.28$. Obliczyć $\tilde{\Delta} = \tilde{b} \odot \tilde{b} \ominus 4\tilde{a} \odot \tilde{c}$ oraz $\frac{|\Delta - \tilde{\Delta}|}{|\Delta|}$. Jaka jest precyzja arytmetyki?

- $\tilde{b} = 3.34 = 0.334 \cdot 10^1$
- $\tilde{a} = 1.22 = 0.122 \cdot 10^1$
- $\tilde{c} = 2.28 = 0.228 \cdot 10^1$

Liczymy:
- $\tilde{\Delta} = \tilde{b} \odot \tilde{b} \ominus 4\cdot \tilde{a} \odot \tilde{c}$
- $\tilde{\Delta} = 0.334 \cdot 10 \odot 0.334 \cdot 10 \ominus 0.228\cdot 10 = 0.112 \cdot 10^2 \ominus 0.111 \cdot 10^2 = 0.001 \cdot 10^2 = 0.1$

Faktyczna wartość $\Delta = 0.0292$.

Czyli mamy błąd $\frac{|\Delta - \tilde{\Delta}}{|\Delta|} = \frac{0.0708}{0.0292} = 0.24246553 \cdot 10$.

Za to $\epsilon = 0.5 \cdot 10^{-2}$.

---

## Zadanie 4.

> Czy poniższe liczby są dokładnie reprezentowane w arytmetyce single zgodną ze standardem *IEEE 754*, w której 1 bit przeznaczono na zapis znaku s liczby x, 8 bitów przeznaczono na zapis cechy $c$ i $23$ bity przeznaczono na zapis części ułamkowej $f$ mantysy ($x = sm2^c,\enspace m \in [1;2),\enspace m = \overline{1.f},\ f<1$, jedynka przed kropką dziesiętną nie jest pamiętana).

- $x = 2^{-1} + 2^{-26}$ — *nie, bo $2^{-26}$ wychodzi poza zakres mantysy, nawet po normalizacji wyniku tego dodawania*

*poniższe liczby mają swoje odpowiednie okresy i ich mantysa będzie nieskończenie długa, więc nie zostaną zapamiętane dokładnie:*
- $y = \frac{1}{3}$
- $z = \frac{1}{5}$
- $w = \frac{1}{10}$

---

## Zadanie 5.

> Niech dane będzie $33$ bitowe słowo, w którym $1$ bit przeznaczono na zapis znaku $s$ liczby $x$, $8$ bitów przeznaczono na zapis cechy $c$ (wraz z bitem znaku) i $24$ bity przeznaczono na zapis mantysy $m$ ($x = sm2^c, m \in [0.5; 1)$).
>
> Wyznaczyć:
> - zakres reprezentowanych liczb,
> - „zero maszynowe”
> - precyzję arytmetyki (błąd reprezentacji) $\epsilon$.
>
> Wyznaczyć również dla arytmetyki `single`.

### 5.a1.

1. Cecha $c \in [-2^7 + 1;\enspace 2^7]$
    1. mamy $2^8$ bitów do zapisania
    2. mamy pewne przesunięcie, *bias*, żeby mieć też możliwość zapisu ujemnych liczb
    3. zakres liczb to $[-127;\enspace 128]$ (taki sam jak w IEEE-754)
2. Mantysa $m \in [0.5;\enspace 1)$.

Zobaczmy liczy ekstremalne:
- $\mathrm{MIN} = m_{\min} \cdot 2^{c_{\min}} = \frac{1}{2} \cdot 2^{-2^7 + 1} = 2^{-128} = \approx 2.938736 \cdot 10^{-39}$
- $\mathrm{MAX} = m_{\max} \cdot 2^{c_{\max}} = (1 - 2^{-24}) \cdot 2^{2^7} = 2^{128} - 2^{104} \approx 3.402823 \cdot 10^{38}$

W takim razie reprezentowalne liczby należą do „podziurawionego” przedziału $[-\mathrm{MAX};\enspace \mathrm{MAX}]$

### 5.b1.

Zero maszynowe to każda liczba $x \in (\mathrm{MIN};\enspace \mathrm{MIN})$, dla takich $x$ zachodzi $rd(x) = 0$.

### 5.c1.

$\epsilon = \frac{1}{2} \cdot \beta^{1-t} = 2^{-24}$

---

### 5.a2.

Różnice:
- zakres cechy $c \in [-2^{7} + 2;\enspace 2^{7} - 1]$ (dla wartości brzegowych tego czego zapisujemy czyli $c_{KN}$ równych $0$ oraz $2^{23-1}$ są zarezerwowane znaki specjalnie $\plusmn0$ oraz $\plusmn\infty$)

- $\mathrm{MIN} = 2^{-23} \cdot 2^{c_{\min}} = 2^{-23 - 2^{7}} \approx 1.4 \cdot 10^{-45}$
- $\mathrm{MAX} = (2 - 2^{-23}) \cdot 2^{c_{\max}} \approx 3.4 \cdot 10^{38}$

### 5.b2.

$x \in (-\mathrm{MIN};\enspace \mathrm{MIN})$

### 5.c2.

$\epsilon = \frac{1}{2} \cdot \beta^{1-t} = 2^{-23}$

---
