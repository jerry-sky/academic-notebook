---
lang: 'pl'
title: 'Lista 2.'
subtitle: 'Programowanie współbieżne, Laboratorium'
author: 'Jerry Sky'
date: '2021-05-02'
---

[poprzednia-lista]: ../lista-1/readme.md

- [Zadanie 1.](#zadanie-1)
- [Zadanie 2.](#zadanie-2)
- [Rozwiązanie](#rozwiązanie)
    - [Go](#go)
    - [Ada](#ada)
    - [Parametry](#parametry)

---

## Zadanie 1.

> Rozszerz system zaimplementowany w [zadaniu z poprzedniej listy][poprzednia-lista] w taki sposób,
> aby można w nim dodać $b$ krawędzi skierowanych postaci $(i,j)$,
> gdzie $i>j$, oraz ustalić parametr $h$,
> oznaczający czas życia pakietu rozumiany jako największa liczba jego transferów od wierzchołka do wierzchołka.
> W grafie mogą występować cykle, więc jeśli pakiet w h krokach nie dotrze do celu,
> to drukowany jest komunikat o jego śmierci i znika z systemu.
> Program ma być uruchamiany z parametrami:
> $n, d, b, k, h$,
> gdzie parametry $n, d, k$ oznaczają to samo co w [zadaniu z poprzedniej listy][poprzednia-lista],
> a parametry $b, h$ mają takie znaczenie, jak opisano wyżej.

---

## Zadanie 2.

> Dodaj wątek kłusownika, który co pewien czas budzi się,
> kontaktuje się z wątkiem losowo wybranego wierzchołka i umieszcza w nim pułapkę na jeden pakiet.
> Jeśli pakiet dotrze do wierzchołka z zastawioną pułapką,
> to drukowany jest komunikat,
> że wpadł on w pułapkę i pakiet znika z systemu wraz z pułapką, w którą wpadł.
>
> (Wskazówka: w wątku wierzchołka zastosuj konstrukcję `select`,
> aby mógł on obsługiwać zarówno zastawienie pułapki kłusownika, jak i odbieranie pakietów.)

---

## Rozwiązanie

### Go

Pliki Źródłowe znajdują się w katalogu `go`.

Żeby uruchomić program, należy wykonać polecenie

```bash
go run . ‹n› ‹d› ‹b› ‹k› ‹h› ‹maxSleep› [‹plundererIntervals›]
```

z uzupełnionymi parametrami.

Nagranie `asciinema` znajduje się w pliku [`go.cast`](go.cast).

---

### Ada

Pliki źródłowe znajdują się w katalogu `ada`.

Przed uruchomieniem programu należy go skompilować poleceniem

```bash
make
```

Teraz można uruchomić program poleceniem

```bash
./main.bin ‹n› ‹d› ‹b› ‹k› ‹h› ‹maxSleep› [‹plundererIntervals›]
```

z uzupełnionymi parametrami.

Nagranie `asciinema` znajduje się w pliku [`ada.cast`](ada.cast).

---

### Parametry

Parametr `maxSleep` określa liczbę, przez jaką należy podzielić domyślny czas oczekiwania wątków (jedna sekunda).
Przykładowo, jeśli `maxSleep = 100` oznacza to, że maksymalny czas oczekiwania wynosi `1/100` sekundy, czyli `10` milisekund.

Parametr *opcjonalny* `plundererIntervals` określa mnożnik okresu oczekiwania określonego przez parametr `maxSleep`.
Jeśli parametr ten nie zostanie podany,
kłusownik nie zostanie aktywowany.\
W celu jego aktywacji należy podać liczbę dodatnią,
np. `1`.
Wówczas kłusownik ma taki sam czas oczekiwania jak każdy wątek węzła w grafie.
Czas oczekiwania można zwiększyć,
podając większą liczbę.

---
