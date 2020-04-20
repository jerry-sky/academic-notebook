# Lista-3

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
