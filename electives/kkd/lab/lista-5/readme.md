# Lista-5

## Zadanie na laboratorium

> **Ocena 3** Napisz program który dla nieskompresowanego obrazu zapisanego w formacie TGA policzy obraz uzyskany w wyniku kwantyzacji równomiernej poszczególnych składowych koloru. Program powinien dodatkowo wypisać błąd średniokwadratowy dla całego obrazu i poszczególnych składowych koloru oraz stosunek sygnału do szumu.
> Program powinien czytać pięć argumentów w linii poleceń: obraz wejściowy, obraz wyjściowy, liczba bitów na czerwień, liczba bitów na zieleń i liczba bitów na niebieski (liczba bitów między $0$ a $8$ - układ RGB).
>
> Przykładowe wywołanie programu powinno wyglądać następująco:
> ```
> mgc@topaz:~$ ./kwantyzacja mg.tga mg332.tga 3 3 2
> mse =174.173323
> mse(r)=86.167312
> mse(g)=87.994938
> mse(b)=348.357719
> SNR =74.038005 (18.694547dB)
> SNR(r)=171.797505 (22.350169dB)
> SNR(g)=152.415938 (21.830304dB)
> SNR(b)=30.058687 (14.779700dB)
> ```
>
> **Ocena 4** Popraw program z poprzedniego punktu zamieniając ostatnie 3 argumenty na jeden oznaczający liczbę bitów na piksel, program sam powinien dobrać podział tych bitów na poszczególne kolory. Kryterium według którego powinien nastąpić podział powinien być podany jako czwarty argument: SNR – maksymalizacja minimalnego SNR dla poszczególnych kolorów, lub MSE – minimalizacja maksymalnego błędu średniokwadratowego dla poszczególnych kolorów. Oprócz danych jak w poprzednim punkcie program powinien wypisać jakiego podziału bitów dokonał.
>
> **Ocena 5** Napisz program który dla nieskompresowanego obrazu zapisanego w formacie TGA policzy obraz uzyskany w wyniku kwantyzacji wektorowej kolorów. Program powinien dodatkowo wypisać błąd średniokwadratowy dla całego obrazu oraz stosunek sygnału do szumu. Do uzyskania wymaganej liczby kolorów należy użyć algorytmu Linndego-Buza-Graya (dla uproszczenia implementacji do mierzenia odległości między kolorami można użyć metryki taksówkowej).
>
> Program powinien czytać trzy argumenty w linii poleceń: obraz wejściowy, obraz wyjściowy, liczba kolorów (między 0 a 24, liczba kolorów to dwójkowa potęga podanej liczby). *(Program nie musi w obrazku wyjściowym kodować mapy kolorów, może wstawić wybrane kolory bezpośrednio do obrazka.)*

Program kwantyzujący obrazek i obliczający jego błędy w porównaniu z obrazkiem wejściowym. Wybiera na podstawie błędów najlepszy rozkład bitów dla poszczególnych kolorów.
(na ocenę 4)

## Uruchomienie programu

W celu uruchomienia programu należy wykonać `./main.py <input file> <output file> <bit depth (bits per pixel)> <bit spread measure: MSE|SNR>` wpisawszy odpowiednie opcje.

Czas trwania programu może być dość długi, zwłaszcza przy dużej liczbie bitów, ponieważ program musi rozważyć wszystkie możliwe rozstawienia bitów dla poszczególnych kolorów.

Na standardowe wyjście błędów wypisywane są kolejno znalezione lepsze ustawienia liczby bitów na każdy z poszczególnych kolorów. Jeśli jest taka potrzeba, oczywiście można standardowe wyjście błędów przekierować na `/dev/null`, celem otrzymania mniejszej liczby linijek wyjścia programu.

Program wymaga zainstalowanego `python3` do uruchomienia.


## Pliki programu

Plik `main.py` jest plikiem wykonywalnym, wymagającym `python3` do uruchomienia. Zawiera główną logikę programu – kwantyzacja obrazka oraz szukanie najlepszego rozkładu bitów.

W pliku `errors.py` zawarta jest klasa pomocnicza używana do zliczania MSE oraz SNR.
