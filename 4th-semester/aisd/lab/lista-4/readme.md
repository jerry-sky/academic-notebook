# Lista-4

## Zadanie 1

Plik wykonywalny `./main.py` jest rozwiązaniem tego zadania. W plikach `bst.py`, `rbt.py` oraz `hash_tables.py` zawarte są implementacje poszczególnych struktur danych.

### Szacowanie czasu działania każdej z operacji

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

     |     . |           BST           |         RB-Tree         |
     | ----: | :---------------------: | :---------------------: |
     | `min` | `4,839897155761719 e-5` | `2,02178955078125 e-5`  |
     | `max` | `2,059459686279297 e-3` | `6,461143493652344 e-5` |

     Warto zaznaczyć, że dla operacji `min` mamy taki sam rząd wielkości czasu operacji. Wynika to z tego, że dodawaliśmy elementy ze słownika cały czas w tej samej kolejności. Tak duża różnica pomiędzy operacjami `min` oraz `max` jest wynikiem braku balansowania drzewa. W RB-Tree nie ma takiego problemu.

5. `successor`\
    Zmierzenie polegało na wykonaniu operacji `load dict-partial.txt`, wykonania operacji `successor` dla kilku wartości ze struktury oraz podzieleniu wartości czasu działania dla operacji `successor` przez liczbę wykonania tej operacji.

    BST: `1,879787 e-3` sekundy\
    RB-Tree: `1,52254 e-4` sekundy

### Szacowanie $n_t$

W zadaniu należało zaimplementować tablice hashujące z metodą łańcuchową dla danych długości mniejszej niż $n_t$ oraz z wykorzystaniem RB-Trees dla danych długości większej od $n_t$.

Pod-zadaniem tutaj jest oszacowanie wartości zmiennej $n_t$. W pliku `ex-1-hash-table-chained-tests.py` znajdują się podstawowe testy weryfikujące dla jakiej liczby elementów w danej komórce RB-Tree ma lepszy czas wstawiania nowego elementu oraz kiedy RB-Tree ma lepszy czas podczas wyszukiwania elementu w strukturze.

Przy uruchamianiu programu `./ex-1-hash-table-chained-test.py 80` można zauważyć, że podana wartość jest graniczna w przypadku czasu wstawiania nowego elementu do struktury. Dla wartości $n_t$ większych od `80` RB-Tree jest zawsze lepsze od listy jednokierunkowej, podczas gdy dla wartości mniejszych jest na odwrót.

Jeśli chodzi o czas wyszukiwania elementu w strukturze dla liczby elementów większej od `2` RB-Tree jest zawsze lepsze.

Biorąc pod uwagę te wyniki należy wybrać wartość $n_t$ dla jakiej `HashTable` będzie działać najszybciej. Jeśli mamy dużo operacji `insert` wartość $n_t$ bliższa `80` będzie lepszym wyborem, kiedy dla dużej liczby operacji `find` wartość $n_t$ bliższa `2` będzie lepszym wyborem.

Dla uproszczenia w programie wybrałem $n_t = 41$. Chociaż można zdecydować się na dynamicznie dobieranie $n_t$ i decydować się na zmianę struktury danej komórki w zależności od liczby wykonanych operacji `find` oraz `insert`.

---

## Zadanie 2

### Testy na słowniku

W celu zmniejszenia czasu oczekiwania ładowania wartości ze słownika do BST stworzyłem osobny plik `dict-partial.txt` zawierający część słów ze słownika `dict.txt`. Nie ma to większego wpływu na wykonywane eksperymenty.

Plik testowy `tests/ex-2-dict-avg.txt` użyłem do oszacowania średniej liczby porównań, kiedy plik `tests/ex-2-base.txt` użyłem do szukania ograniczeń górnych i dolnych.

1. BST:

    W przypadku wyszukiwania wartości mniejszej niż wartość korzenia w drzewie wypełnionym po kolei (rosnąco) słowami ze słownika (będzie to pierwsze słowo ze słownika w drzewie bez samo-balansowania) liczba porównań wynosi oczywiście `1`, bo szukana wartość nie istnieje w drzewie a poszukiwania kończą się na odkryciu, że lewym potomkiem korzenia drzewa jest `NIL`.

    Wyszukując słowo bliższe końcowym słowom ze słownika można zauważyć, że liczba porównań znacznie rośnie. Przykładowo wyszukiwanie słowa `zloty` generuje aż `2139` porównań.

    Powyższe rezultaty wynikają z własności BST. Bez samo-balansowania wstawiane słowa ze słownika implikują bardzo długie gałęzie drzewa.

    Średnia liczba porównań wynosi `1365,57`.

2. RB-Tree:

    Wyszukiwanie słów z początku słownika zajmuje `10` porównań.
    Kiedy wyszukiwanie słów z końca słownika zajmuje `20` porównań.\
    *(Obie powyższe wartości są mniejsze niż `2*\lg(n+1)` więc mamy pewność co do zachowania własności RB-Tree.)*

    Średnia liczba porównań wynosi `13,14`.

3. HashTable:

    Wyszukiwanie jakichkolwiek słów ze słownika zajmuje maksymalnie 2 porównania, a w większości przypadków zajmuje tylko jedno porównanie. Oznacza to, że mamy pewne kolizje słów podobnych do siebie, ale tych kolizji nie mamy tak dużo.

    Średnia liczba porównań wynosi `1,43`.

### Testy na `lotr.txt`

Testy wykonywałem dla pierwszych 5000 linijek oryginału pliku `lotr.txt` z powodu wolnego wstawiania elementów dla BST.

Plik testowy `tests/ex-2-lotr-avg.txt` użyłem do oszacowania średniej liczby porównań, kiedy plik `tests/ex-2-base.txt` użyłem do szukania ograniczeń górnych i dolnych.

1. BST:

    Wyszukiwanie pierwszego słowa z pliku (słowo `SPECIAL`) zajmuje oczywiście tylko jedno porównanie jako, że w BST nie zachodzą rotacje. Wyszukiwanie słowa `your` zajmuje 25 porównań i jest to największa liczba porównań, jaką udało mi się uzyskać.

    Dla wyszukiwania kilkunastu wybranych słów średnia liczba porównań wynosi około `17,79`.

2. RB-Tree:

    Największa liczba porównań jaką udało mi się znaleźć to `23`.

    Dla wyszukiwania kilkunastu wybranych słów średnia liczba porównań wynosi około `11,36`.

3. HashTable:

    Nie udało mi się znaleźć większej liczby porównań niż 2.

    Dla wyszukiwania kilkunastu wybranych słów tylko raz liczba porównań wynosiła 2 – przez co średnia wynosi `1,07`.
