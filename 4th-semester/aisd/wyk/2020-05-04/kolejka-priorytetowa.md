# Kolejka priorytetowa

## Operacje

*Zakładamy tutaj, że im mniejszy klucz tym element ma wyższy priorytet.*

### `MakeQueue`$(A)$

Tworzy kolejkę priorytetową z tablicy $A$ elementów posiadających priorytety.

### `Insert`$(Q, \mathrm{key})$

Wstawia element o kluczu $\mathrm{key}$ do kolejki $Q$.

### `Minimum`$(Q)$

Zwraca element należący do $Q$ o najmniejszym kluczu, czyli najwyższym priorytecie *(nie usuwa go z $Q$)*

### `ExtractMin`$(Q)$

Wykonuje `Minimum`$(Q)$, a następnie usuwa zwrócony element z $Q$.

### `DecreaseKey`$(Q,i)$

Informuje kolejkę, że element $Q[i]$ ma zmniejszony klucz (zwiększony priorytet), może to skutkować przesunięciem elementu $Q[i]$ w kolejce.

### `Union`$(Q_1, Q_2)$

Zwraca kolejkę będącą złączeniem kolejek $Q_1$ oraz $Q_2$.

### `Delete`$(Q,i)$

Usuwa element $Q[i]$ z kolejki $Q$.

## Implementacja kolejki przy pomocy [kopca binarnego](../2020-04-27/binary-heap.md)

### `MakeQueue`$(A)$ (Binary heap)

Procedura ta może zostać zaimplementowana przy użyciu procedury [`BuildHeap`$(A)$](../2020-04-27/binary-heap.md#buildheapa), która ma złożoność obliczeniową $O(n)$, gdzie $n$ jest długością tablicy $A$.

### `Insert`$(Q,\mathrm{key})$ (Binary heap)

Procedura ta będzie dodawać nowy element w pierwszym możliwym miejscu (nowy liść), a następnie idąc w górę kopca (działając podobnie do [`Heapify`](../2020-04-27/binary-heap.md#heapifyai) ale od dołu do góry) będzie szukane gdzie umiejscowiony zostanie nowy element.

1. $Q.\mathrm{size}$`++`
2. $i = Q.\mathrm{size}$
3. `while` $i > 1 \land Q[\mathrm{parent}(i)] > \mathrm{key}$:
   1. $Q[i] = Q[\mathrm{parent}(i)]$
   2. $i = \mathrm{parent}(i)$
4. $Q[i] = \mathrm{key}$

Złożoność obliczeniowa: nowy klucz będzie przesuwany w górę kopca wykonując $O(1)$ operacji na każdym jego poziomie.\
Zatem wiedząc, że wysokość kopca o $n$ elementach to $O(\lg n)$ wiemy, że złożoność obliczeniowa tej procedury wynosi $O(\lg n)$

### `Minimum`$(Q)$ (Binary heap)

`return` $Q[1]$

Kopiec jest zapisywany w tablicy $Q$, zakładając, że jest to kopiec minimalny jego pierwszy element będzie miał najmniejszy klucz. Złożoność obliczeniowa to $\Theta(1)$.

### `ExtractMin`$(Q)$ (Binary heap)

1. `if` $Q.\mathrm{size} < 1$:
   1. `return` $\text{„empty queue”}$
2. `else`:
   1. $\min = Q[1]$
   2. $Q[1] = Q[Q.\mathrm{size}]$
   3. $Q.\mathrm{size}$`--`
   4. `Heapify`$(Q,1)$
   5. `return` $\min$

Jeśli kopiec nie jest pusty to zapisujemy wartość w jego korzeniu, zastępujemy ją ostatnią wartością z kolejki $Q$, zmniejszamy rozmiar kolejki i przywracamy własność kopca.

Złożoność obliczeniowa: wszystkie operacje poza `Heapify`$(Q,1)$ mają złożoność $\Theta(1)$, natomiast `Heapify`$(Q,1)$ dla kolejki długości $n$ ma złożoność $O(\lg n)$.\
Zatem w sumie złożoność to $O(\lg n)$

### `DecreaseKey`$(Q,i)$

1. `while` $i > 1 \land Q[\mathrm{parent}(i)] > Q[i]$:
   1. $Q[i] = Q[\mathrm{parent}(i)]$
   2. $i = \mathrm{parent}(i)$

Niniejsza procedura jest bardzo podobna do procedury [`Insert`$(Q,\mathrm{key}$](#insertqmathrmkey-binary-heap). Jest realizowana poprzez sprawdzenie czy własność kopca binarnego jest zachowana, jeśli nie to to naprawia kopiec przesuwając odpowiedni element w górę kopca.

Podobne wnioskowanie jak w przypadku `Insert` daje nam złożoność obliczeniową $O(\lg n)$.

### `Union`$(Q_1, Q_2)$ (Binary heap)

1. $Q =$ `Join`$(Q_1, Q_2)$ $~\triangleright$ złączenie elementów dwóch tablic
2. `BuildHeap`$(Q)$

Złączenie kopców polega na przepisaniu obu kopców do jednej tablicy oraz wykonaniu procedury budowy kopca na nowej tablicy.

Złożoność obliczeniowa: zarówno połączenie dwóch tablic $Q_1, Q_2$ jak i procedura `BuildHeap`$(Q_1, Q_2)$ możemy ograniczyć asymptotycznie przez złożoność liniową od sumarycznej wielkości tych tablic. Zakładając, że $Q_1.\mathrm{size} + Q_2.\mathrm{size} = n$ dostajemy złożoność $O(n)$.

### `Delete`$(Q,i)$

1. $Q[i] = Q[Q.\mathrm{size}]$
2. $Q.\mathrm{size}$`--`
3. `Heapify`$(Q,i)$

Usuwanie elementu o indeksie $i$ z kopca polega na przesunięciu tego elementu do części tablicy, które będzie poza kopcem, zmniejszeniem wielkości kopca oraz naprawieniem własności kopca.

Złożoność obliczeniowa: operacja o największej złożoności obliczeniowej jest procedura `Heapify`$(Q,i)$, która ma złożoność $O(\lg n)$, zakładając, że $n = Q.\mathrm{size}$.

## Różne implementacje

Porównanie złożoności obliczeniowych procedur na kolejkach priorytetowych dla różnych implementacji kopców:

| Procedura     | Kopiec binarny (koszt pesymistyczny) | Kopiec dwumianowy (koszt pesymistyczny) | Kopiec Fibonacciego (koszt zamortyzowany) |
| ------------- | ------------------------------------ | --------------------------------------- | ----------------------------------------- |
| `Insert`      | $O(\lg n)$                           | $O(\lg n)$                              | $O(1)$                                    |
| `Minimum`     | $O(1)$                               | $O(\lg n)$                              | $O(1)$                                    |
| `ExtractMin`  | $O(\lg n)$                           | $O(\lg n)$                              | $O(\lg n)$                                |
| `DecreaseKey` | $O(\lg n)$                           | $O(\lg n)$                              | $O(1)$                                    |
| `Union`       | $O(n)$                               | $O(\lg n)$                              | $O(1)$                                    |
| `Delete`      | $O(\lg n)$                           | $O(\lg n)$                              | $O(\lg n)$                                |

## More

- [Chapter 6.5](https://web.ist.utl.pt/~fabio.ferreira/material/asa/clrs.pdf)
- [Chapter 4.5](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf)
- [aisd02.pdf, aisd09.pdf](https://drive.google.com/drive/folders/0B83LMR1NBoUXLXdYZ2hsNFBqTTA)
