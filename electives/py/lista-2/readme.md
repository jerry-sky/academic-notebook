---
lang: 'pl'
title: 'Lista-2'
author: 'Jerry Sky'
---

---

- [Zadanie 1](#zadanie-1)
- [Zadanie 2](#zadanie-2)
- [Zadanie 3](#zadanie-3)
- [Zadanie 4](#zadanie-4)

---

Moje *concerns*:
1. Brak standaryzacji parsowania docstring'ów?
   - VS Code nie potrafi przypisać opisu z docstring'u danej funkcji do danego argumentu - po najechaniu kursorem na argument nie wyświetla się opis tego argumentu pomimo jego zdefiniowania w docstring'u danej funkcji.
   - Nie mogę znaleźć jedynego i słusznego systemu zapisywania deskrypcji argumentów funkcji, dlatego też trzymam się [Google's Python styleguide](http://google.github.io/styleguide/pyguide.html).

## Zadanie 1

> Napisz program, który dla danego pliku tekstowego wróci następujące informacje: liczba bajtów, liczbę słów, liczbę linii oraz maksymalną długość linii.

[kod](ex-1.py)

## Zadanie 2

> Napisz program, który koduje oraz dekoduje dowolny plik binarny w kodzie Base64. Kod Base64 koduje w taki sposób, że każde kolejne 6 bitów z pliku kodowane jest znakiem ASCII przedstawionych w poniższej tabeli:
> ```py
> tablica = 'ABCD​EFGH​IJKL​MNOP​QRST​UVWX​YZab​cdef​ghij​klmn​opqr​stuv​wxyz​0123​4567​89+/'
> ```
> Na przykład: słowo "Python" kodujemy jako "UHl0aG9u"

[kod](ex-2.py)

Jeśli linijka zawiera zmienną globalną danego modułu przyrównaną do długiego `str`inga to według [Google's Python styleguide *(3.2)*](http://google.github.io/styleguide/pyguide.html#32-line-length) jest to akceptowalne.

## Zadanie 3

> Napisz program, który zamienia wszystkie nazwy w danym katalogu oraz wszystkich podkatalogach na małe litery. Jako parametr podajemy katalog (zobacz moduł `os`).

[kod](ex-3.py)

## Zadanie 4

> Napisz program, który w danym katalogu znajdzie wszystkie pliki, które powtarzają się więcej niż raz (zobacz os, help(os.walk)). Weź pod uwagę, że pliki mogą mieć różne nazwy, ale tą samą zawartość, dlatego przyjmujemy, że dwa pliki są takie same, jeśli mają taką samą wielkość oraz taką samą wartość funkcji haszującej.
> Na wyjściu program wyświetla listę wszystkich plików, które się powtarzają (nazwy plików wraz ze ścieżką)
> ```bash
> $ python repchecker.py ./
>    ---------------------------------
>    ./plik1.txt
>    ./katalog1/plik5.txt
>    ./katalog3/plik1.dat
>    ---------------------------------
>    ./plik3.txt
>    ./katalog2/plik2.txt
>    ---------------------------------
> ```

[kod](ex-4.py)
