---
lang: 'pl'
title: 'Lista 6'
author: 'Jerry Sky'
---

---

- [Zadanie 2.](#zadanie-2)
    - [Zbiory $\operatorname{LEADING}$ oraz $\operatorname{TRAILING}$](#zbiory-operatornameleading-oraz-operatornametrailing)
    - [Obliczanie relacji $\lessdot$, $\doteq$ oraz $\gtrdot$](#obliczanie-relacji-lessdot-doteq-oraz-gtrdot)
    - [Implementacja](#implementacja)

---

## Zadanie 2.

> Jak wyglądałaby tablica priorytetów obliczona algorytmem dla gramatyki
> $$
> E \to E + E | E - E | E * E | E / E | id
> $$

*«Gramatyki operatorowe»*

### Zbiory $\operatorname{LEADING}$ oraz $\operatorname{TRAILING}$

Standardowy algorytm dla danej produkcji $A$ (pierwsze terminale wyprowadzane z $A$):
1. $a \in \operatorname{LEADING}(A)$ jeśli mamy produkcję $A \to B a \beta$ lub $A \to a \beta$.
2. Jeśli istnieje produkcja $A \to B \alpha$ oraz $a \in \operatorname{LEADING}(B)$ to $a \in \operatorname{LEADING}(A)$.
3. Dla wszystkich terminali wykonujemy powyższe podpunkty do momentu, kiedy nic się nie zmienia.

Analogicznie dla $\operatorname{TRAILING}(A)$ (ostatnie terminale wyprowadzane z $A$).

---

### Obliczanie relacji $\lessdot$, $\doteq$ oraz $\gtrdot$

Standardowy algorytm:\
Dla każdej produkcji $A \to x_1 \dots x_k$:
1. Jeśli $x_i$ i $x_{i+1}$ są terminalami, to $x_i \doteq x_{i+1}$.
2. Jeśli $x_i$ i $x_{i+2}$ są terminalami a $x_{i+1}$ nieterminalem, to $x_i \doteq x_{i+2}$
3. Jeśli $x_i$ jest terminalem a $x_{i+1}$ nieterminalem to dla każdego $a \in \operatorname{LEADING}(x_{i+1})$ mamy $x_i \lessdot a$.
4. Jeśli $x_i$ jest nieterminalem a $x_{i+1}$ terminalem to dla każdego $a \in \operatorname{TRAILING}(x_i)$ mamy $a \gtrdot x_{i+1}$.

Widać już, że w naszym przypadku krok 3. i 4. będą generować przeciwne sobie reguły, jako, że mamy tylko jeden nieterminal $E$.

---

### Implementacja

W gramatyce jest tylko jeden nieterminal $E$, więc stosując [powyższe algorytmy na $\operatorname{LEADING}$ oraz $\operatorname{TRAILING}$](#zbiory-operatornameleading-oraz-operatornametrailing) mamy:
- $\operatorname{LEADING}(E) = \{+, -, *, /, id\}$,
- $\operatorname{TRAILING}(E) = \{+, -, *, /, id\}$.

Brak sprecyzowanego pierwszeństwa prowadzi do konfliktów w tabelce.

Przykład: „$+$”:
- Mamy produkcję $E \to \underbrace{E}_{x_1} \underbrace{+}_{x_2} \underbrace{E}_{x_3}$.

- Z punktu 4. [algorytmu](#obliczanie-relacji-lessdot-doteq-oraz-gtrdot) mamy $x_1$ będący jedynym nieterminalem oraz $x_2$ będący terminalem;\
    czyli dla każdego elementu ze zbioru $\operatorname{TRAILING}(E)$ (dla wszystkich operatorów) zachodzi relacja $\gtrdot$ względem terminalu „$+$”.

- Ale jednocześnie z punktu 3. mamy $x_2$ będący terminalem oraz $x_3$ będący jedynym nieterminalem;\
    czyli dla każdego elementu ze zbioru $\operatorname{LEADING}(E)$ (dla wszystkich operatorów) zachodzi relacja $\lessdot$ względem terminalu „$+$”.


|      |        $+$         |        $-$         |        $*$         |        $/$         |    $id$    |   $\$$    |
| ---: | :----------------: | :----------------: | :----------------: | :----------------: | :--------: | :-------: |
|  $+$ | $\gtrdot \lessdot$ | $\lessdot \gtrdot$ | $\lessdot \gtrdot$ | $\lessdot \gtrdot$ | $\lessdot$ | $\gtrdot$ |
|  $-$ | $\gtrdot \lessdot$ | $\lessdot \gtrdot$ | $\lessdot \gtrdot$ | $\lessdot \gtrdot$ | $\lessdot$ | $\gtrdot$ |
|  $*$ | $\gtrdot \lessdot$ | $\lessdot \gtrdot$ | $\lessdot \gtrdot$ | $\lessdot \gtrdot$ | $\lessdot$ | $\gtrdot$ |
|  $/$ | $\gtrdot \lessdot$ | $\lessdot \gtrdot$ | $\lessdot \gtrdot$ | $\lessdot \gtrdot$ | $\lessdot$ | $\gtrdot$ |
| $id$ |     $\gtrdot$      |     $\gtrdot$      |     $\gtrdot$      |     $\gtrdot$      |            | $\gtrdot$ |
| $\$$ |     $\lessdot$     |     $\lessdot$     |     $\lessdot$     |     $\lessdot$     | $\lessdot$ |



---

