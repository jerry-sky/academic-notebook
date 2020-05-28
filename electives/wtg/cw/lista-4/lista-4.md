# Lista-4
*Grafy planarne*

- [Lista-4](#lista-4)
  - [Zadanie 42](#zadanie-42)
  - [Zadanie 45](#zadanie-45)
  - [Zadanie 48](#zadanie-48)


## Zadanie 42

> Przedstaw grafy $K_{3,3}$ i $K_5$ jako grafy na płaszczyźnie z minimalną liczbą przecięć.

![solution](l4z42.png)

## Zadanie 45

> Narysuj na płaszczyźnie graf Petersena tak aby na rysunku były tylko dwa przecięcia
krawędzi.

![petersen's graph](l4z45.png)

## Zadanie 48

> Pokaż, że każde drzewo jest planarne.
>
> *Wskazówka: To jest proste ćwiczenie na indukcję matematyczną; indukcję zrób po liczbie
wierzchołków.*

Niech zadane drzewo będzie $T$.

Stworzymy graf izomorficzny z drzewem $T$. Bierzemy wierzchołek $r \in V(T)$, który traktujemy jako korzeń drzewa. Wszystkie wierzchołki należące do sąsiedztwa $r$ dorysowujemy na nowym grafie w takiej samej odległości jednak każdy skierowany w inną stronę i łączymy te wierzchołki krawędziami z $r$. Teraz dla każdego z tych wierzchołków sąsiednich do $r$ powtarzamy tę procedurę aż nie skończą się nam wierzchołki.\
Kształt powstałego grafu może przypominać gwiazdę, bo rysując kolejne krawędzie oddalamy się od $r$ i nie przecinamy żadnych innych krawędzi podczas rysowania nowych – mamy taką możliwość, ponieważ żyjemy w przestrzeni $\reals\times\reals$, która daje nam nieskończoną precyzję i nieskończone możliwości kładzenia kolejnych krawędzi i wierzchołków :).
