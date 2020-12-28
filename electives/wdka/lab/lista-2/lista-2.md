# Lista-2

*(Termin oddania 2020-11-11)*

- [Zadanie 1.](#zadanie-1)
    - [Zadanie 1.1.](#zadanie-11)
    - [Zadanie 1.2.](#zadanie-12)
    - [Zadanie 1.3.](#zadanie-13)
    - [Zadanie 1.4.](#zadanie-14)
- [Zadanie 2.](#zadanie-2)
- [Zadanie 5.](#zadanie-5)
- [Zadanie 6.](#zadanie-6)
- [Zadanie 7.](#zadanie-7)

---

Do rozwiązań dołączone są pliki o rozszerzeniu `.wls` — są to pliki zawierające skrypty napisane w *WolframScript* i realizują praktyczną część danego zadania.

Uruchomienie na Linuxie (z zainstalowanym *Wolfram Mathematica* i *WolframScript*): `./ex-[numer zadania].wls`.

---

## Zadanie 1.

> Niech $N$ będzie drugim imieniem Rycha Pei a $L$ będzie liczbą lat jakie ukończył Rychu Peja.

### Zadanie 1.1.

> Ile jest kompozycji liczby $L$?

Określamy klasę kombinatoryczną dla kompozycji liczb:
$$
\mathcal{C} \cong \operatorname{SEQ}(\mathcal{N}_{\ge1})
$$
oraz OGF dla tej klasy:
$$
C(z) = \frac{1}{1 - \frac{z}{1-z}} = \frac{1-z}{1 - 2z}.
$$

Zatem naszym wynikiem będzie:
$$
[z^L]C(z) = [z^L] \frac{1}{1-2z} - [z^L] \frac{z}{1-2z} = 2^L - 2^{L-1} = 2^{L-1} \overset{L = 44}{=} 2^{43} =\\
= 8796093022208 = 8.796093022208 \cdot 10^{12}
$$

[Kod programu](ex-1.1.wls) znajduje się w pliku `ex-1.1.wls`.

---

### Zadanie 1.2.

> Ile jest partycji liczby $L$ na liczby ze zbioru $\left\{ 1,2,20,21 \right\}$?

Określamy klasę kombinatoryczną dla partycji liczby na podliczby ze zbioru $\{1,2,20,21\}$:
$$
\mathcal{P}^{\left\{ 1,2,20,21 \right\}} \cong \operatorname{MSET}(\mathcal{N}_{\in \{1,2,20,21\}})
$$
oraz OGF dla tej klasy:
$$
P_a(z) = P^{\{1,2,20,21\}}(z) = \frac{1}{1-z} \cdot \frac{1}{1-z^2} \cdot \frac{1}{1-z^{20}} \cdot \frac{1}{1-z^{21}}.
$$

Zatem naszym wynikiem będzie:
$$
[z^L]P_a(z) = 55.
$$

[Kod programu](ex-1.2.wls) znajduje się w pliku `ex-1.2.wls`.

---

### Zadanie 1.3.

> Ile jest słów będących permutacją liter ze słowa $N$?

Słowo: *Waldemar* — powtarzają się tylko jedna litera (*a*) tylko jeden raz.

Mamy $n = 8$. Gdyby wszystkie litery byłyby różne mamy wszystkich takich permutacji $8!$. Jednakże, mamy jedno powtórzenie, więc dzielimy przez $2!$ (bo literek *a* jest dwa — wyrzucamy rozróżnienie między nimi).

Zatem nasz wynik wynosi $\frac{8!}{2!} = 20160$.

[Kod programu](ex-1.3.wls) znajduje się w pliku `ex-1.3.wls`.

---

### Zadanie 1.4.

>  Ile jest słów będących permutacją liter ze słowa $N$, które nie mają więcej niż $3$ spółgłosek obok siebie.

Słowo: *Waldemar* — powtarzają się tylko jedna litera (*a*) tylko jeden raz.

Rozważamy przegródki, gdzie ścianami wewnętrznymi są samogłoski (jest ich $3$) a w przegródkach mamy spółgłoski. Liczba spółgłosek wynosi pięć, więc suma liczebności z poszczególnych przegródek też musi tyle wynosić. Określamy $x_i$ jako liczbę spółgłosek w $i$-tej przegródce (mamy ich $4$). Przy czym w żadnej przegródce nie może być więcej niż trzy spółgłoski.\
Czyli:
$$
\sum_{i=1}^4 x_i = 5, \quad \forall i \enspace x_i \in \{0,\dots,3\}.
$$

Odpowiada temu pewna klasa kombinatoryczna $\mathcal{A}$ o OGF:
$$
A(z) = (1 + z + z^2 + z^3)^4.
$$

Pośredni wynik wynosi $[z^5]A(z) = 28$.

Pozostało jeszcze pomnożyć ten współczynnik przez odpowiednią liczbę, która nada rozróżnialność między literami $28 \cdot \frac{5! \cdot 3!}{2!}$ jako, że mamy $5$ spółgłosek oraz $3$ samogłoski, przy czym mamy dwie kopie tej samej spółgłoski dlatego dzielimy przez $2!$.

Wynik ostateczny: $14400$.

[Kod programu](ex-1.4.wls) znajduje się w pliku `ex-1.4.wls`.

---

## Zadanie 2.

> Losujemy niezależnie ciąg 100 bitów. Niech $R$ będzie najdłuższym ciągiem samych jedynek obok siebie (np. Dla $00101010101110$ mamy $R = 3$). Oblicz p-stwo, że $R = 10$.

Myślimy o zerach jako o ścianach przegródek, a w tych przegródkach siedzą jedynki. Przy czym, rozważamy różne liczby zer i musimy oczywiście wykluczyć te sytuacje, w których mamy za mało zer. Co ważniejsze, musimy liczyć tylko dla tych sytuacji, w których mamy co najmniej $10$ jedynek w co najmniej jednej przegródce. Używamy następującej sumy do opisania bloków jedynek:
$$
\left(\sum_{k=0}^{10} z^k \right)^{n+1}
$$
bo mamy $n+1$ ścianek dla $n$ przegródek. Jednakże musimy odjąć takie bloki, dla których liczba jedynek może być mniejsza niż $10$:
$$
\left( \sum_{k=0}^{9} z^k \right)^{n+1}
$$
i chcemy z tych sum wyciągnąć współczynniki dla potęg $[z^{100-n}]$, jako że chcemy uzyskać liczbę jedynek ($n$ to liczba zer, więc $100-n$ to liczba jedynek).

Zatem:
$$
\sum_{n=0}^{90} \left( [z^{100-n}]\left(\sum_{k=0}^{10} z^k \right)^{n+1} - [z^{100-n}]\left( \sum_{k=0}^{9} z^k \right)^{n+1} \right)
$$
jest naszym rozwiązaniem (sumujemy wszystkie możliwości dla zer).

Wynik ostateczny: $0.022107962880719877 \approx 2\%$.

[Kod programu](ex-2.wls) znajduje się w pliku `ex-2.wls`.

---

## Zadanie 5.

> Ile mamy uporządkowanych drzew o $20$ węzłach, w których każdy węzeł ma $0$, $1$ lub $2$ potomków?

Sytuacja podobna do [zadania 2. z listy 2. z ćwiczeń](../../cw/lista-2/lista-2.md#zadanie-2) — przy czym tutaj mamy małe rozszerzenie — każdy potomek może mieć teraz również tylko jednego potomka.

Zmienia to nieco postać klasy kombinatorycznej:
$$
\mathcal{T} \cong \mathcal{Z} \times (\mathcal{E} + \mathcal{T} + \mathcal{T} \times \mathcal{T}).
$$

I znowu budujemy OGF:
$$
T(z) = z \cdot \left( 1 + T(z) + T^2(z) \right)
$$
i dochodzimy do tego samego problemu — musimy tutaj użyć Twierdzenia Lagrange’a o inwersji. Określamy funkcję:
$$
\varphi(x) = 1 + x + x^2,
$$
która jest funkcją analityczną (wielomian; jest swoim rozwinięciem Taylora).

Wiemy również, że
$$
[z^n]T(z) = \frac{1}{n}[x^{n-1}]\varphi^n(x).
$$

Zatem, możemy uzyskać nasz wynik:
$$
[z^{20}]T(z) = \frac{1}{20} [x^{19}] (1 + x + x^2)^n = 18199284 = 1.8199284 \cdot 10^{7}
$$

[Kod programu](ex-5.wls) znajduje się w pliku `ex-5.wls`.

---

## Zadanie 6.

> Ile jest triangulacji $20$-kąta?

Wykorzystujemy wzór
$$
T(z) = \sum_{n=0}^{\infty} \frac{1}{n+1} \binom{2n}{n} \cdot z^n.
$$

Ostateczny wynik: $[z^{18}] T(z) = 477638700 = 4.77638700 \cdot 10^{8}$.

[Kod programu](ex-6.wls) znajduje się w pliku `ex-6.wls`.

---

## Zadanie 7.

> Święty Mikołaj ma w worku dziesięć różnych przedmiotów o wadze $1$ kg, trzy różne przedmioty o wadze $2$ kg oraz jeden przedmiot o masie $7$ kg.
> 1. Na ile sposobów może przygotować prezent o masie $12$ kg?
> 2. A na ile sposobów prezent o masie co najmniej $12$ kg?

1. Będzie to zbiór potęgowy tych wszystkich przedmiotów. Czyli OGF będzie postaci:
    $$
    A(z) = (1 + z)^{10} \cdot (1 + z^2)^{3} \cdot (1 + z^7)
    $$

    Ostateczny wynik: $[z^{12}]A(z) = 990$

2. Tutaj robimy sumę od $12$ do maksymalnej liczby kilogramów, jaką jest Święty Mikołaj zbudować z dostępnych przedmiotów.
    $$
    \sum_{n=0}^{23} [z^{n}]A(z) = 8192.
    $$

[Kod programu](ex-7.wls) znajduje się w pliku `ex-7.wls`.

---
