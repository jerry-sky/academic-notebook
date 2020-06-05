# Lista-4

## Zadanie na laboratorium

> Napisz program, który dla nieskompresowanych obrazów zapisanych w formacie TGA, policzy wyniki kodowania za pomocą różnicy między predyktorami JPEG-LS (7 starych standardów i nowy standard, jako kolor otoczenia obrazka przyjmujemy czarny - `RGB(0,0,0)`) i poda entropię dla kodu całego obrazka jak i poszczególnych składowych koloru.
>
> Dla porównania program powinien drukować także entropię wejściowego obrazu i entropię poszczególnych składowych koloru. Na końcu program powinien podać, która metoda jest optymalna (daje najmniejszą entropię) dla danego obrazu jako całości oraz optymalne metody dla poszczególnych składowych koloru.
>
> Entropię program powinien liczyć tylko dla mapy bitowej (pomijamy nagłówki i stopki) a różnice wyliczone dzięki predyktorom powinny być kodowane jako liczby 8 bitowe (operacje $(\mod 256)$ ).

## Uruchomienie programu

W celu uruchomienia programu należy wykonać `./main.py <input file`.

Program wymaga zainstalowanego `python3` do uruchomienia.

Nazewnictwo:
- `pixels` odnosi się do entropii całego obrazu
- `red`, `green`, `blue` odnoszą się do entropii poszczególnych składowych kolorów obrazu


## Pliki programu

Plik `main.py` jest plikiem wykonywalnym wymagającym `python3` do uruchomienia.

W pliku `pixel.py` znajdują się funkcje pomocnicze do arytmetyki na wartościach pikseli.

Plik `entropy.py` zawiera klasę odpowiadającą za zliczanie ile razy dana wartość się pojawiła na mapie bitowej obrazka. Przy pomocy tej klasy obliczana jest również entropia.
