Lista-5
-------

Program kwantyzujący obrazek i obliczający jego błędy w porównaniu z obrazkiem wejściowym. Wybiera na podstawie błędów najlepszy rozkład bitów dla poszczególnych kolorów.
(na ocenę 4)

Uruchomienie programu
---------------------

W celu uruchomienia programu należy wykonać `./main.py <input file> <output file> <bit depth (bits per pixel)> <bit spread measure: MSE|SNR>` wpisawszy odpowiednie opcje.

Czas trwania programu może być dość długi, zwłaszcza przy dużej liczbie bitów, ponieważ program musi rozważyć wszystkie możliwe rozstawienia bitów dla poszczególnych kolorów.

Na standardowe wyjście błędów wypisywane są kolejno znalezione lepsze ustawienia liczby bitów na każdy z poszczególnych kolorów. Jeśli jest taka potrzeba, oczywiście można standardowe wyjście błędów przekierować na `/dev/null`, celem otrzymania mniejszej liczby linijek wyjścia programu.

Program wymaga zainstalowanego `python3` do uruchomienia.


Pliki programu
--------------

Plik `main.py` jest plikiem wykonywalnym, wymagającym `python3` do uruchomienia. Zawiera główną logikę programu – kwantyzacja obrazka oraz szukanie najlepszego rozkładu bitów.

W pliku `errors.py` zawarta jest klasa pomocnicza używana do zliczania MSE oraz SNR.

