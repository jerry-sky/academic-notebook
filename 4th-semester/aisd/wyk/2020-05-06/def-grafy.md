---
lang: 'pl'
title: 'Grafy'
author: 'Jerry Sky'
---

---

- [Graf](#graf)
- [Reprezentacja](#reprezentacja)
    - [Macierz sąsiedztwa $A$](#macierz-sąsiedztwa-a)
    - [Lista sąsiedztwa](#lista-sąsiedztwa)
- [Wielkości](#wielkości)

---

## Graf

Oznaczenie: $G = (V,E)$, $V = \{v_1, \dots, v_n\}$

## Reprezentacja

### Macierz sąsiedztwa $A$

Mamy $|V| = n$.

Macierz sąsiedztwa jest rozmiaru $n\times n$, gdzie $A = \{a_{i,j}: 1\le i,j\le n\}$ oraz
    $$
    a_{i,j} =
    \begin{cases}
      1 & \text{jeśli istnieje krawędź od }v_i\text{ do }v_j\\
      0 & \text{otherwise}
    \end{cases}
    $$

    Dla grafów nieskierowanych macierz sąsiedztwa jest symetryczna, zatem możemy przetrzymywać w pamięci tylko jej połowę. Największą zaletą reprezentacji grafy przy pomocy macierzy sąsiedztwa jest możliwość sprawdzenia istnienia krawędzi pomiędzy wybranymi wierzchołkami grafu w złożoności obliczeniowej $O(1)$.\
    Minusem takiej reprezentacji jest jej duży rozmiar $O(n^2)$, zatem jeśli w grafie mamy mało krawędzi to większość elementów macierzy to zera i jest to duża strata pamięci.

### Lista sąsiedztwa

Dla każdego wierzchołka tworzymy listę, w której przetrzymujemy sąsiadów danego wierzchołka. Rozmiar takiej reprezentacji jest proporcjonalny do liczby krawędzi w grafie $|E|$ *(dla grafów skierowanych każda krawędź pojawia się raz, dla nieskierowanych dwa razy)*.\
Wadą listy sąsiedztwa jest złożoność obliczeniowa dostępu do krawędzi grafu, która jest zależna od długości list i w pesymistycznym przypadku może być nawet $O(n)$.

Wybór reprezentacji grafu należy dostosować do kontekstu w jakim grafy będą używane oraz dostępnych informacji na temat wejściowych grafów.\
Jeśli grafy będą gęste (liczba krawędzi $\Omega(n^2)$) to preferowaną reprezentacją jest macierz sąsiedztwa. Jeśli grafy będą rzadkie to preferowaną reprezentacją może być lista sąsiedztwa.

---

## Wielkości

Przez wielkość grafu rozumiemy $|V| + |E|$, anie tylko liczbę wierzchołków $|V|$.

Przykładowo: dla grafu pełnego o liczbie wierzchołków $|V| = n$ mamy $|E| = \binom{n}{2} = \Theta(n^2)$. Jeśli zatem algorytm będzie działał w złożoności $O(n^2) = O(|E|)$ na tym grafie to będziemy mówili o liniowej złożoności względem wielkości grafu.
