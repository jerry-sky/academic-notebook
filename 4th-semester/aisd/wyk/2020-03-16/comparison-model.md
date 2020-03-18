# Comparison model
*(2020-03-16)*

## Binarne drzewo decyzyjne

Wszystkie dotychczas omówione algorytmy sortowania ([`InsertionSort`](../2020-03-3/insertion-sort.md), [`MergeSort`](../2020-03-3/merge-sort.md), [`QuickSort`](../2020-03-11/quick-sort.md)) zakładały, że aby ustalić kolejność elementów możemy je tylko porównywać między sobą - jest to tzw. *Comparison Model*. Przy użyciu binarnego drzewa decyzyjnego możemy udowodnić, że liczba porównań między sortowanymi elementami musi wynosić co najmniej $\log(n!) = O\big(n\log n\big)$.

Weźmy drzewo sortujące biorące za argument tablicę $n$-elementową. Każdy z liści takiego drzewa jest permutacją $\{1,2,\dots,n\}$. Mamy więc przynajmniej $n!$ liści. Warto zauważyć, że w drzewie binarnym o głębokości $d$ jest co najwyżej $2^d$ liści.

Wówczas głębokość naszego drzewa i złożoność algorytmu sortującego zarazem wynosi $\log(n!)$.\
Za to $\log(n!) \ge c\cdot n \log n$ dla pewnych $c > 0$ jest znanym faktem. Chociażby $n! \ge \big(\frac{n}{2}\big)^{\frac{n}{2}}$, ponieważ $n! = 1\cdot 2 \dotsb n$ zawiera przynajmniej $\frac{n}{2}$ współczynników większych od $\frac{n}{2}$ - wówczas wystarczy nałożyć $\log$ na obie strony nierówności.

W takim razie już wiemy, że w najgorszym przypadku mamy $\Omega(n\log n)$ porównań.

Source: [Algorithms: Dasgupta, Papadimitriou, Vazirani](http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf) - end of paragraph 2.3
