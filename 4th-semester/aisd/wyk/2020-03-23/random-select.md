# `RandomSelect`
*(2020-03-23)*

## Description

`RandomSelect` wykorzystuje podejście zaprezentowane w [algorytmie `QuickSort`](../2020-03-11/quick-sort.md). Jest to algorytm, który w najgorszym przypadku będzie działał w złożoności $O(n^2)$, ale jeśli założymy, ze wejściowa tablica $A$ jest losową permutacją wielkości $n$ to można pokazać, że $E$ (wartość oczekiwana) zmiennej losowej $X$ liczby porównań wynosi $O(n)$ *(robi się to w podobny sposób jak to było w przypadku `QuickSort`a)*.\
Algorytm ten jest tylko drobną modyfikacją [algorytmu do wyznaczania mediany (2.4 Medians)][algorithms].

Więcej informacji [tutaj 9.2](https://web.ist.utl.pt/~fabio.ferreira/material/asa/clrs.pdf).

[algorithms]: http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf
