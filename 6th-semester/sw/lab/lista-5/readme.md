---
lang: 'pl'
title: 'Lista 5.'
subtitle: 'Systemy wbudowane, Laboratorium'
author: 'Jerry Sky'
---

- [Kompilacja i uruchomienie programów](#kompilacja-i-uruchomienie-programów)
- [Zadanie 1.](#zadanie-1)
    - [Programy](#programy)
    - [Błędy względne](#błędy-względne)
- [Zadanie 2.](#zadanie-2)
    - [Program](#program)
    - [Wynik](#wynik)

---

> Elementem koordynującym współpracę wielu niezależnych elementów w systemie,
> a także umożliwiającym realizację jego zadań w perspektywie czasu jest zegar.
> Generuje on tzw. podstawę czasu systemowego — np. zegar 50 MHz określi podstawową
> jednostkę czasu używaną przez procesor na 20ns ($2^{−8}$ sek.)
>
> Dla różnych podzespołów systemu jednak stawia się różne wymagania dotyczące zegara.
> Chciałoby się, by procesor wykonywał obliczenia jak najszybciej (najszybszy zegar),
> ale transmisje muszą być realizowane wolniej, m. in. ze względu na pewność przesyłu.
> Jednym ze sposobów radzenia sobie z tym problemem jest integracja różnych zegarów w jednym systemie,
> co jest praktykowane, lecz niesie za sobą potrzebę ich wzajemnej synchronizacji.
> Drugim podejściem jest zwielokrotnianie (tj. wydłużanie okresu)
> albo dzielenie (taktowanie układu jeszcze szybciej) podstawy czasu.
>
> Zajmijmy się spowalnianiem zegara.
> Służą do tego dzielniki częstotliwości.
> Na dzisiejszych zajęciach zbudujesz (napiszesz) taki dzielnik.
> Jest to bardzo prosty układ: na wejściu przyjmuje oryginalny zegar oraz parametr
> zawierający informację o żądanych parametrach zegara wyjściowego (dzielnik).
> Na wyjściu generuje impuls zegarowy odpowiednio spowolniony względem zegara wejściowego.
> Weźmy pod uwagę powyższy zegar 50 MHz.
> Jeśli potrzebujemy zegar 1 MHz, jaki parametr dzielnika jest potrzebny?
> Oczywiście, na każde 50 taktów zegara głównego wygenerujemy jeden takt zegara spowolnionego.
> Czyli wystarczy zliczyć 50 taktów zegara głównego i odwrócić sygnał
> zegara spowalnianego!
>
> A co, gdy potrzebujemy zegara 40 Hz?
> To bardzo znaczne spowolnienie: każdy takt wyjściowy to 1 250 000 taktów głównych!
> Widać zatem, że dzielnik częstotliwości oprócz parametru „przez ile dzielić”
> musi być również parametryzowany rozmiarem licznika, który będzie wewnętrznie zliczał impulsy.
> (Przypomnij sobie pragmę `generic`!)
>
> Jest jeszcze jeden problem: przypomnij sobie wykład o UART i precyzji zegarów nadajnika i odbiornika.
> Problem wynika z tego, że częstotliwość zegara głównego możemy dzielić
> tylko przez dzielnik będący liczbą całkowitą.
> A zatem z zegara 1 MHz nie wygenerujemy w ten sposób zegara o częstotliwości
> $\frac{1 \,\mathrm{MHz}}{2.5} = 400 \mathrm{kHz}$
> (chociaż to taka okrągła wartość…).

---

## Kompilacja i uruchomienie programów

Kompilacja wszystkich programów:

```bash
make build
```

Uruchomienie danego programu:

```bash
make r=program
```

gdzie `program` to jeden z:
- `clock_divider`,
- lub `clock_divider_tb`.

Uruchomienie programu oraz wygenerowanie pliku do odczytu przy pomocy programu GTKWave:

```bash
make wave-quiet r=program
```

Uruchomienie programu, wygenerowanie pliku do odczytu, oraz uruchomienie programu GTKWave:

```bash
make wave r=program
```

---

## Zadanie 1.

> Napisz kod dzielnika częstotliwości.
>
> - Zbuduj test dla dzielnika; główny zegar w teście ma częstotliwość 125 MHz.
> - Zainicjuj trzy instancje dzielnika o najmniejszych możliwych rozmiarach
> (w rozumieniu liczby bitów), generujące przebiegi 100 Hz, 1.1 kHz oraz 50 MHz.
>
> Korzystając z podglądu przebiegów na GTKWave,
> oblicz w procentach niedokładności generowanych przebiegów.

### Programy

Kod programu symulującego dzielnik częstotliwości znajduje się w [pliku `clock_divider.vhd`](clock_divider.vhd).

W [pliku `clock_divider_tb.vhd`](clock_divider_tb.vhd) znajduje się program testowy implementujący przypadki podane w zadaniu.

### Błędy względne

| Oczekiwana cz. | zaobserwowany okres | faktyczna cz.            | błąd względny               |
| -------------- | ------------------- | ------------------------ | --------------------------- |
| 100Hz          | 10ms                | 100Hz                    | $0$                         |
| 1100Hz         | 909096ns            | 1099.99… Hz              | $\approx 5.6 \cdot 10^{-6}$ |
| 50MHz          | 24ns                | $4.1(6) \cdot 10^{7}$ Hz | $0.1(6)$

---

## Zadanie 2.

> Napisz kod dzielnika częstotliwości, który będzie miał $N$ wyjść
> ($N$ jest określane pragmą `generic`), z których $i$-te wyjście
> (licząc od $0$) będzie zegarem o okresie $2^{i+1}$ razy dłuższym niż zegar podstawowy.

### Program

Kod programu znajduje się w [pliku `clock_exp_divider.vhd`](clock_exp_divider.vhd).

Jego wyniki są widoczne w programie GTKWave razem z wynikami z zadania 1.

### Wynik

Przykład dla `N = 5`:

![GTKWave output](clock-exp-gtkwave.png)

Oczywiście, jeszcze prostszym układem symulującym takie zachowanie byłby zwykły
licznik binarny, który zwiększa swoją wartość o jeden za każdym sygnałem zegara
oryginalnego.

---
