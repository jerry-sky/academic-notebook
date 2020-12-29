---
lang: 'pl'
title: 'Lista-2'
author: 'Jerry Sky'
---

---

## Zadanie na laboratorium

> Napisz program kodujący i program dekodujący dany plik wejściowy do pliku wyjściowego. Program kodujący powinien dodatkowo na koniec zwrócić na ekran odpowiednią entropię kodowanych danych, średnią długość kodowania i stopień kompresji. Alfabetem wejściowym są 8-bitowe kody ASCII.
>
> Należy wybrać jeden z wariantów:
>
> **Ocena 3** Programy mają używać klasycznego kodowania Huffmana i w czasie kompresji dodawać odpowiednio zapamiętany słownik umożliwiający dekompresję.
>
> **Ocena 4** Programy mają używać dynamicznych kodów Huffmana.
>
> **Ocena 5** Programy mają używać adaptacyjnego kodowania arytmetycznego ze skalowaniem.

Program używający dynamicznego kodowania Huffmana (na ocenę 4).

## Uruchomienie programu

W celu uruchomienia programu należy użyć:

`./main.py <--encode|--decode> <input file> <output file>`.
