---
lang: 'pl'
title: 'Lista-3'
author: 'Jerry Sky'
date: '2020-12-06'
---

---

- [Zadanie 1.](#zadanie-1)
- [Zadanie 2.](#zadanie-2)

---

## Zadanie 1.

> Używając LEX-a i BISON-a zaimplementuj translator wyrażeń arytmetycznych w ciele $\mathbb{Z}_{1234577}$ z postaci infiksowej do postaci postfiksowej (odwrotnej notacji polskiej), z korekcją postaci liczby (w $Z_p$ nie ma liczb ujemnych i większych lub równych $p$), i podającej wynik obliczenia wyrażenia. Wyrażenia do policzenia umieszczone są w osobnych liniach. Program ma przetwarzać wszystkie linie wejścia, a linie zaczynające się od `#` traktować jak linie komentarza i omijać. W przypadku długich linii ma być możliwość ich podzielenie za pomocą znaku `\` (tak jak w języku C).
>
> Zadbaj o właściwe priorytety operatorów, właściwą łączność operatorów i odpowiednią obsługę błędów. Pamiętaj o unarnym operatorze `-` dla danych wejściowych (często dla wygody w $Z_p$ piszemy np. $−1$ zamiast $p−1$). Potęgowanie powinno być dozwolone tylko jako pojedynczą operacja — nie wolno składać potęg.

Rozwiązanie zadania znajduje się w plikach `ex-1.{l,y}`. Po uprzednim skompilowaniu przy pomocy `make` program można uruchomić przy pomocy `./ex-1`.

---

## Zadanie 2.

> Napisz poprzednie zadanie w innym języku programowania, np. w Pythonie z pakietem PLY lub Javie z biblioteką ANTLR (inne języki uzgodnij z prowadzącym laboratorium).

Program jest napisany w Pythonie. Kod źródłowy znajduje się w plikach `./ex-2.py` oraz `auxiliary.py`.

Przed uruchomieniem należy się upewnić, że paczka `ply` jest zainstalowana i dostępna dla programu `python3` (wystarczy uruchomić polecenie `python3 -m pip install ply`).

Żeby uruchomić program, należy wykonać `./ex-2.py` lub najpierw `make` a następnie `./ex-2`.

---
