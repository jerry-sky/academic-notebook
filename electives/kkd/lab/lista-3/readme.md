# Lista-3

## Zadanie na laboratorium

> **Ocena 3** Napisz program który implementuje zmodyfikowany algorytm LZ77, który zamiast 3 liczb używa 2:
> - $(0, kod\_litery)$ – jeśli pierwszej litery w buforze kodowania nie ma w buforze słownika,
> - $(i, j)$ – dla najdłuższego możliwego prefiksu z bufora kodowania występującego w buforze słownika (przedłużonym o bufor kodowania) i to przesunięcie w słowniku a $j + 1$ ilość znaków do skopiowania (omijamy kod ostatniej litery z klasycznego LZ77).\
> W programie bufor słownika ma mieć 255 znaków a bufor kodowania 256 (stąd używane liczby są 8-bitowe).\
> Program ma mieć możliwość kodowania i dekodowania, dodatkowo podczas kodowania ma podawać długość kodowanego pliku, długość uzyskanego kodu, stopień kompresji, entropię kodowanego tekstu i entropię uzyskanego kodu.
>
> **Ocena 4** Napisz program kodujący i dekodujący dany plik za pomocą algorytmu LZW. Ciąg wartości indeksów słownika początkowo powinien być kodowany liczbami 9-bitowymi a następnie liczby powinny być automatycznie wydłużane o kolejne bity wraz ze wzrostem wielkości słownika.\
> Program dodatkowo podczas kodowania ma podawać długość kodowanego pliku, długość uzyskanego kodu, stopień kompresji, entropię kodowanego tekstu i entropię uzyskanego kodu.
>
> **Ocena 5** Napisz program kodujący i dekodujący dany plik za pomocą algorytmu LZW. Ciąg wartości indeksów słownika ma być zakodowany kodowaniem uniwersalnym. Alfabetem wejściowym są 8-bitowe kody. Domyślnie program powinien używać kodowania Eliasa $\omega$ oraz mieć możliwość opcjonalnego użycia pozostałych kodowań Eliasa oraz kodowania Fibonacciego.\
> Program dodatkowo podczas kodowania ma podawać długość kodowanego pliku, długość uzyskanego kodu, stopień kompresji, entropię kodowanego tekstu i entropię uzyskanego kodu.

Program używający algorytmu LZW z kodowaniem uniwersalnym (Fibonacciego oraz Eliasa). *(na ocenę 5)*

## Uruchomienie programu

W celu uruchomienia programu należy wykonać `./main.py <opts> <input file> <output file>` gdzie `<opts>`:

  - `--mode` może być:
    - `encoding`
    - `decoding`
  - `--coding` może być:
    - `fib`
    - `delta`
    - `gamma`
    - `omega` *(domyślne)*

Program wymaga zainstalowanego `python3` do uruchomienia.

## Pliki programu

Pliki `*_coding.py` zawierają poszczególne klasy kodujące i dekodujące pliki używając kodowania uniwersalnego.

Plik `lzw.py` zawiera klasę implementującą algorytm kompresji danych LZW.

Plik `bitwiseio.py` zawiera klasę ułatwiającą czytanie poszczególnych bitów z plików.

Plik `entropy.py` służy do obliczania entropii plików wejściowego oraz wyjściowego podczas kodowania.

Plik `main.py` jest głównym programem, który jest plikiem wykonywalnym wymagającym `python3` do uruchomienia.
