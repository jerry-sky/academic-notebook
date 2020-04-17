# Lista-2

## Treść zadania

Rozważmy model sieci $S = (G,H)$.

Przez $N=[~n_{i,j}~]$ będziemy oznaczać macierz natężeń strumienia pakietów, gdzie element $n_{i,j}$ jest liczbą pakietów przesyłanych (wprowadzanych do sieci) w ciągu sekundy od źródła $v_i$ do ujścia $v_j$.

- Zaproponuj topologię grafu $G = (V,E)$ ale tak aby żaden wierzchołek nie był izolowany oraz aby:
  $$
  |V| = 20 \land |E| < 30.
  $$

  Zaproponuj $N$ oraz następujące funkcje krawędzi ze zbioru $H$:
  - funkcję przepustowości $c$ *(rozumianą jako maksymalną liczbę bitów, którą można wprowadzić do kanału komunikacyjnego w ciągu sekundy)*
  - funkcję przepływu $a$ *(rozumianą jako faktyczną liczbę pakietów, które wprowadza się do kanału komunikacyjnego w ciągu sekundy)*. Pamiętaj aby funkcja przepływu realizowała macierz $N$ oraz aby dla każdego kanału $e$ zachodziło: $c(e) > a(e)$.

- Niech miarą niezawodności sieci jest prawdopodobieństwo tego, że w dowolnym przedziale czasowym, nierozspójniona sieć zachowuje $T < T_{\max}$, gdzie:
  $$
  T = \frac{1}{N_\Sigma} \cdot \sum_{e\in E}\left( \frac{a(e)}{\frac{c(e)}{m} - a(e)} \right)
  $$
  jest średnim opóźnieniem pakietu w sieci, $N_\Sigma$ jest sumą wszystkich elementów macierzy natężeń, a $m$ jest średnią wielkością pakietu w bitach.

  Napisz program szacujący niezawodność takiej sieci przyjmując, że prawdopodobieństwo nieuszkodzenia każdej krawędzi w dowolnym interwale jest równe $p$.\
  Uwaga: $N$, $p$, $T_{\max}$ oraz topologia wyjściowa sieci ($G$) są parametrami.

- Przy ustalonej strukturze topologicznej sieci i dobranych przepustowościach stopniowo zwiększaj wartości w macierzy natężeń. Jak będzie zmieniać się niezawodność zdefiniowana tak jak punkcie poprzednim ($\mathrm{P}(T < T_{\max})$).

- Przy ustalonej macierzy natężeń i strukturze topologicznej stopniowo zwiększaj przepustowości. Jak będzie zmieniać się niezawodność zdefiniowana tak jak punkcie poprzednim ($\mathrm{P}(T < T_{\max})$).

- Przy ustalonej macierzy natężeń i pewnej początkowej strukturze topologicznej, stopniowo zmieniaj topologię poprzez dodawanie nowych krawędzi o przepustowościach będących wartościami średnimi dla sieci początkowej. Jak będzie zmieniać się niezawodność zdefiniowana tak jak punkcie poprzednim ($\mathrm{P}(T < T_{\max})$).

Napisz sprawozdanie zawierające opis zrealizowanych programów, komentarz do przeprowadzonych badań oraz wnioski.

## Sprawdzenie jednostki wzoru

$$
\frac{1}{\frac{1}{s}} \cdot \left( \frac{\frac{1}{s}}{\frac{\frac{b}{s}}{b} - \frac{1}{s}} \right) = s \cdot \left(\frac{\frac{1}{s}}{\frac{1}{s}}\right) = s
$$

## Sprawozdanie

### Pierwsze uruchomienia programu

Z parametrami $p = 0.99$, $T_{\max} = 5 \cdot 10^{-6}$ oraz $N$ generowanym losowo z przedziału $[1;100]$ wartości zwracane wahały się pomiędzy $0.98$ a $1$.

### Zwiększenie natężeń

Po zwiększeniu zakresu z którego była losowana liczba pakietów do macierzy natężeń $N$ wymagane było zwiększenie oczywiście $T_{max}$ żeby uzyskać dobrą niezawodność. Opóźnienie było bardziej odczuwalne.

### Zwiększenie przepustowości

Po zwiększeniu maksymalnej przepustowości problemy z niezawodnością systemu oczywiście znacznie zmalały. Przekroczeń czasu oczekiwania było znacznie mniej niż w poprzednim przypadku.

### Dodawanie kolejnych krawędzi

Po dodaniu większej ilości krawędzi oczywistym stało się, że nawet przy znacznie zmniejszonym $p$ niezawodność nadal była dość dobra, bo było większe prawdopodobieństwo, że znajdzie się inna droga.

### Wnioski

Najlepsza sieć to taka, która ma dużo nadmiarowych połączeń, bo jeśli jedno z połączeń ulegnie zniszczeniu zawsze znajdzie się drugie.
