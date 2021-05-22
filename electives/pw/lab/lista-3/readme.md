---
lang: 'pl'
title: 'Lista 3.'
subtitle: 'Programowanie współbieżne, Laboratorium'
author: 'Jerry Sky'
---

- [Zadanie](#zadanie)
- [Argumenty](#argumenty)
- [Go](#go)
- [Ada](#ada)

---

## Zadanie

> Zakładamy, że mamy graf $n$ wierzchołków, w którym krawędzie są nieskierowane.
> Krawędź między wierzchołkami $i$ a $j$ oznaczamy: $\{i,j\}$.
> Listę sąsiadów wierzchołka $i$ oznaczamy: $N(i)$.
>
> Podobnie jak w poprzednich zadaniach zakładamy,
> że w grafie istnieje ścieżka Hamiltona złożona z krawędzi postaci $\{v, v+1\}$
> (dzięki czemu graf jest spójny),
> oraz pewna liczba $d$ dodatkowych krawędzi (skrótów).
>
> Należy zaimplementować wykonywanie protokołu routingu podobnego do znanego protokołu RIP,
> zgodnie z poniższymi wskazówkami.
>
> - Każdy wierzchołek $i$ zawiera zmienną reprezentującą tzw. routing table (oznaczaną przez $R_i$),
>     która dla każdego wierzchołka $j$, różnego od $i$, zawiera następujące dane:
>     - $R_i[j].\mathrm{nexthop}$ — wierzchołek ze zbioru $N(i)$ (tj. sąsiad $i$) leżący na najkrótszej,
>         znanej wierzchołkowi $i$, ścieżce $p$ od $i$ do $j$, oraz
>     - $R_i[j].\mathrm{cost}$ — długość tej ścieżki $p$.
> - Początkowo każdy wierzchołek $i$ zna swoich bezpośrednich sąsiadów $N(i)$ i wie o istnieniu krawędzi postaci $\{v,v+1\}$.
>     Zatem,
>     - dla $j \in N(i)$, początkowo $R_i[j].\mathrm{cost} = 1$ i $R_i[j].\mathrm{nexthop} = j$, a
>     - dla $j \notin N(i)$, $R_i[j].\mathrm{cost} = |i-j|$ oraz
>         - $R_i[j].\mathrm{nexthop} = i+1$, jeśli $i<j$, albo
>         - $R_i[j].\mathrm{nexthop} = i-1$, jeśli $j<i$.
> - Ponadto, dla każdego $R_i[j]$, istnieje flaga $R_i[j].\mathrm{changed}$ (początkowo ustawiona na `true`).
> - W każdym wierzchołku $i$ działają dwa współbieżne wątki:
>     - $\mathrm{Sender}_i$ oraz
>     - $\mathrm{Receiver}_i$
> - Oba te wątki mają współbieżny dostęp do routing table $R_i$.
>     W Go można zaimplementować $R_i$ jako *stateful goroutine*, a w Adzie jako zmienną *protected*.
> - Co pewien czas $\mathrm{Sender}_i$ budzi się i jeśli istnieją jakieś $j$, gdzie $R_i[j].\mathrm{changed} =$ `true`,
>     to tworzy pakiet z ofertą, do którego dodaje pary $(j, R_i[j].\mathrm{cost})$ dla wszystkich takich $j$,
>     ustawiając $R_i[j].\mathrm{changed}$ na `false`, a następnie wysyła ten pakiet do każdego swojego sąsiada z $N(i)$.
> - Wątek $\mathrm{Receiver}_i$ oczekuje na pakiet z ofertą od jakiegoś sąsiada z $N(i)$.
>     Gdy taki pakiet otrzymuje od jakiegoś sąsiada $l$, to dla każdej pary $(j, \mathrm{cost}_j)$ z takiego pakietu:
>         - wylicza $\mathrm{newcost}_{i,j} = 1 + \mathrm{cost}_j$,
>         - jeśli $\mathrm{newcost}_{i,j} < R_i[j].\mathrm{cost}$ to ustawia nowe wartości:
>             - $R_i[j].\mathrm{cost} = \mathrm{newcost}$,
>             - $R_i[j].\mathrm{nexthop} = l$,
>             - $R_i[j].\mathrm{changed} =$ `true`,
> - Oba wątki drukują stosowne komunikaty o wysyłanych i otrzymywanych pakietach oraz zmianach w routing table.
>
> Zwróć uwagę, aby $\mathrm{Sender}_i$ nie blokował dostępu do $R_i$ w czasie,
> gdy rozsyła pakiet z ofertami do sąsiadów oraz tak zmieniał $R_i[j].\mathrm{changed}$
> na `false` aby nie „zagłuszyć” żadnej nowej zmiany.

## Argumenty

- `n` — liczba wierzchołków
- `d` — liczba dodatkowych krawędzi (skrótów)
- `maxSleep` — odwrotność maksymalnego czasu oczekiwania wątku $\mathrm{Sender}$ (`maxSleep = 100` oznacza maks. czas. oczekiw. równy `1/100` sekundy)

Wszystkie powyższe argumenty powinny być liczbami naturalnymi różnymi od zera.

---

## Go

W celu uruchomienia programu należy wykonać polecenie

```bash
go run . ‹n› ‹d› ‹maxSleep›
```

z [uzupełnionymi parameterami](#argumenty) będąc w katalogu `go`.

---

## Ada

W celu uruchomienia programu należy go najpierw skompilować poleceniem

```bash
make
```

a następnie wykonać polecenie

```bash
./main.bin ‹n› ‹d› ‹maxSleep›
```

z [uzupełnionymi parameterami](#argumenty) będąc w katalogu `ada`.

---
