# Lista-4

## Zadanie 1

> Napisz program, który symuluje działanie wybranych struktur danych przechowujących ciągi znaków (przyjmujemy porządek leksykograficzny). Program powinien przyjmować jako parametr wejściowy typ struktury:
> - `--type bst` drzewo BST
> - `--type rbt` drzewo czerwono-czarne
> - `--type hmap` tablice hashujące z metodą łańcuchową dla przechowywanych w jednej komórce danych długości mniejszej niż $n_t$ oraz z wykorzystaniem samoorganizujących się drzew binarnych (np. drzew czerwono-czarnych) dla przechowywanych w jednej komórce danych o długości większej niż $n_t$. Przeprowadź testy mające na celu oszacowanie $n_t$, dla którego zysk w czasie dostępu do elementu uzasadnia nadkład wykonywanych operacji balansujących. Dobierz liczbę komórek $m$ odpowiednio do wybranej funkcji hashującej.
>
> Każda ze struktur powinna udostępniać przynajmniej poniższe funkcjonalności podawane na standardowym wejściu
> - insert $s$ – wstaw do struktury ciąg $s$ (jeśli na początku lub końcu ciągu znajduje się znak spoza klasy [a-zA-Z] to znak ten jest usuwany)
> - load $f$ – dla każdego oddzielonym białym znakiem, wyrazu z pliku $f$ wykonaj operację insert, lub zwróć informację o nieistniejącym pliku
> - delete $s$ – jeśli struktura nie jest pusta i dana wartość $s$ istnieje, to usuń element $s$
> - find $s$ – sprawdź czy w strukturze przechowywana jest wartość $s$ (jeśli tak to wypisz $1$, w p. p. wypisz $0$)
> - min – wypisz najmniejszy element znajdujący się w strukturze lub, dla struktur pustych oraz nie zachowujących porządku (np. hmap), pustą linię
> - max – wypisz największy element znajdujący się w strukturze lub, dla struktur pustych oraz nie zachowujących porządku (np. hmap), pustą linię
> - successor $k$ – wypisz następnik elementu $k$ lub, jeśli on nie istnieje (np. struktura nie zawiera $k$, $k$ nie ma następników, struktura nie zachowuje porządku), pustą linię
> - inorder – wypisz elementy drzewa w posortowanej kolejności (od elementu najmniejszego do największego) lub, dla struktur pustych oraz nie zachowujących porządku (np. hmap), pustą linię
>
> Wynik powinien być wypisywany na standardowe wyjście, a na standardowym wyjściu błędów powinny być wypisywane w kolejności: czas działania całego programu, liczba operacji każdego typu, maksymalna liczba elementów (maksymalne zapełnienie struktury w czasie działania programu), końcowa liczba elementów w strukturze. Przeprowadź eksperymenty pozwalające oszacować średni czas działania każdej z operacji.
>
> **Wejście**\
> Wejście składa się z $n+1$ linii. W pierwszej, znajduje się liczba $n$ określająca liczbę wykonywanych operacji, w liniach 2-$(n+1)$ znajdują się kolejne operacji zgodnie z ich specyfikacją. Program może wykorzystywać więcej niż jeden wątek, jednak operacje muszę być wykonane w zadanej kolejności.\
> Długość pojedynczego ciągu znaków nie przekracza 100, natomiast $n+1$ nie przekracza zakresu Integera.
>
> **Wyjście**\
> Wyjście składa się z $k \le n$ linii, będących wynikami kolejnych operacji podanych na wejściu.
>
> **Przykład** Przykładowe wywołanie
> ```
> ./main --type rbt <./input >out.res
> ```
> input | out.res
> --- | ---
> 17 |
> max | a aaa ab b
> insert aaa | ab
> insert a | 1
> insert b | 1
> insert ab | 1
> inorder | 0
> delete a | aaa
> delete b |
> max |
> load sample.txt |
> find three |
> delete three |
> find three |
> find Three |
> delete Three |
> find Three |
> min
>

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

> Wykonaj i zaprezentuj eksperymenty, które pozwolą postawić tezę na temat dolnego ograniczenia, średniej oraz górnego ograniczenia na liczbę porównań między elementami, wykonywaną przez procedurę find w każdej ze struktur. Testy wykonaj na liście unikatowych ciągów (np. słownik) oraz takiej, gdzie możliwe są powtórzenia.

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
