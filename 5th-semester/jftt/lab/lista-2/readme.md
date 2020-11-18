# Lista-2

*Jerzy Wroczyński*\
*nr indeksu: 250075*\
*(Termin oddania 2020-11-15)*

- [Kompilacja wszystkich programów](#kompilacja-wszystkich-programów)
- [Zadanie 1.](#zadanie-1)
- [Zadanie 2.](#zadanie-2)
- [Zadanie 3.](#zadanie-3)
- [Zadanie 4.](#zadanie-4)

---

## Kompilacja wszystkich programów

W celu kompilacji wszystkich programów załączonych jako rozwiązania do zadań z listy należy wykonać polecenie `make`. Wówczas stworzone zostaną pliki wykonywalne `ex-*.o`. Poniżej, w osobnych sekcjach jest opisane działanie każde z nich i w jaki sposób należy je uruchamiać.

---

## Zadanie 1.

> Napisz we *FLEX*-ie program, który czyta dowolny plik tekstowy, usuwa w nim wszystkie białe znaki na końcu i na początku wiersza, zmienia wszystkie wystąpienia ciągów tabulatorów i spacji na dokładnie jedną spację, likwiduje puste linie, oraz na końcu dopisuje liczbę linii i słów (ciągi znaków oddzielone białymi znakami).

W celu uruchomienia programu należy wykonać polecenie
```bash
./ex-1.o < plik-wejściowy > plik-wyjściowy
```
oczywiście po [skompilowaniu](#kompilacja-wszystkich-programów).

---

## Zadanie 2.

> Napisz w FLEX-ie program który usuwa wszystkie komentarze w plikach źródłowych języka Python.

W celu uruchomienia programu należy wykonać polecenie
```bash
./ex-2.o < plik-wejściowy > plik-wyjściowy
```
oczywiście po [skompilowaniu](#kompilacja-wszystkich-programów).

---

## Zadanie 3.

> Napisz w FLEX-ie program, który usuwa wszystkie komentarze w programach napisanych w języku *C++*, a po włączeniu odpowiedniej opcji pozostawia komentarze dokumentacyjne (wg. Doxygen-a co najmniej następujące `/**`, `/*!`, `///` i `//!`) i usuwa pozostałe.

W celu uruchomienia programu należy wykonać polecenie
```bash
./ex-3.o < plik-wejściowy > plik-wyjściowy
```
oczywiście po [skompilowaniu](#kompilacja-wszystkich-programów).

Żeby komentarze dokumentacyjne nie zostały usunięte należy dodać parametr o jakiejkolwiek wartości, przykładowo:
```bash
./ex-3.o a < plik-wejściowy > plik-wyjściowy
```

---

## Zadanie 4.

> Używając FLEX-a zaimplementuj prosty kalkulator postfiksowy (odwrotna notacja polska) dla liczb całkowitych wykonujący operacje dodawania (`+`), odejmowania (`-`), mnożenia (`*`), dzielenia całkowitoliczbowego (`/`), potęgowania (`^`) i modulo (`%`). Wyrażenie do policzenia powinno być napisane w jednej linii. Program powinien wyświetlać dla każdej linii wynik albo komunikat o błędzie (jak najbardziej szczegółowy).

Klasycznie uruchamiając program wykonany w Flexie
```bash
./ex-4.o
```
program będzie czytał `stdin` jako plik wejściowy linijka po linijce.

---
