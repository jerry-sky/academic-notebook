---
lang: 'pl'
title: 'Kolorowanie I'
author: 'Jerry Sky'
---

---

- [Def Kolorowanie grafu](#def-kolorowanie-grafu)
- [Def Właściwe kolorowanie grafu](#def-właściwe-kolorowanie-grafu)
- [Def Liczba chromatyczna](#def-liczba-chromatyczna)
    - [Przykłady (liczba chromatyczna)](#przykłady-liczba-chromatyczna)
- [Fakt #1](#fakt-1)
    - [D-d Faktu #1](#d-d-faktu-1)
- [Zachłanne kolorowanie *(Greedy Colouring)*](#zachłanne-kolorowanie-greedy-colouring)
- [Def Graf $k$-zdegenerowany](#def-graf-k-zdegenerowany)
    - [Przykład (graf $k$–zdegenerowany)](#przykład-graf-kzdegenerowany)
    - [Obserwacja #1](#obserwacja-1)
- [Twierdzenie #1](#twierdzenie-1)
    - [D-d Twierdzenia #1](#d-d-twierdzenia-1)
- [Twierdzenie #2](#twierdzenie-2)
    - [Wniosek #1](#wniosek-1)
        - [D-d (Wniosek #1)](#d-d-wniosek-1)
    - [Przykład #2](#przykład-2)
- [Twierdzenie #3](#twierdzenie-3)
- [D-d Twierdzenia #3](#d-d-twierdzenia-3)
    - [Wniosek #2](#wniosek-2)

---

## Def Kolorowanie grafu

Mamy $G = (V,E)$.

Kolorowaniem grafu nazywamy funkcję $f: V \to \mathbb{N}^+$

## Def Właściwe kolorowanie grafu

Mamy $G = (V,E)$.

Właściwym kolorowaniem grafu nazywamy funkcję $f: V \to \mathbb{N}^+$ taką, że $(\forall x,y \in V)(\{x,y\} \in E \to c(x) \neq c(y))$

*Uwaga: będziemy się zajmować tylko grafami prostymi (wielokrotność krawędzi nie ma znaczenia; graf nie może mieć pętli).*

## Def Liczba chromatyczna

$\mathcal{X}(G) = \min \{ k \in \mathbb{N}: \text{ istnieje właściwe kolorowanie grafu } G \text{ elementami } \{1,2,\dots,k\} \}$.

### Przykłady (liczba chromatyczna)

- $\mathcal{X}(K_n) = n$
- $\mathcal{X}(C_{2n}) = 2$
- $\mathcal{X}(C_{2n+1}) = 3$
- $\mathcal{X}(K_{m,n}) = 2$

## Fakt #1

$\mathcal{X}((V, E_1 \cup E_2)) \le \mathcal{X}((V,E_1)) \mathcal{X}((V,E_2))$

### D-d Faktu #1

Bierzemy kolorowanie $c_i$ grafów $(V,E_i)$ ($i=1,2$) i kładziemy $c(x) = (c_1(x),c_2(x))$

## Zachłanne kolorowanie *(Greedy Colouring)*

Mamy częściowe kolorowanie $c$ czyli funkcję $c$ taką, że $\mathcal{domain}(c) \subseteq V$ oraz mamy ciąg $x_1,\dots,x_k$ wierzchołków taki, że $\{ x_1, \dots, x_k \} \cap \mathrm{domain}(c) = \emptyset$.

Input: $(c; x_1,x_2, \dots, x_k)$

1. `for` $i = 1 \dots k$
   1. $f := \min ( \mathbb{N}^+ \setminus \{ c(y): \{x,y\} \in E \land y \in \mathrm{domain}(c) \} )$
   2. $c := c \cup \{ (x_i,f) \}$
2. `return` $c$

## Def Graf $k$-zdegenerowany

Graf jest zdegenerowany jeśli dla dowolnego niepustego podzbioru $X \subseteq V$ istnieje $x \in X$ taki, że $\deg_{G[X]}(x) \le k$.

### Przykład (graf $k$–zdegenerowany)

Każde drzewo jest $1$–zdegenerowanym grafem (każde drzewo ma liść, czyli wierzchołek o rzędzie $1$).

### Obserwacja #1

**Każdy graf $G$ jest $\Delta(G)$–zdegenerowany.**

## Twierdzenie #1
Graf jest $k$-zdegenerowany iff, gdy istnieje takie uporządkowanie $(v_1,\dots,v_n)$ (wszystkich) wierzchołków takie, że
$$
(\forall i)(|\{ j<iL \{v_j,v_i\} \in E \}| \le k)
$$

### D-d Twierdzenia #1

„$\implies$”:\
Indukcja po liczbie wierzchołków; wybieramy $v_n \in V$ taki, że $\deg_G(x) \le k$; założenie indukcyjne stosujemy do $V \setminus \{v_n\}$.

„$\impliedby$”:\
Bierzemy ciąg $(v_1,\dots,v_n)$ spełniający powyższy warunek. Rozważamy $X \subseteq V$. Bierzemy $x = v_i \in X$ taki, że jeśli $v_j \in X$ to $j \le i$ (czyli: wybieramy element zbioru $X$ o największym indeksie w rozważanym ciągu).

## Twierdzenie #2
Jeśli graf $G$ jest $k$–zdegenerowany i $(v_1,\dots,v_n)$ jest takim uporządkowaniem wierzchołków, które spełnia warunek z [ostatniego twierdzenia](#twierdzenie-1), to [algorytm Greedy Colouring](#zachłanne-kolorowanie-greedy-colouring) dla $(\emptyset;x_1,\dots,x_n)$ zwraca właściwe $k+1$–kolorowanie grafu $G$.

### Wniosek #1

Dla dowolnego grafu $G$ mamy $\mathcal{X}(G) \le \Delta(G) + 1$.\
*Uwaga: możemy to pokazać w prosty sposób metodą indukcji matematycznej względem liczby wierzchołków; wprowadziliśmy go przy pomocy zdegenerowania grafu gdyż pojęcie to przyda się nam w dalszych rozważaniach.*

#### D-d (Wniosek #1)

Indukcja po liczbie $k = |V|$. Dla $k=1$ mamy $\mathcal{X}(G) = 1$ oraz $\Delta(G) + 1 = 0 + 1 = 1$.\
Zakładamy teraz, że $k>1$ oraz, że twierdzenie jest prawdziwe dla $G$ taki, że $|V(G)| < k$. Bierzemy graf $G$ taki, że $|V(G)| = k$. Bierzemy dowolny wierzchołek $v \in V$. Graf $G' = G[V \setminus \{v\}]$ ma $k-1$ wierzchołków. Co więcej $\Delta(G') \le \Delta(G)$. Mamy więc (założenie indukcyjne) właściwe kolorowanie $c': V(G') \to \{1,\dots,\Delta(G)+1\}$. Zbiór $\mathcal{N}(v)$ ma moc nie większą niż $\Delta(G)$. Zatem
$$
\{1,\dots,\Delta(G)+1\} \setminus \{ c(x): x\in \mathcal{N}(v) \neq \emptyset \}.
$$
Bierzemy dowolny element $a$ z tego zbioru i rozszerzamy kolorowanie $c'$:
$$
c = c' \cup \{(v,a)\}.
$$
To jest właściwe kolorowanie grafu $G$ za pomocą $\Delta(G) + 1$ kolorów.

### Przykład #2
Każde drzewo jest $2$–kolorowalne (czyli jeśli $T$ jest drzewem, to $\mathcal{X}(T) = 2$)

## Twierdzenie #3
Każdy graf planarny jest $5$–zdegenerowany.

## D-d Twierdzenia #3

Na [jednym z poprzednich wykładów](../2020-04-01/2020-04-01.md#texttwierdzenie-1) pokazaliśmy, że w każdym grafie planarnym istnieje wierzchołek o rzędzie nie większym niż $5$. Ponadto, pod-graf grafu planarnego jest planarny, więc ma wierzchołek rzędu $\le 5$.

### Wniosek #2

**Każdy graf planarny jest $\bold6$–kolorowalny**
