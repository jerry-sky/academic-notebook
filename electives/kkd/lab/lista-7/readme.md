# Lista-7

## Zadanie na laboratorium

Napisz następujące programy:

`koder in out` – program który korzystając z rozszerzonego kodu Hamminga $(8, 4)$ zakoduje plik `in` do pliku `out`.

`szum p in out` – program który z prawdopodobieństwem `p` zamienia na przeciwny każdy bit z pliku `in` i zapisuje wynik w pliku `out`.

`dekoder in out` – program który korzystając z rozszerzonego kodu Hamminga $(8, 4)$ zdekoduje plik `in` do pliku `out`, wypisując na końcu w ilu przypadkach napotkał 2 błędy.

`sprawdz in1 in2` – program porównujący plik in1 z plikiem `in2` i wypisujący ile 4-bitowych
bloków nie jest identycznych.

## Uruchomienie programów

W celu uruchomienia któregokolwiek programu należy wykonać komendę taką samą jak w [powyższej sekcji](#zadanie-na-laboratorium) z prefiksem „`./`”.

## Pliki programów

W plikach `encoder.py`, `noise.py`, `decoder.py` oraz `compare.py` znajdują się odpowiednie implementacje zadanych programów.

W pliku `utilities.py` znajduje się funkcja pomocnicza do uzyskiwania $n$-tego bitu z bloku bitów.

## Źródło

W bardzo przystępny sposób rozszerzone kody Humming-a zostały [przedstawione przez Pana Profesora Jerzego Rutkowskiego](https://www.youtube.com/watch?v=B1eNseCicEI).
