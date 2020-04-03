# Binary Search Tree *(BST)*
*(2020-03-25)*

## Description

Drzewa poszukiwań binarnych (ukorzenione drzewa, każdy węzeł ma dwóch potomków, liście mają zero potomków) są strukturami danych, na których można wykonywać różne operacje na zbiorach dynamicznych takie jak $\mathrm{Search},~\mathrm{Minimum},~\mathrm{Maximum},~\mathrm{Predecessor},~\mathrm{Successor},~\mathrm{Insert},~\mathrm{Delete}$.

## Węzeł drzewa

Węzeł drzewa składa się z:
1. $\mathrm{key}$ - wartość ze zbioru dynamicznego $A$, którą możemy porównać z każdym innym elementem należącym do $A$
2. $\mathrm{left}$ - wskaźnik na lewego potomka
3. $\mathrm{right}$ - wskaźnik na prawego potomka
4. $\mathrm{parent}$ - wskaźnik na rodzica *(opcjonalny)*

## Porządek w BST

Niech $x$ będzie węzłem BST $T$. Jeśli $y \in$ lewe pod-drzewo $x$ wtedy $y.\mathrm{key} \le x.\mathrm{key}$, w przeciwnym przypadku $y.\mathrm{key} \ge x.\mathrm{key}$.

## Wysokość BST

Istotnym parametrem BST jest jego wysokość $h$, czyli najdłuższa ścieżka między korzeniem drzewa, a liściem.

## Operacje dla BST

### $\mathrm{InorderTreeWalk}$
Operacja pozwalająca na przechodzenie drzewa w uporządkowany sposób. Operacja ta wywołana na drzewie o $n$ węzłach ma złożoność obliczeniową $\Theta(n)$.

### $\mathrm{Search}(x)$
Operacja pozwalająca wyszukać węzeł w drzewie BST, którego pole $\mathrm{key} == x$.\
Jeśli taki element nie istnieje to zwraca $\mathrm{null}$.\
Operacja ta ma złożoność obliczeniową $O(h)$ gdzie $h$ to [wysokość BST](#wysoko%c5%9b%c4%87-bst).

### $\mathrm{Insert}(x)$
Operacja wstawiająca nowy węzeł do BST, którego pole $\mathrm{key} := x$.\
Operacja ta zachowuje oczywiście [porządek w BST](#porz%c4%85dek-w-bst) do którego wstawiany jest nowy element.\
Operacja ta ma złożoność obliczeniową $O(h)$.

### $\mathrm{Delete}(x)$
Operacja usuwająca element $x$ z BST.\
Operacja ta jest bardziej złożona niż poprzednie, należy w niej rozpatrzeć czy usuwany węzeł jest:
- liściem drzewa
- ma jedno pod-drzewo, które nie jest węzłem $\mathrm{null}$owym
- ma dwa pod-drzewa, które nie są węzłami $\mathrm{null}$owymi

Operacja ta zachowuje oczywiście [porządek w BST](#porz%c4%85dek-w-bst), z którego usuwany jest węzeł $x$.\
Operacja ta ma złożoność obliczeniową $O(h)$.

### $\mathrm{Minimum}$
Operacja zwraca element BST o najmniejszej wartości pola $\mathrm{key}$, czyli element *„najbardziej po lewej stronie w drzewie”*.\
Operacja ta ma złożoność obliczeniową $O(h)$.

### $\mathrm{Maximum}$
Operacja zwraca element BST o największej wartości pola $\mathrm{key}$, czyli element *„najbardziej po prawej stronie w drzewie”*.\
Operacja ta ma złożoność obliczeniową $O(h)$.

### $\mathrm{Successor}(x)$
Operacja zwraca węzeł BST, którego wartość pola $\mathrm{key}$ jest następnikiem węzła $x$, czyli węzeł o najmniejszej wartości pola $\mathrm{key}$ większej niż $x.\mathrm{key}$ *(zakładając, że wszystkie klucze w drzewie są różne)*.
Operacja ta ma złożoność obliczeniową $O(h)$.

### $\mathrm{Predecessor}(x)$
Operacja analogiczna do [$\mathrm{Successor}$](#mathrmsuccessorx), zwracająca poprzednika węzła $x$.

### $\mathrm{BSTSort}$
Rozpatrzmy operację $\mathrm{BSTSort}$, która wstawia do BST wszystkie elementy zbioru $A=(a_1,\dots,a_n)$, a następnie wykonuje na tym drzewie $\mathrm{InorderTreeWalk}$.\
Wynikiem będzie wypisanie posortowanego ciągu elementów ze zbioru $A$. Warto zauważyć, że $\mathrm{BSTSort}$ wykonuje te same porównania co [$\mathrm{QuickSort}$](../2020-03-11/quick-sort.md) wykonany na zbiorze $A$ *(tylko może w innej kolejności)*.

Załóżmy, że wejściem do naszego algorytmu jest losowa permutacja elementów tablicy $A$.\
Wiedząc [z wcześniejszego wykładu](../2020-03-16/dual-pivot-quick-sort.md), że w $\mathrm{QuickSort}$cie $E(\#\text{porównań}) = \Theta(n\log n)$.\
W takim razie dla BST:
$$
\mathrm{E}(\text{średnia głębokość węzła w drzewie BST}) = \Theta(\log n)
$$
gdzie **głębokością węzła $x$ w BST jest jego odległość od korzenia drzewa**.\
Niestety, z tego faktu **nie** możemy wywnioskować, że wysokość drzewa jest również logarytmiczna *(istnieje drzewo o średniej głębokości węzła $\Theta(\log n)$ oraz wysokości $\Theta\left(\sqrt{n}\right)$*

## Własność #2
Zauważmy, że jeśli do BST wstawimy $n$ elementów w uporządkowanej kolejności to jego wysokość będzie wynosić $h=n$.

## Twierdzenie #1

$\mathrm{E}(\text{wysokości BST o }n\text{ węzłach}) = O(\log n)$ zakładając, że kolejność wstawianych elementów do drzewa jest zadana przez losową permutację.

### D-d Twierdzenia #1

1. Zamiast analizować zmienną losową wysokości drzewa $H_n$, analizujemy zmienną $Y_n = 2^{H_n}$.
2. Wykorzystując indukcję dowodzimy, że $\mathrm{E}(Y_n) = O(n^3)$
3. Wykorzystując nierówność Jensena oraz powyżej udowodnioną równość na wartości oczekiwanej $Y_n$ otrzymujemy $\mathrm{E}(H_n) \le 3\log(n) + O(1)$. Luc Devroye w 1986r pokazał, że $\mathrm{E}(H_n) = 2.9882\dots\log(n) + o(\log n)$

## Sources

Więcej informacji na temat BST można znaleźć [tu (Chapter 12)](https://web.ist.utl.pt/~fabio.ferreira/material/asa/clrs.pdf) oraz [tutaj](https://algs4.cs.princeton.edu/32bst/).

