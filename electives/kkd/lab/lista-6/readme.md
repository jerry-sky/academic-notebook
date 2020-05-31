# Lista-6

## Zadanie na laboratorium

> Napisz program kodujący oraz program dekodujący dany obrazek w formacie TGA. Parametrem programu kodującego jest $k$, przyjmujący wartości ze zbioru $\{1, \dots, 7\}$, oznaczający liczbę bitów kwantyzatora.
>
> Dodatkowo napisz program który dla wejściowego obrazka i jego odkodowanej wersji poda błąd średniokwadratowy dla całego obrazu i poszczególnych składowych koloru oraz stosunek sygnału do szumu.
>
> **Ocena 3** Dla każdego koloru użyć kodowania różnicowego z kwantyzatorem równomiernym.
>
> **Ocena 4** Dla każdego koloru użyć filtra dolnoprzepustowego (średnia) i górnoprzepustowego (odchylenie). Następnie wynik filtra dolnoprzepustowego zakodować różnicowo a wynik górnoprzepustowego wprost za pomocą kwantyzatora równomiernego.
>
> **Ocena 5** Jak w punkcie poprzednim, ale użyć kwantyzatorów nierównomiernych (dopasowanych do poszczególnych pasm).

Rozwiązanie na *ocenę 3*.

## Uruchomienie programu

W celu uruchomienia głównego programu należy wykonać `./main.py --mode <encode|decode> <input file> <output file> [bit depth]` gdzie `[bitdepth]` jest wymaganym argumentem jeśli `--mode encode`.

Żeby uruchomić program do obliczania błędów należy wykonać `./errors.py <first file> <second file>`.

## Pliki programu

Plik wykonywalny `main.py` zawiera główny program kodujący obrazek TGA do pliku binarnego oraz dekodujący plik binarny do zkwantyzowanego obrazka TGA.

Plik `bitpack_utility.py` zawiera funkcje pomocnicze do odczytywania poszczególnych bajtów lub paczek bitów o innych rozmiarach niż `size=8`.

Plik `bitwiseio.py` zawiera dwie klasy służące do czytania pliku w *bit po bicie* zamiast *bajt po bajcie*.

Plik wykonywalny `errors.py` zawiera program obliczający błąd średniokwadratowy oraz stosunek sygnału do szumu dla całego obrazu i poszczególnych kolorów.

Plik `tga_utility.py` zawiera funkcje pomocnicze używane podczas kodowania i odkodowywania obrazków (nagłówki i stopki plików).
