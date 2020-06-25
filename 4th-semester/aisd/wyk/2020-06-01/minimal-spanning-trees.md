# Minimal spanning trees
*MSTs*

- [Outline](#outline)
- [I/O](#io)
- [Drzewa](#drzewa)
- [Algorytm Kruskala](#algorytm-kruskala)
  - [Poprawność algorytmu Kruskala](#poprawność-algorytmu-kruskala)
  - [Zbiory rozłączne (disjoint sets)](#zbiory-rozłączne-disjoint-sets)
  - [Pseudokod algorytmu Kruskala](#pseudokod-algorytmu-kruskala)
- [Algorytm Prima](#algorytm-prima)
- [More](#more)

## Outline

Na wejściu dostajemy graf spójny $G = (V,E,l)$, gdzie $V$ jest zbiorem wierzchołków, $E$ zbiorem krawędzi, a $l: E \to \mathbb{R}_+$ funkcją wagi krawędzi (zakładamy, że waga krawędzi jest dodatnia). Celem jest wyznaczenie podzbioru krawędzi tego grafu, który pozostawi graf spójnym oraz suma wag tych krawędzi będzie możliwie najmniejsza.

## I/O

*Input:* nieskierowany graf $G = (V,E,l), l: E \to \mathbb{R}_+$.

*Output:* drzewo $T = (V,E')$, gdzie $E' \subseteq E$, który minimalizuje wagę drzewa $\mathrm{waga}(T) = \sum_{e\in E'}l(e)$.

## Drzewa

Nim przejdziemy do budowy algorytmów zachłannych rozwiązujących problem MST przyjrzyjmy się pewnym własnościom grafów (drzew nieukorzenionych):
- drzewo jest nieskierowanym grafem spójnym i acyklicznym
- Własność 1:\
    Usunięcie krawędzi należącej do cyklu w grafie nie rozspójni grafu.
- Własność 2:\
    Drzewo o $n$ wierzchołkach ma $n-1$ krawędzi.

    Własność tą można pokazać zaczynając od grafu o $n$ wierzchołkach i $0$ krawędziach.\
    Następnie dokładając krawędź:
    - możemy dodać tylko krawędź pomiędzy dwoma niepołączonymi składowymi, bo w przeciwnym przypadku otrzymamy cykl, więc nie drzewo
    - Każda poprawnie dodana krawędź redukuje liczbę spójnych składowych grafu o $1$.

    Zatem pod dodaniu $n-1$ krawędzi otrzymamy jedną spójną składową o $n$ wierzchołkach, a całość będzie tworzyła drzewo.
- Własność 3:\
    Każdy spójny nieskierowany graf $G = (V,E)$ taki, że $|E| = |V| - 1$ jest drzewem.

    Aby udowodnić tą własność musimy jedynie pokazać, że $G$ jest acykliczny. Załóżmy nie wprost, że $G$ zawiera cykl. Usuńmy jedną krawędź należącą do cyklu z tego grafu, otrzymamy $G' = (V,E)$, gdzie $E' \subseteq E$, który będzie acykliczny i, z własności 1, spójny.

    Zatem graf $G'$ jest drzewem (z definicji drzewa) i, z własności 2, mamy $|E'| = |V| - 1$ $\implies$ sprzeczność.

    Zauważmy, że z powyższych własności wynika np. że aby stwierdzić czy spójny graf jest drzewem wystarczy sprawdzić, czy jego liczba krawędzi jest równa $\text{liczbie wierzchołków}-1$.
- Własność 4:

    Nieskierowany graf jest drzewem iff gdy istnieje unikatowa ścieżka pomiędzy dwoma wierzchołkami w tym grafie.

    Zauważmy, że jeśli między jakimiś dwoma węzłami istniały by dwie różne ścieżki to po połączeniu tych ścieżek otrzymalibyśmy cykl, a więc graf nie byłby drzewem. Ponadto, jeśli w grafie istnieje ścieżka między dowolnymi dwoma węzłami to graf jest spójny.
- *Cut property*:

    Załóżmy, że zbiór krawędzi $X$ jest podzbiorem krawędzi minimalnego drzewa rozpinającego grafu $G = (V,E)$. Wybierzmy podzbiór wierzchołków $S \subset V$ taki, że żadne krawędź pomiędzy $S$ i $V \setminus S$ nie należy do $X$. Niech $e$ będzie krawędzią o minimalnej wadze pomiędzy wierzchołkami z $S$ i wierzchołkami $V \setminus S$. Wtedy $X \cup e$ jest również podzbiorem krawędzi minimalnego drzewa rozpinającego grafu $G$.

    Zauważmy, że jeśli krawędzie $X$ są podzbiorem krawędzi minimalnego drzewa rozpinającego $T$ grafu $G$ oraz wybrana krawędź $e$ należy do tego drzewa $T$ to wniosek jest oczywisty. Załóżmy zatem, że $e \notin T$. Skonstruujemy inne MST $T'$, które będą się różnić od MST $T$ zmianą jednej krawędzi. Dodajmy zatem krawędź $e$ do drzewa $T$. Skoro $T$ było spójne to dodanie krawędzi $e$ utworzyło cykl. Zatem musi istnieć inna krawędź $e'$ łącząca wierzchołki ze zbioru $S$ z wierzchołkami ze zbioru $V \setminus S$. Jeśli usuniemy tą krawędź dostaniemy $T' = T \cup e \setminus s'$, które będzie drzewem, ponieważ:
    1. $T'$ będzie spójne z Własności 1, ponieważ $e'$ należało do cyklu,
    2. $T'$ ma tą samą liczbę krawędzi co drzewo $T$, więc z Własności 2 i 3 jest drzewem.

    Ponadto $T'$ będzie minimalnym drzewem rozpinającym, ponieważ
    $$
    \mathrm{waga}(T') = \mathrm{waga}(T) + l(e) - l(e')
    $$
    oraz obie krawędzie $e$ i $e'$ łączą wierzchołki zbioru $S$ z wierzchołkami zbioru $V \setminus S$, a dodatkowo $e$ została wybrana tak, że jej waga jest najmniejsza spośród krawędzi przechodzącymi pomiędzy tymi zbiorami. Zatem $l(e) \le l(e')$, co implikuje $\mathrm{waga}(T') \le \mathrm{waga(T)}$. Ale skoro $T$ było minimalnym drzewem rozpinającym to $\mathrm{waga}(T') = \mathrm{waga}(T)$, a zatem $T'$ jest również minimalnym drzewem rozpinającym, co kończy dowód.

    Zauważmy, że *cut property* precyzuje które krawędzie można dodawać pomiędzy zbiorami wierzchołków $S$ i $V \setminus S$ zakładając, że zbiory te już połączone krawędzią. Możemy zatem zbudować różne algorytmy wyznaczania MST bazując na różnych strategiach wyboru krawędzi do minimalnego drzewa rozpinającego, jeśli strategie te będą wykorzystywać poprawnie *cut property*.

    Dobrą wizualizację *cut property* daje $\text{Figure 5.3}$ oraz sekcja $\text{5.1.2 The cut property}$ w [książce Algorithms][dpv].

## Algorytm Kruskala

Algorytm ten buduje minimalne drzewo rozpinające dla wejściowego grafu $G = (V,E,l)$ i jest bardzo dobrą ilustracją zachłannego wyboru.

\>*Do MST $T$ dodawaj kolejne krawędzie o najmniejszej wadze, które nie tworzą cyklu.*

### Poprawność algorytmu Kruskala

Zauważmy, że po kilku krokach algorytmu Kruskala mamy częściowe rozwiązanie, które składa się ze zbioru spójnych składowych będących drzewami. Kolejna dodawana krawędź $e$ będzie łączyć dwie spójne składowe, powiedzmy $T_1$ oraz $T_2$. Skoro $e$ jest krawędzią o najmniejszej wadze nietworzącą cyklu to jest ona również krawędzią o najmniejszej wadze pomiędzy wierzchołkami należącymi do $T_1$ i $V\setminus T_1$. A zatem z *cut property* jest ona częścią MST, co dowodzi poprawności algorytmu Kruskala.

### Zbiory rozłączne (disjoint sets)

Ostatnią rzecz, którą pozostaje zrobić aby zaimplementować algorytm Kruskala, to wymyślić w jaki sposób możemy efektywnie stwierdzać, czy wybrana krawędź łączy ze sobą dwie różne komponenty (czyli nie tworzy cyklu). Użyjemy w tym celu struktury *zbiorów rozłącznych*, która będzie implementować następujące procedury:
- `makeset`$(x)$ – tworzy jednoelementowy zbiór $x$
- `find`$(x)$ – sprawdza do którego zbioru należy element $x$
- `union`$(x,y)$ – łączy zbiór, do którego należą elementy $x$ ze zbiorem do którego należą elementy $y$

Jednym ze sposobów reprezentowania zbiorów jest użycie ukorzenionego drzewa, gdzie:
- każdy wierzchołek drzewa reprezentuje element należący do zbioru
- każdy wierzchołek ma wskaźnik na swojego przodka (wskaźniki na potomków nie są potrzebne)
- korzeń drzewa jest reprezentantem zbioru opisanego przez drzewo (identyfikator korzenia jest traktowana jako identyfikator całego zbioru opisanego przez jego drzewo) i można go odróżnić od innych wierzchołków, bo jego wskaźnik na ojca wskazuje na niego samego,
- dodatkowo, każdy węzeł drzewa posiada pole `rank`, które może być chwilowo interpretowana jako wysokość pod-drzewa zawieszonego w danym węźle

Implementacja metod struktury dla ukorzenionych drzew:

`makeset`$(x)$:
1. $x.\mathrm{parent} \gets x$
2. $x.\mathrm{rank} \gets 0$

`find`$(x)$:
1. `while` $x \neq x.\mathrm{parent}$:
   1. $x \gets x.\mathrm{parent}$
2. `return` $x$

`union`$(x,y)$
1. $\mathrm{rootX} \gets$ `find`$(x)$
2. $\mathrm{rootY} \gets$ `find`$(y)$
3. `if` $\mathrm{rootX} = \mathrm{rootY}$:
   1. `return`
4. $\triangleright$ łączymy drzewa poprzez podłączanie wyższego drzewa do korzenia niższego
5. `if` $\mathrm{rootX}.\mathrm{rank} > \mathrm{rootY}.\mathrm{rank}$:
   1. $\mathrm{rootY}.\mathrm{parent} \gets \mathrm{rootX}$
6. `else`:
   1. $\mathrm{rootX}.\mathrm{parent} \gets \mathrm{rootY}$
   2. `if` $\mathrm{rootX}.\mathrm{parent} = \mathrm{rootY}$:
      1. $\mathrm{rootY}.\mathrm{rank} \gets \mathrm{rootY}.\mathrm{rank} + 1$

Procedura `union` łącząc zbiory buduje drzewa reprezentujące te zbiory w taki sposób, że zachowane są następujące własności:
1. $d_1$: dla każdego $x$, $x.\mathrm{rank} < x.\mathrm{parent}.\mathrm{rank}$;\
Własność zachodzi, ponieważ węzeł z $\mathrm{rank}$ równym $k$ jest tworzony poprzez złączenie dwóch drzew, których korzenie mieli $\mathrm{rank}$ równy $k-1$ (rozumowanie to można rozszerzyć do formalnego dowodu indukcyjnego).
2. $d_2$: każdy korzeń mający $\mathrm{rank}$ równy $k$ jest korzeniem drzewa mającego co najmniej $2^k$ węzłów.\
Jeśli zbiór ma $n$ elementów, a korzeń jego drzewa ma $\mathrm{rank}$ równą $k$ to $n > 2^k$ co implikuje, że $k < \log(n)$, co daje logarytmiczne ograniczenie na wysokość drzewa. Zatem procedury `find` oraz `union` mają pesymistyczną złożoność obliczeniową $O(\log(n))$ dla zbiorów wielkości $n$.

W [sekcji 5.1.4 książki Algorithms][dpv] jest pokazane jak można jeszcze usprawnić tę implementację.

### Pseudokod algorytmu Kruskala

`Kruskal`$(G)$:
1. `for all` $v \in V$:
   1. `makeset`$(v)$
2. $X \gets \{\}$
3. $\text{posortuj krawędzie ze zbioru } E \text{ według ich wagi}$
4. `for all` $\{u,v\} \in E$ w kolejności rosnącej:
   1. `if` `find`$(u)$ $\neq$ `find`$(v)$:
      1. $\text{dodaj krawędź } \{u,v\} \text{ do } X$
      2. `union`$(u,v)$

*Złożoność obliczeniowa:* W pesymistycznym przypadku algorytm Kruskala wykona $|V| \times$ `makeset`, $2|E| \times$ `find` oraz $(|V| - 1) \times$ `union`.

## Algorytm Prima

Algorytm szukający MST wykorzystując *cut property*. W przypadku tego algorytmu wybrane krawędzie do zbioru $X$ (oznaczenia zgodne z wcześniejszymi z *cut property*) zawsze formują drzewo (czyli graf spójny, a nie jak w przypadku algorytmu Kruskala rozłączne komponenty), a zbiór wierzchołków $S$ jest po prostu zbiorem węzłów tego drzewa tworzonego przez krawędzie $X$.

`Prim`$(G)$:
1. `for all` $v \in V$:
   1. $v.\mathrm{cost} \gets \infty$
   2. $v.\mathrm{prev} \gets$ `null`
2. $\mathrm{wybierz węzeł startowy } s$
3. $s.\mathrm{cost} \gets 0$
4. $s.\mathrm{prev} \gets s$
5. $\triangleright$ używa $v.\mathrm{cost}$ jako kluczy w [kolejce priorytetowej](../2020-05-04/kolejka-priorytetowa.md); im mniejsza wartość $\mathrm{cost}$ tym wyższy priorytet
6. $Q \gets$ `MakeQueue`$(V)$
7. `while` $Q \neq \emptyset$:
   1. $v \gets$ `ExtractMin`$(Q)$
   2. `for all` $\{v,z\} \in E$:
      1. `if` $z.\mathrm{cost} > l(v,z)$:
         1. $z.\mathrm{cost} \gets l(v,z)$
         2. $z.\mathrm{prev} = v$
         3. `DecreaseKey`$(Q,z)$

Algorytm Prima w każdej iteracji pętli `while` dodaje krawędź do zbioru $X$ (realizowane jest to przez [`ExtractMin`](../2020-05-04/kolejka-priorytetowa.md#extractminq)). Dodawana krawędź ma najmniejszą wagę spośród krawędzi pomiędzy wierzchołkami należącymi do zbioru $S$ i $V \setminus S$, co jest realizacją *cut property*. Z tego wynika poprawność algorytmu Prima.

*Złożoność obliczeniowa:* Łatwo zauważyć, że algorytm Prima jest bardzo podobny do [algorytmu Dijkstry](../2020-05-20/dijkstras-algorithm.md), a główna różnica polega na tym, że priorytetem wierzchołka w algorytmie Prima jest waga najlżejszej krawędzi łączącej ten wierzchołek z wierzchołkami ze zbioru $S$ (w algorytmie Dijkstry była to łączna długość ścieżki od węzła startowego). Zatem algorytm Prima ma taką samą złożoność jak algorytm Dijkstry i jak już wiemy jest ona zależna od [implementacji kolejki priorytetowej](../2020-05-04/kolejka-priorytetowa.md).

## More

- [sekcja 5.1 Algorithms][dpv]
- [sekcja 24 Introduction to Algorithms][clrs]

[dpv]: http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf
[clrs]: https://web.ist.utl.pt/~fabio.ferreira/material/asa/clrs.pdf
