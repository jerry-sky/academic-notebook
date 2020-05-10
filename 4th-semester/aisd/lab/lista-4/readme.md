# Lista-4

## Zadanie 1

### Szacowanie czasu każdej z operacji

Plik `dict-partial.txt` zawiera część słownika `dict.txt`. Niniejszy plik wykorzystałem do zmierzenia średniego czasu wykonywania poszczególnych operacji.
1. `insert`\
    Zmierzenie polegało na wykonaniu operacji `load dict-partial.txt` i podzieleniu wartości czasu działania programu oraz wartości liczby elementów w strukturze.

    Dla BST: `3,89406 e-4` sekundy\
    Dla RB-Tree: `2,6235 e-5` sekund\
    Dla HashMap: `1,2254 e-5` sekund

2. `delete`\
    Zmierzenie polegało na wykonaniu operacji `load dict-partial.txt`, usunięciu kilku wartości ze struktury oraz podzieleniu wartości czasu działania dla operacji `delete` przez liczbę wykonania tej operacji.

    Dla BST: `2,543259 e-3` sekundy\
    Dla RB-Tree: `1,62268 e-4` sekundy\
    Dla HashMap: `9,1505 e-5` sekundy

3. `find`\
    Zmierzenie polegało na wykonaniu operacji `load dict-partial.txt`, wykonania operacji `find` dla kilku wartości ze struktury oraz podzieleniu wartości czasu działania dla operacji `find` przez liczbę wykonania tej operacji.

    Dla BST: `2,442122 e-3` sekundy\
    Dla RB-Tree `1,45102 e-4` sekundy\
    Dla HashMap: `1,0548258 e-2` sekundy

4. `min` oraz `max`\
    Zmierzenie polegało na wykonaniu operacji `load dict-partial.txt`, wykonania operacji `min` oraz `max`.

     |    . | BST | RB-Tree |
     | ---: | :---: | :---: |
     |`min`| `4,839897155761719 e-5`| `2,02178955078125 e-5`|
     |`max`| `2,059459686279297 e-3`| `6,461143493652344 e-5`|

     Warto zaznaczyć, że dla operacji `min` mamy taki sam rząd wielkości czasu operacji. Wynika to z tego, że dodawaliśmy elementy ze słownika w cały czas w tej samej kolejności. Tak duża różnica pomiędzy operacjami `min` oraz `max` jest wynikiem braku balansowania drzewa. W RB-Tree nie ma takiego problemu.

5. `successor`\
    Zmierzenie polegało na wykonaniu operacji `load dict-partial.txt`, wykonania operacji `successor` dla kilku wartości ze struktury oraz podzieleniu wartości czasu działania dla operacji `successor` przez liczbę wykonania tej operacji.

    BST: `1,879787 e-3` sekundy\
    RB-Tree: `1,52254 e-4` sekundy

### Szacowanie $n_t$

W zadaniu należało zaimplementować tablice hashujące z metodą łańcuchową dla danych długości mniejszej niż $n_t$ oraz z wykorzystaniem RB-Trees dla danych długości większej od $n_t$.

Pod-zadaniem tutaj jest oszacowanie wartości zmiennej $n_t$. W pliku `ex-1-hash-table-chained-tests.py` znajdują się podstawowe testy weryfikujące dla jakiej liczby elementów w danej komórce RB-Tree ma lepszy czas wstawiania nowego elementu oraz kiedy RB-Tree ma lepszy czas podczas wyszukiwania elementu w strukturze.

Przy uruchamianiu programu `./ex-1-hash-table-chained-test.py 80` można zauważyć, że podana wartość jest graniczna w przypadku czasu wstawiania nowego elementu do struktury. Dla wartości $n_t$ większych od `80` RB-Tree jest zawsze lepsze od listy jednokierunkowej, kiedy dla wartości mniejszych na odwrót.

Jeśli chodzi o czas wyszukiwania elementu w strukturze dla liczby elementów większej od $2$ RB-Tree jest zawsze lepsze.

Biorąc pod uwagę te wyniki należy wybrać wartość $n_t$ dla jakiej `HashTable` będzie działać najszybciej. Jeśli mamy dużo operacji `insert` wartość $n_t$ bliższa `80` będzie lepszym wyborem. Kiedy dla dużej liczby operacji `find` wartość $n_t$ bliższa `2` będzie lepszym wyborem.

Dla uproszczenia w programie wybrałem $n_t = 41$. Chociaż można zdecydować się na dynamicznie dobieranie $n_t$ i decydować się na zmianę struktury danej komórki w zależności od liczby wykonanych operacji `find` oraz `insert`.
