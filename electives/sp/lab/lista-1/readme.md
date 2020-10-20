# Lista-1

*(Termin oddania: 2020-10-25)*

- [Zadanie 1.](#zadanie-1)
- [Zadanie 2.](#zadanie-2)
- [Zadanie 3.](#zadanie-3)
- [Zadanie 4.](#zadanie-4)
- [Zadanie 5.](#zadanie-5)
- [Zadanie 6.](#zadanie-6)

Wszystkie zadania znajdują się w plikach `ex-*.sh`.

W pliku `recording.cast` znajduje się zapis komend i ich wynik prezentujący działanie zadań. Niniejszy zapis może zostać odtworzony przy pomocy komendy
```bash
asciinema play recording.cast
```
przy zainstalowanym programie `asciinema` w systemie.

---

## Zadanie 1.

> Napisz skrypt, który jako argument otrzymuje:
> - ścieżkę do katalogu (korzenia poddrzewa katalogów, zawierającego pliki tekstowe),
>
> i drukuje listę wszystkich regularnych plików (nie katalogów) w tym poddrzewie.

[kod](ex-1.sh)

---

## Zadanie 2.

> Skrypt, wywoływany jak w zadaniu 1, który dla wszystkich słów występujących w plikach w danym poddrzewie katalogów, drukuje statystyki, ile razy dane słowo wystąpiło we wszystkich tych plikach.
>
> Przez słowo rozumiemy każdy niepusty podciąg sąsiadujących znaków liter ograniczony białymi znakami (white space).
>
> *Uwaga: Można założyć, że w plikach występują tylko litery, spacje i znaki nowej linii.*

[kod](ex-2.sh)

---

## Zadanie 3.

> Skrypt, wywoływany jak w zadaniu 1, który dla każdego słowa pojawiającego się w plikach danego poddrzewa katalogów, drukuje liczbę plików, w których to słowo występuje.

[kod](ex-3.sh)

---

## Zadanie 4.

> Skrypt, wywoływany jak w zadaniu 1, który dla każdego słowa pojawiającego się w plikach danego poddrzewa katalogów, drukuje linie, w których to słowo występuje, poprzedzone nazwą pliku, z którego pochodzą.

[kod](ex-4.sh)

---

## Zadanie 5.

> Skrypt, wywoływany jak w zadaniu 1, który we wszystkich plikach zastępuje wszystkie wystąpienia znaku 'a' znakiem 'A'.

[kod](ex-5.sh)

---

## Zadanie 6.

> Skrypt, wywoływany jak w zadaniu 1, który drukuje słowa występujące więcej niż raz w jakimś wierszu, wraz z tymi wierszami i nazwami plików, z których te wiersze pochodzą.

[kod](ex-6.sh)

---
