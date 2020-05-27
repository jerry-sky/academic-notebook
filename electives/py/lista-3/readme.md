# Lista 3

## Zadanie 1

> Załóżmy, że reprezentujemy macierze kwadratowe w Pythonie następująco (dla rozmiaru macierzy n=3):\
>    `["1.1 2.2 3.3", "4.4 5.5 6.6", "7.7 8.8 9.9"]`\
> Napisz funkcję wykorzystując tylko listy składane, która dokonuje transpozycji takich macierzy (dowolnych rozmiarów) oraz zwraca wynik w tej samej postaci (można to zrobić w jednej linii kodu!).

Mamy
$$
A =
\begin{bmatrix}
  1.1 & 2.2 & 3.3 \\
  4.4 & 5.5 & 6.6 \\
  7.7 & 8.8 & 9.9 \\
\end{bmatrix}
$$
Transponujemy $A$ i mamy
$$
A^T =
\begin{bmatrix}
  1.1 & 4.4 & 7.7 \\
  2.2 & 5.5 & 8.8 \\
  3.3 & 6.6 & 9.9 \\
\end{bmatrix}
$$

[kod](ex-1.py)

Żeby szybko przetestować program, można edytować plik `matrix-test.txt` i uruchomić program używając `./ex-1.py matrix-test.txt`.

## Zadanie 2

> Napisz generator o nazwie "flatten", który przechodzi dowolną listę (również zagnieżdżoną) i podaje po kolei jej elementy: Na przykład dla listy
>```py
> l = [[1, 2, ["a", 4, "b", 5, 5, 5]], [4, 5, 6 ], 7, [[9, [123, [[123]]]], 10]]
> ```
>
> Po wywołaniu: print(list(flatten(l))), otrzymujemy:
> ```py
> [1, 2, 'a', 4, 'b', 5, 5, 5, 4, 5, 6, 7, 9, 123, 123, 10]
> ```

[kod](ex-2.py)

W celu szybkiego testu programu można zmienić plik `flatten-example.json` i uruchomić program używając `./ex-2.py flatten-example.json`.

## Zadanie 3

> Wykorzystując, tylko listy składane (jako generatory) napisz program, który odczytuje plik tekstowy następnie pobiera ostatnią kolumnę, która zawiera informację o wielkości pliku, sumuje i wynik wyświetla na ekranie. Przykład pliku:
> ```
>  127.0.0.1 -  - "GET /ply/  HTTP/1.1" 200 7587
>  127.0.0.1 -  - "GET /favicon.ico HTTP/1.1" 404 133
>  127.0.0.1 -  - "GET /ply/bookplug.gif" 200 23903
>  127.0.0.1 -  - "GET /ply/ply.html HTTP/1.1" 200 97238
>  127.0.0.1 -  - "GET /ply/example.html HTTP/1.1" 200 2359
>  127.0.0.1 -  - "GET /index.html" 200 4447
> ```
> Dostajemy wynik:\
>    `Całkowita liczba bajtów: 135667`


[kod](ex-3.py)

W celu szybkiego testu programu można zmienić plik `column-sum-example.txt` i uruchomić program używając `./ex-3.py column-sum-example.txt`.

## Zadanie 4

> Rozważmy algorytm QuickSort napisany w języku Haskell:
> ```haskel
> qsort [] = []
> qsort (x:xs) = qsort elts_lt_x ++ [x] ++ qsort elts_greq_x
>                  where
>                    elts_lt_x = [y | y <- xs, y < x]
>                    elts_greq_x = [y | y <- xs, y >= x]
> ```
> Napisz podobny program w języku Python wykorzystując
> - składnie funkcjonalną (filter)
> - operacje na listach składanych.

[kod](ex-4.py)

## Zadanie 5

> Poniżej w języku OCAML napisany jest program, który generuje wszystkie podzbiory
> ```ocaml
>   let rec allsubsets s =
>     match s with
>       [] -> [[]]
>     | (a::t) -> let res = allsubsets t in
>                   map (fun b -> a::b) res @ res;;
>
>   # allsubsets [1;2;3];;
>   - : int list list = [[1; 2; 3]; [1; 2]; [1; 3]; [1]; [2; 3]; [2]; [3]; []]
> ```
> Napisz podobny program w języku Python wykorzystując:
> - składnie funkcjonalną (map, lambda)
> - operacje na listach składanych

[kod](ex-5.py)
