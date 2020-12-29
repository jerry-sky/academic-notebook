---
lang: 'pl'
title: 'Lista-5'
author: 'Jerry Sky'
---

---

- [Zadanie 1](#zadanie-1)
- [Zadanie 2](#zadanie-2)
- [Zadanie 3](#zadanie-3)

---

W pliku `test-graph.txt` znajduje się podstawowy graf do testów zadań [2](#zadanie-2) i [3](#zadanie-3).

## Zadanie 1

> Napisz program, który symuluje działanie kolejki priorytetowej. Struktura powinna umożliwiać przechowywanie wartości typu `int` wraz z ich priorytetem, będącym nieujemną liczbą całkowitą przy czym najwyższym priorytetem jest wartość $0$. Program nie powinien wymagać żadnych parametrów uruchomienia, a na standardowym wejściu przyjmuje dodatnią liczbę całkowitą $M$ (liczba operacji), a następnie (w liniach $2$–$(M + 1)$) jedną z operacji:
>
> - `insert` $x$ $p$ - wstaw do struktury wartość $x$ o priorytecie $p$
> - `empty` - wypisz wartość $1$ dla pustej struktury, wartość $0$ w p.p.
> - `top` - wypisz wartość o najwyższym priorytecie lub pustą linię w przypadku braku elementów w strukturze
> - `pop` - wypisz wartość o najwyższym priorytecie a następnie usuń ją ze struktury (wypisz pustą linię w przypadku braku elementów w strukturze)
> - `priority` $x$ $p$ - dla każdego elementu o wartości $x$ obecnego w strukturze ustawia priorytet $p$ jeśli jest on wyższy od aktualnego priorytetu danego elementu
> - `print` - wypisuje w jednej linii zawartość struktury w postaci $(x_i, p_i)$, gdzie $x_i$ to kolejne wartości przechowywane w kolejce a $p_i$ odpowiadające im priorytety.
>
> Dla liczby elementów w kolejce $n$, koszt operacji musi wynosić $O(log n)$, dla wszystkich poleceń z pominięciem `print`.

[kod](priority_queue.py)

Aby uruchomić program należy wykonać `./priority_queue.py`.

## Zadanie 2

> Korzystając ze struktury zaimplementowanej w [zadaniu 1](#zadanie-1) lub kopca Fibonacciego, zaimplementuj program realizujący algorytm Dijkstry, dla podanego grafu skierowanego $G = (V,E)$, znajdujący najkrótsze ścieżki z wybranego wierzchołka $v \in V$ do każdego $\overline{v} \in V$.\
> Program nie powinien wymagać żadnych parametrów uruchomienia. Po uruchomieniu programu, na standardowym wejściu, podajemy definicję grafu $G$ oraz wierzchołek startowy $v$. Kolejno wczytywane są:
>
> - liczba wierzchołków $n = |V|$ (przyjmijmy, że wierzchołki są etykietowane kolejnymi liczbami naturalnymi $\{0,\dots,n-1\}$)
> - liczba krawędzi $m = |E|$ (krawędzie są postaci $(u,v,w)$, gdzie $u$ to źródło krawędzi, $v$ jest wierzchołkiem docelowym a $w$ wagą krawędzi – zakładamy, że wagi są nieujemnymi liczbami rzeczywistymi, ale niekoniecznie spełniona jest nierówność trójkąta, ponadto przyjmujemy iż ścieżka z $u$ do $u$ zawsze istnieje i ma koszt $0$)
> - kolejno $m$ definicji krawędzi w postaci `u v w`
> - etykieta wierzchołka startowego
>
> Na standardowym wyjściu powinno zostać $n$ linii, w formacie `id_celu waga_drogi`, natomiast na standardowym wyjściu błędów powinny być wypisane dokładne ścieżki (tzn. wierzchołki pośrednie i wagi) do każdego z wierzchołków docelowych oraz czas działania programu w milisekundach.

[kod](dijkstra.py)

Aby uruchomić program należy wykonać `./dijkstra.py <test-graph.txt` dla przykładowego grafu.

## Zadanie 3

> Korzystając ze struktury z [zadania 1](#zadanie-1) zaimplementuj algorytmy znajdujące dla podanego grafu nieskierowanego $G = (V,E)$ minimalne drzewa rozpinające.
>
> Program powinien umożliwiać wykonanie algorytmu Prima (parametr uruchomienia `-p`) oraz algorytmu Kruskala (parametr uruchomienia `-k`). Niezależnie od parametru uruchomienia, dane wejściowe przyjmują postać:
>
> - liczba wierzchołków $n = |V|$ (przyjmujemy, że wierzchołki są etykietowane kolejnymi liczbami naturalnymi $\{0,\dots,n-1\}$)
> - liczba krawędzi $m = |E|$ (krawędzie są postaci $(u,v,w)$, gdzie $u$ to źródło krawędzi, $v$ jest wierzchołkiem docelowym a $w$ wagą krawędzi – zakładamy, że wagi są nieujemnymi liczbami rzeczywistymi, ale niekoniecznie spełniona jest nierówność trójkąta, ponadto przyjmujemy iż ścieżka z $u$ do $u$ zawsze istnieje i ma koszt $0$ oraz $\forall_{u,v}~(u,v,w) \iff (v,u,w)$, ponadto przyjmujemy, że graf jest spójny)
> - kolejno $m$ definicji krawędzi w postaci `u v w`
>
> Na standardowym wyjściu powinny zostać wypisane, w kolejnych liniach krawędzie `u v w` użyte w drzewie rozpinającym (przyjmujemy, że $u < v$) oraz łączną wagę drzewa rozpinającego.

[kod](msts.py)

Aby uruchomić program należy wykonać `./msts.py <test-graph.txt` dla przykładowego grafu.
