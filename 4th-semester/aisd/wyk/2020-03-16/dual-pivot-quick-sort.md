# Dual-pivot `QuickSort`

## Algorytm sortujący Dual-pivot `QuickSort`

Należy zauważyć, że używając dwóch pivotów $p < q$ dzielimy tablicę sortowaną na trzy pod-tablice:
- elementy mniejsze od $p$
- elementy pomiędzy $p$ a $q$
- elementy większe od $q$

W takim przypadku liczba porównań pomiędzy kluczami (elementami sortowanymi) jest zmienną losową, a nie deterministyczną funkcją zależną od $n$ *(jak to było w zwyczajnym `QuickSort`'cie)*.

Historia `QuickSort`'a z dwoma i więcej pivotami:
- *1975*: Sedgewick: $\bold E(\#porównań) = \frac{32}{15}n\ln n + O(n)$ oraz $\bold E(\# porównań~w~Partition) = \frac{16}{9}n + o(n)$
- *2009*: Yaroslavsky: $\bold E(\#porównań) = \frac{19}{10}n \ln n + O(n)$ oraz $\bold E(\#porównań~w~Partition) = \frac{19}{12}n + o(n)$ - algorytm zaimplementowany w *Java 7*
- *2015*: Aumüller i Dietzfelbinger: $\bold E(\#porównań) - \frac{9}{5}n\ln n + O(n)$ oraz $\bold E(\#porównań~w~Partition~Count) = \frac{3}{2}n + o(n)$. Zaproponowana strategia Count okazuj się również optymalną (w sensie pierwszy składnik wartości oczekiwanej liczby porównań dla Dual-pivot QuickSort nie może być mniejszy niż $\frac{9}{5}n\ln n$).

## Krótki zarys działania
Najlepiej zaznajomić się ze [standardowym *(singular-pivot)* `QuickSort`em](../2020-03-11/quick-sort.md) przed przeczytaniem poniższej listy działania.
- mamy dwa pivoty $p$ oraz $q$ takie, że $p < q$
- załóżmy, że w procedurze `partition` klasyfikując $i$ty element tablicy mamy $s_{i-1}$ elementów $<p$ oraz $l_{i-1}$ elementów $>q$
- jeśli $l_{i-1} > s_{i-1}$ to porównuj $i$ty element w pierwszej kolejności z $q$, a następnie, jeśli jest taka potrzeba, z $p$
- jeśli $l_{i-1} < s_{i-1}$ to porównuj $i$ty element w pierwszej kolejności z $p$, a następnie jeśli jest taka potrzeba, z $q$
