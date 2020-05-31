# Lista-6

## Zadanie 1

> Zaimplementuj algorytm propagacji wstecznej przedstawiony na wykładzie 9 dla sieci neuronowej 3-4-1 (3-wejścia, 4-warstwa ukryta, 1-wyjście). Rozwiąż pokazany problem `XOR`. Następnie
> - zamiast funkcji sigmoidalnej $\sigma = \frac{1}{1-e^{-x}}$ wykorzystaj funkcje aktywacji $\mathrm{ReLU}(x) = \max\{0,x\}$
> - wykorzystaj kombinacje funkcji sigmoidalnej $\sigma$ z $\mathrm{ReLU}$ np. warstwa ukryta ma $\sigma$ a warstwa wyjściowa jest $\mathrm{ReLU}$ lub inne kombinacje. Poeksperymentuj!
>
> Które rozwiązanie daje lepszą dokładność? Odpowiedź na to pytanie pisząc program testowy, który to pokazuje (np. po uruchomieniu w terminalu dostajemy wyniki dla różnych kombinacji z opisem). Rozwiąż ten problem również dla innych funkcji logicznych AND i OR. Dlaczego w danych wejściowych z przykładu z wykładu mamy ostatnią kolumnę z samymi jedynkami. Na to pytanie odpowiedź w komentarzu kodu źródłowego programu.

[kod](ex-1.py)

Uruchomienie programu: `./ex-1.py <XOR|OR|AND>`.
