---
lang: 'pl'
title: 'Lista-3'
author: 'Jerry Sky'
---

---

- [Zadanie 1](#zadanie-1)
- [Zadanie 2](#zadanie-2)
- [Zadanie 3](#zadanie-3)

---

> Celem listy jest praktyczne przećwiczenie metaheurystyk populacyjnych. Dobór parametrów (np. kodowanie, liczność populacji, liczba iteracji, operatory stochastyczne) należy do autora programu. W czasie rozwiązywania listy autor powinien rozpoznać jaki wpływ na działanie programu (czas działania, wymagania pamięciowe, osiągany rezultat, podatność na utknięcia w lokalnym minimum, … ) mają poszczególne parametry.

## Zadanie 1

> Napisz program, który za pomocą wybranego algorytmu populacyjnego (sugerowane podejście: rój cząstek lub algorytm genetyczny z reprezentowaniem genów przez liczbę rzeczywistą) znajdzie minimum funkcji X.S. Yang zadanej wzorem
> $$
> f(\overline{x}) = \sum_{i=1}^5\mathcal{E}_i |x_i|^i
> $$
> dla $\mathcal{E}_i$ będących niezależnymi zmiennymi losowymi z rozkładu jednostajnego na $[0, 1]$.
>
> **In**: 11 liczb (6 całkowitych i 5 typu `double`) `t x1 x2 x3 x4 x5` $\mathcal{E}_1~ \mathcal{E}_2~ \mathcal{E}_3~ \mathcal{E}_4~ \mathcal{E}_5$ oddzielonych spacją.\
> `t` – maksymalna liczba sekund, którą może wykonywać się program w tym uruchomieniu, $\overline{x} = ($`x1, x2, x3, x4, x5`$)$ – jest rozwiązaniem początkowym (podane liczby zawsze są całkowite, program natomiast może je interpretować jako dowolny typ liczbowy). $\mathcal{E}_i$ są współczynnikami funkcji reprezentowanymi przez liczby typu `double`.\
> Uwaga: Dla każdego $i$ $|x_i| \le 5$.
>
> **Out**: 6 liczb typu `double` oddzielonych spacją, z czego cztery pierwsze to $\overline{x}$, natomiast ostatnia to wartość funkcji w punkcie $\overline{x}$.

[code](z1/main.py)

## Zadanie 2

> Napisz program, który za pomocą algorytmu genetycznego będzie generował słowa, które można ułożyć z otrzymanego multizbioru liter, należące do załączonego słownika, maksymalizując ich punktację. Zakładamy, że w folderze bieżącym pliku main znajduje się słownik dopuszczalnych słów [`dict.txt`](z2/dict.txt) (testy mogą być prowadzone dla mniejszego słownika, nie będą prowadzone dla słownika liczniejszego od przykładowego, ograniczamy się do ASCII), który służy do weryfikacji dopuszczalności uzyskanego rozwiązania. Słowo uważane jest za niedopuszczalne również wtedy, gdy nie można go ułożyć z dostępnych liter (liczba kopii jest brana pod uwagę). Jeśli rozwiązanie jest dopuszczalne, za jego punktację przyjmujemy sumę punktów wszystkich liter, które się na nie składają.
>
> **In**: Wejście składać się będzie z $n + s + 1$ linii. W pierwszej linii znajdować się będą trzy liczby całkowite oddzielone spacjami: `t` $n$ $s$. Liczba `t` jest ograniczeniem czasowym jak w zadaniu pierwszym, liczba $n$ określa rozmiar multizbioru liter, $s$ oznacza liczbę zadanych na wejściu rozwiązań dopuszczalnych. W kolejnych $n$ liniach znajdować się będą oddzielone spacją pary $c_i$ $p_i$, gdzie $c_i$ jest $i$-tym elementem multizbioru ($i$-tą literą), natomiast $p_i$ jej wartością punktową. Można przyjąć, że wszystkie kopie tej samej litery mają identyczną wartość punktową. W $s$ ostatnich liniach znajdować się będą kolejno słowa (bez rozdzielających litery spacji) będące dopuszczalnymi rozwiązaniami dla danego wywołania.\
> Przykładowe dane wejściowe można znaleźć [tu](z2/l3z2a.txt) i [tutaj](z2/l3z2b.txt).
>
> **Out**: Na standardowym wyjściu powinna zostać zwrócona liczba całkowita będąca sumą punktów uzyskanego rozwiązania. Na standardowym wyjściu błędów powinno zostać wypisane rozwiązanie końcowe (w przypadku większej ilości informacji, słowo końcowe powinno być jedynym ciągiem znaków w ostatniej linii `stderr`).
>
> Uwaga: Słownik zawsze będzie uporządkowany w kolejności alfabetycznej. W ramach preprocessingu można reorganizować słownik (np. drzewo prefiksowe) natomiast `t` jest ograniczeniem na całkowity czas działania programu.\
> Uwaga 2: Zakładamy, że kapitalizacja liter nie ma znaczenia.

[code](z2/main.py)

## Zadanie 3

> Napisz program, który będzie symulował poruszanie się agenta po kracie (wycinek $\mathbb{Z}^2$). Celem jest dotarcie agenta do wyznaczonego punktu, przy założeniach, że w każdym kroku może poruszyć się o $1$ w lewo, o $1$ w prawo, o $1$ w górę albo o $1$ w dół. Program powinien za pomocą symulowanego wyżarzania generować kolejne sekwencje kroków, tak by dotarcie do celu zajęło jak najmniej rund. Jeśli agent dotrze do celu przed wykonaniem wszystkich kroków, liczymy liczbę wykonanych kroków, jeśli po wykonaniu całej wygenerowanej sekwencji kroków, agent nie dotarł do celu - kontynuuje z miejsca, w którym wylądował a długość wykonanej sekwencji wlicza się do bieżącego rozwiązania albo zaczyna nową iterację.
>
> **In**: Dane wejściowe składać się będą z $n + s + 1$ linii. W pierwszej linii będą umieszczone, oddzielone spacją liczby całkowite `t`, $n$, $m$, $s$ i $p$ , gdzie $t$ jest limitem czasu, jak w zadaniu 1, $n$ i $m$ oznaczają wymiary kraty (odpowiednio liczba wierszy i kolumn w labiryncie, który będzie chciał opuścić agent). Liczba całkowita $s$ oznacza liczbę danych na wejściu rozwiązań początkowych, natomiast $p \ge s$ określa górne ograniczenie na liczebność populacji. W kolejnych $n$ liniach będą znajdowały się cyfry tworzące labirynt. Między cyframi nie będzie spacji. W ostatnich s liniach będą znajdować się ciągi znaków `U`, `D`, `R`, `L` prowadzące z punktu startowego do jednego z wyjść (ciągi mogą być różnej długości, mogą prowadzić do różnych wyjść). Możliwe cyfry:
> - 0 – standardowe, puste pole, po którym agent może się poruszać
> - 1 – ściana, która nie może zostać pokonana (Uwaga: ściany mogą znajdować się również wewnątrz labiryntu, nie ma wymagania by przynajmniej jednym sąsiadem `1` była `1`; ściany mogą całkowicie blokować dostęp do części labiryntu, pod warunkiem, że istnieje ścieżka z pozycji startowej agenta do przynajmniej jednego wyjścia.).
> - 5 – symbol agenta, oznaczający jego pozycję początkową (Uwaga: nie ma konieczności wizualizacji kolejnych kroków).
> - 8 – symbol wyjścia, oznaczający pozycję celu, na który agent powinien dotrzeć (Uwaga: w danej instancji może być więcej niż jeden symbol 8, nie wszystkie 8 muszą się znajdować na obrzeżu).
>
> Uwaga: Agent nie zna swojej pozycji początkowej, ani pozycji celu. Można założyć, że agent potrafi rozpoznać rodzaj pola (cyfrę) swoich czterech sąsiadów oraz, że zna $n$ oraz $m$.\
> Przykładowe dane wejściowe można znaleźć [tu](z3/l3z3a.txt), [tutaj](z3/l3z3b.txt) i [tutaj](z3/l3z3c.txt). Przykłady z list wcześniejszych mają inny format wejścia zatem przed użyciem na L3 muszą zostać zmodyfikowane.
>
> **Out**: Na standardowym wyjściu znaleźć się powinna jedynie łączna liczba kroków $k$ od pozycji startowej do celu, wykonana w wybranym rozwiązaniu. Ostatnią linią na standardowym wyjściu błędów powinien być $k$–elementowy ciąg znaków `U`, `D`, `R`, `L` oznaczający kolejne wybrane kierunki w rozwiązaniu, gdzie litery kodują odpowiednio krok w górę, krok w dół, krok w prawo i krok w lewo.

[code](z3/main.py)
