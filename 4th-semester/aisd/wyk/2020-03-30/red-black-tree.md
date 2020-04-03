# Drzewa czerwono-czarne
*(2020-03-30)*

## Introduction
Na [poprzednim wykładzie](../2020-03-25/binary-search-tree.md) poznaliśmy strukturę BST, które pozwalają zaimplementować operacje na zbiorach dynamicznych w złożoności obliczeniowej $O(h)$, gdzie $h$ jest [wysokością BST](../2020-03-25/binary-search-tree.md#wysokość-bst).\
Operacje te działają więc szybko, jeżeli wysokość drzewa przeszukiwań jest mała. Jeśli jednak wysokość drzewa jest duża $h = O(n)$, to koszty operacji mogą być równie duże jak dla zwykłych list.\
Dlatego powstało dużo modyfikacji BST *(drzewa czerwono-czarne, drzewa AVL etc.)*, które pozwalają utrzymać drzewa poszukiwań w postaci zbalansowanej, czyli wysokość drzewa w pesymistycznym przypadku można ograniczyć przez $\Theta(\log n)$.\
Teraz zajmiemy się **drzewami czerwono-czarnymi** *(RB-Trees)*.

## Warunki na RB-Tree
1. Każdy węzeł drzewa przechowuje dodatkową informację: kolor węzła - czerwony albo czarny
2. Każdy liść przechowujący wartość $\mathrm{NIL}$ jest czarny
3. Jeśli węzeł jest czerwony, to obaj jego potomkowie są czarni
4. Każda prosta ścieżka z ustalonego węzła do liścia ma tyle samo czarnych węzłów (liczbę tę nazywamy czarną wysokością węzła i oznaczamy przez $bh()$)

## Lemma A
RB-Tree o $n$ kluczach ma wysokość co najwyżej $2\lg(n+1)$ (czyli $h \le 2\lg(n+1) = \Theta(\log n)$).

### D-d Lemma A

1. Rozpatrzmy drzewo $T'$ powstałe z RB-Tree $T$ o $n$ kluczach (czyli $2n+1$ węzłach licząc razem z liśćmi) poprzez złączenie każdego czerwonego węzła z jego czarnym rodzicem. Tak powstałe drzewo $T'$ (2-3-4-tree) ma węzły zawierające jeden, dwa lub trzy klucze i odpowiednio dwa, trzy lub cztery pod-drzewa. Wysokość tak powstałego drzewa $h'$ jest równa czarnej wysokości korzenia oryginalnego drzewa $T$ $(h' = bh(T))$.\
Liczba liści (przechowujących wartość $\mathrm{NIL}$) jest taka sama dla RB-Tree i drzewa powstałego po transformacji $T'$ i jest równa $n+1$.
2. Zauważmy, że liczbę liści drzewa $T'$ możemy ograniczyć przez
    $$
    2^{h'} \le \#liści \le 4^{h'}
    $$
    a zatem $h' \le \lg(n+1)$.
3. Zauważmy również, że wysokość RB-Tree $T$ może wynosić maksymalnie $2bh(T) = 2h'$.\
Zatem $h \le 2\lg(n+1)$.

## Operacje

Operacje dodawania i usuwania węzłów z drzewa znane z [poprzedniego wykładu](../2020-03-25/binary-search-tree.md) w oczywisty sposób nie zachowują własności (porządku) RB-Tree, dlatego należy je rozszerzyć.\
Rozszerzenia te będą wykonywały rekonstrukcję drzewa po której własności RB-Tree będą spełnione.\
Wykorzystywane będą dwie procedury:

### $\mathrm{Recolor}(x, color)$
Ustawia $color$ jako kolor węzła $x$.\
Złożoność obliczeniowa $O(1)$.

### $\mathrm{Rotate_{right}}(T,x)$, $\mathrm{Rotate_{left}}(T,x)$
Są to operacje odpowiednio prawej i lewej rotacji drzewa. Podczas rotacji drzewa względem węzła $x$, węzeł $x$ jest zastępowany swoim odpowiednim potomkiem $y$ (dla prawej rotacji lewym potomkiem, dla lewej rotacji prawym potomkiem), $x$ staje się potomkiem $y$ (dla prawej rotacji prawym potomkiem, dla lewej lewym), a odpowiednie pod-drzewa $x$ i $y$ są przepinane w taki sposób aby własność BST była zachowana.\
Złożoność obliczeniowa rotacji to $O(1)$.

### $\mathrm{Insert_{RB}}$, $\mathrm{Delete_{RB}}$
Operacje $\mathrm{Insert_{RB}}$, $\mathrm{Delete_{RB}}$ mają asymptotyczną złożoność obliczeniową $O(h)$, czyli taką jak w przypadku operacji $\mathrm{Insert}$ oraz $\mathrm{Delete}$ w zwykłym BST.\
Natomiast jasne jest, że stała występujące przy $h$ będzie większa.

## Sources

Więcej informacji na temat RB-Trees można znaleźć tutaj:
- [Chapter 13](https://web.ist.utl.pt/~fabio.ferreira/material/asa/clrs.pdf)
- [tu](https://algs4.cs.princeton.edu/33balanced/)
- [dr Kik - aisd04.pdf](https://drive.google.com/drive/folders/0B83LMR1NBoUXLXdYZ2hsNFBqTTA)

