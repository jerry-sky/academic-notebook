# Najdłuższy podciąg rosnący
*(2020-04-8)*

## Input
Ciąg $A = (a_1,\dots,a_n)$

## Output
Najdłuższy rosnący podciąg $A$.

Podciągiem ciągu $A$ nazywamy ciąg $(a_{i_1}, \dots, a_{i_k})$, gdzie $1 \le i_1 < \dotsb < i_k \le n$, jeśli dodatkowo ma on być rosnący to $a_{i_1} < \dotsb < a_{i_k}$.

## Przykład $A$

Mamy $A = (5,2,8,5,3,7,9,8)$.

Wówczas najdłuższy pociąg $A$ to np. $(2,3,7,9)$, ale istnieją również inne podciągi tej samej długości np. $(2,5,7,8)$.

## Steps

1. Budujemy [DAG](najkrótsza-ścieżka-dag.md) $G = (V,E,c)$ odpowiadającego naszemu problemowi.
2. Niech zbiór wierzchołków stanowią elementy ciągu wejściowego $A$: $V = \{a_1,\dots,a_n\}$.
3. Wstawiamy krawędzie tylko pomiędzy wierzchołkami, które mogą być kolejnymi elementami rosnącego podciągu, czyli $(a_i, a_j) \in E$ jeśli $i<j \land a_i < a_j$.
4. Niech waga (długość) każdej krawędzi będzie równa $1$, czyli $\forall(u,v) \in E: c(u,v) = 1$.

Zauważmy, że tak powstały graf $G$ jest DAG-iem oraz, że ścieżki w tak zdefiniowanym grafie odpowiadają podciągom rosnącym ciągu $A$. Zatem naszym zadaniem teraz jest znalezienie najdłuższej ścieżki w tak zdefiniowanym grafie.

### Znalezienie najdłuższej ścieżki

Niech $L(i)$ będzie długością najdłuższego podciągu kończącego się na elemencie $a_i$, wówczas:
```
for i = 1 to n:
  L(i) = 1 + max{ L(j): (j,i) in E }
return max{ L(i): i in [n] }
```
Podobnie jak w [problemie najkrótszej ścieżki w DAG](najkrótsza-ścieżka-dag.md), jeśli zapamiętamy $a_j$ dla którego osiągnięty jest $\max\{L(j): (j,i) \in E\}$ to możemy odtworzyć uzyskany w wyniku podciąg.

Złożoność obliczeniowa powyższego algorytmu wynosi $O(|E|)$ (podobnie jak to było w przypadku najkrótszych ścieżek w DAG), czyli w pesymistycznym przypadku $O(n^2)$, który zachodzi jeśli ciąg wejściowy jest posortowany rosnąco.

