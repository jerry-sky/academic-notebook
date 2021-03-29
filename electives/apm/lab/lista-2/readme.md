---
lang: 'pl'
title: 'Lista 2. — Aplikacje mobilne, Laboratorium'
author: 'Jerry Sky'
---

- [Zadanie 1.](#zadanie-1)
- [Zadanie 2.](#zadanie-2)

---

## Zadanie 1.

>Napisz grę w kółko i krzyżyk, gdzie dwóch graczy na zmianę naciska przyciski w siatce 3×3 lub 5×5 oznaczone odpowiednio przez „X” lub „O”.
>Jeśli, któryś z graczy ułoży swoje litery pionowo, poziomo lub po przekątnej to wygrywa.
>Wykorzystaj odpowiedni Layout do rozłożenia przycisków oraz zrób tak, aby przyciski wypełniały odpowiednio ekran i czcionka była odpowiednio duża (możesz to przetestować na emulatorze dla różnych rozdzielczości ekranów).
>Wykorzystaj kilka aktywności.
>Co najmniej pierwsza startowa, na której wybieramy wersje gry tzn. 3×3 lub 5×5 oraz wynik ostatniej rozgrywki (kto wygrał X czy O).
>Druga aktywość dla gry 3x3 i trzecia dla wersji 5x5.

Projekt znajduje się w katalogu `ex-1/TicTacToe`.

---

## Zadanie 2.

> Napisz aplikację „Wisielec”, która wyświetla po kolei obrazek wisielca oraz słowo, które gracz próbuje zgadnąć.
> Słowo wybierane jest losowo z dostępnego słownika.
> Oczywiście cały czas wyświetlane jest słowo z prawidłowo zgadniętymi literami np. dla słowa komputer jeśli gracz zgadł prawidłowo litery o, m i e, słowo będzie wyglądało mniej więcej tak `?om???e?`.
> Wykorzystując dostępne Layout-y zrób też własną klawiaturę do wprowadzania liter na aktywości gry.
> Do utworzenia obrazków wykorzystaj np. program GIMP nazwij je odpowiednio `wisielec0.png`, `wisielec1.png` i tak dalej.
> Do wyświetlania obrazków wykorzystaj np. ImageView. Do przechowywania słownika wykorzystaj plik `strings.xml`.
>
> ```xml
> <string-array name="words">
>     <item>komputer</item>
>     <item>zgadywanka</item>
>     ...
> </string-array>
> ```
>
> Słownik możesz wypełnić dowolnymi słowami np. ściągniętymi z internetu przez prosty skrypt.

Projekt znajduje się w katalogu `ex-2/Hangman`.

---
