---
lang: 'pl'
title: 'Lista-2'
author: 'Jerry Sky'
---

---

- [Zadanie 1](#zadanie-1)
- [Zadanie 2](#zadanie-2)
- [Zadanie 3](#zadanie-3)

---

> Celem listy jest praktyczne przećwiczenie metaheurystyk opartych na symulowanym wyżarzaniu. Dobór parametrów (np. temperatura początkowa, tempo wychładzania czy też poziom akceptacji) należy do autora programu. W czasie rozwiązywania listy autor powinien rozpoznać jaki wpływ na działanie programu (czas działania, wymagania pamięciowe, osiągany rezultat, podatność na utknięcia w lokalnym minimum, … ) mają poszczególne parametry.

## Zadanie 1

> Napisz program, który za pomocą symulowanego wyżarzania znajdzie minimum funkcji Salomona zadanej wzorem
> $$
> f(\overline{x}) = 1 - \cos\left( 2\pi\sqrt{\sum_{i=1}^{4}x_i^2} \right) + 0.1\sqrt{\sum_{i=1}^{4}x_i^2}
> $$
> **In**: Piątka liczb całkowitych `t x1 x2 x3 x4` oddzielonych spacją.\
> `t` – maksymalna liczba sekund, która może wykonywać się program w tym uruchomieniu, $x =$ $($`x1, x2, x3, x4`$)$ – jest rozwiązaniem początkowym (podane liczby zawsze są całkowite, program natomiast może je interpretować jako dowolny typ liczbowy).
>
> **Out**: 5 liczb typu `double` oddzielonych spacją, z czego cztery pierwsze to $\overline{x}$, natomiast piąta to wartość odpowiedniej funkcji w punkcie $\overline{x}$.

[code](z1/main.py)

## Zadanie 2

> Napisz program, który dla przedstawionej macierzy liczb całkowitych (zakres wartości między $0$ a $255$, można przyjąć typ `uint8` lub odpowiednik) $M$, znajdzie najbliższą macierz $M'$, spełniającą poniższe ograniczenia
> - wykorzystujemy co najwyżej $8$ różnych wartości liczbowych: $0, 32, 64, 128, 160, 192, 223, 255$,
> - macierz wynikowa $M'$ składa się z bloków $a \times b$, takich że $a \ge k$ i $b \ge k$, wewnątrz jednego bloku wszystkie liczby mają równą wartość,
> - odległość między macierzami $M$ i $M'$, rozmiaru $n\times m$, liczymy jako $d_{MSE}(M, M') = \frac{1}{nm}\sum_{i=1}^n\sum_{j=1}^m (M(i,j) - M'(i,j))^2$
>
> **In**: Dane wejściowe składać się będą z $n+1$ linii. W pierwszej linii będą umieszczone, oddzielone spacją liczby całkowite `t`, $n$, $m$, $k$, gdzie `t` jest limitem czasu, jak w zadaniu 1, natomiast $n$ i $m$ oznaczają wymiary macierzy początkowej $M$, a $k$ jest parametrem odpowiadającym za rozmiar bloków w macierzy wynikowej $M'$. W kolejnych $n$ liniach będą znajdowały się wartości kolejnego wiersza macierzy (dokładnie $m$ liczb oddzielonych spacjami). Przykładowe dane wejściowe można znaleźć [tu](z2/l2z2a.txt) i [tutaj](z2/l2z2b.txt).
>
> **Out**: Na standardowym wyjściu znaleźć się powinna jedynie odległość pomiędzy $M$ a $M'$. Na standardowym wyjściu błędów powinna być jedynie macierz $M'$, przedstawiona jako $n$ wierszy, w każdym dokładnie $m$ liczb całkowitych z określonego przedziału, oddzielonych spacją.

[code](z2/main.py)

## Zadanie 3

> Napisz program, który będzie symulował poruszanie się agenta po kracie (wycinek $\mathbb{Z}^2$). Celem jest dotarcie agenta do wyznaczonego punktu, przy założeniach, że w każdym kroku może poruszyć się o $1$ w lewo, o $1$ w prawo, o $1$ w górę albo o $1$ w dół. Program powinien za pomocą symulowanego wyżarzania generować kolejne sekwencje kroków, tak by dotarcie do celu zajęło jak najmniej rund. Jeśli agent dotrze do celu przed wykonaniem wszystkich kroków, liczymy liczbę wykonanych kroków, jeśli po wykonaniu całej wygenerowanej sekwencji kroków, agent nie dotarł do celu - kontynuuje z miejsca, w którym wylądował a długość wykonanej sekwencji wlicza się do bieżącego rozwiązania albo zaczyna nową iterację.
>
> **In**: Dane wejściowe składać się będą z $n+1$ linii. W pierwszej linii będą umieszczone, oddzielone spacją liczby całkowite `t`, $n$ i $m$, gdzie `t` jest limitem czasu, jak w zadaniu 1, natomiast $n$ i $m$ oznaczają wymiary kraty (odpowiednio liczba wierszy i kolumn w labiryncie, który będzie chciał opuścić agent). W kolejnych $n$ liniach będą znajdowały się cyfry tworzące labirynt. Między cyframi nie będzie spacji. Możliwe cyfry:
> - 0 – standardowe, puste pole, po którym agent może się poruszać
> - 1 – ściana, która nie może zostać pokonana (Uwaga: ściany mogą znajdować się również wewnątrz labiryntu, nie ma wymagania by przynajmniej jednym sąsiadem `1` była `1`; ściany mogą całkowicie blokować dostęp do części labiryntu, pod warunkiem, że istnieje ścieżka z pozycji startowej agenta do przynajmniej jednego wyjścia.).
> - 5 – symbol agenta, oznaczający jego pozycję początkową (Uwaga: nie ma
konieczności wizualizacji kolejnych kroków).
> - 8 – symbol wyjścia, oznaczający pozycję celu, na który agent powinien dotrzeć (Uwaga: w danej instancji może być więcej niż jeden symbol 8, wszystkie 8 znajdują się on na obrzeżu).
>
> Uwaga: Agent nie zna swojej pozycji początkowej, ani pozycji celu. Można założyć, że agent potrafi rozpoznać rodzaj pola (cyfrę) swoich czterech sąsiadów oraz, że zna $n$ oraz $m$. Przykładowe dane wejściowe można znaleźć [tu](z3/l2z3a.txt), [tutaj](z3/l2z3b.txt) i [tutaj](z3/l2z3c.txt). Przykłady z [listy pierwszej](../l1/readme.md) są również prawidłowymi przykładami dla listy 2.
>
> **Out**: Na standardowym wyjściu znaleźć się powinna jedynie łączna liczba kroków $k$ od pozycji startowej do celu, wykonana w wybranym rozwiązaniu. Ostatnią linią na standardowym wyjściu błędów powinien być $k$-elementowy ciąg znaków `U`, `D`, `R`, `L` oznaczający kolejne wybrane kierunki w rozwiązaniu, gdzie litery kodują odpowiednio krok w górę, krok w dół, krok w prawo i krok w lewo.

[code](z3/main.py)
