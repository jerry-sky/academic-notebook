# Lista-1

*(Termin oddania 2020-10-31)*

- [Zadanie 1.](#zadanie-1)
- [Zadanie 3.](#zadanie-3)
- [Zadanie 4.](#zadanie-4)
- [Zadanie 5.](#zadanie-5)
- [Zadanie 6.](#zadanie-6)
- [Zadanie 7.](#zadanie-7)

---

Do rozwiązań dołączone są pliki o rozszerzeniu `.wls` — są to pliki zawierające skrypty napisane w *WolframScript* i realizują praktyczną część danego zadania.

Uruchomienie na Linuxie (z zainstalowanym *Wolfram Mathematica* i *WolframScript*): `./ex-[numer zadania].wls`.

---

## Zadanie 1.

> Dla jakich $x$ zachodzi:
> $$
> x > 10^6 \cdot \ln(x)
> $$

Powyższe wyrażenie zachodzi dla
$$
0 < x < 1.0000010000015\\
\lor\\
x > 1.6626508901372496 \cdot 10^7.
$$

Wykresy (zielony — $10^6 \cdot ln(x)$, czerwony — $x$):

![](1.wykres-1.png)\
![](1.wykres-2.png)\
![](1.wykres-3.png)


[Kod programu](ex-1.wls) znajduje się w pliku `ex-1.wls`.

---

## Zadanie 3.

>  Na ile sposobów można wypłacić 200\$ mając do dyspozycji 20 banknotów 20\$, 10 banknotów 10\$, 10 banknotów 5\$ dolarowych oraz 50 banknotów 1\$.\
> *Uwaga: banknoty są **rozróżnialne**.*

Określmy klasę kombinatoryczną pomocną w rozwiązaniu tego zadania:
$$
\mathcal{B} = (\left\{ a_1, \dots, a_{20}, b_1, \dots, b_{10}, c_1, \dots, c_{10}, d_1, \dots, d_{50} \right\}, |\cdot|)\\
\mathcal{A} = \operatorname{PSET}(\mathcal{B})
$$
($\mathcal{B}$ to klasa pomocnicza, bazowa; skupiamy się na $\mathcal{A}$)\
gdzie:
- $a_i$ to banknoty \$20
- $b_i$ to banknoty \$10
- $c_i$ to banknoty \$5
- $d_i$ to banknoty \$1

a funkcja wagi $|\cdot|$ przypisuje wszystkim poszczególnym banknotom wartości ich nominałów.

OGF: $A(z) = \prod_{n\ge0} \left( 1+z^n \right)^{b_n} = \left( 1 + z \right)^{50} \cdot \left( 1 + z^5 \right)^{10} \cdot \left( 1 + z^{10} \right)^{10} \cdot \left( 1 + z^{20} \right)^{20}$

Odpowiedzią na nasze pytanie jest $[z^{200}]A(z) = 1209902431363984921974763 = 1.2099024 \cdot 10^{24}$.

[Kod programu](ex-3.wls) znajduje się w pliku `ex-3.wls`.

---

## Zadanie 4.

> Na ile sposobów Rychu Peja może wypłacić 16 zł, mając do dyspozycji 3 monety 5 zł, 5 monet 2 zł, 10 monet 1 zł oraz 100 monet 10 gr. Zakładamy, że kolejność wydawania monet nie ma znaczenia, a monety są nierozróżnialne.

Idea rozwiązania jest podobna do [zadania 3.](#zadanie-3), przy czym tutaj nie rozróżniamy poszczególnych monet (nie mają numerów seryjnych). Jednakże nadal mamy ograniczenia co do liczby wykorzystywanych monet, więc nie możemy użyć tutaj $\operatorname{MSET}$. Znowu użyjemy $\operatorname{PSET}$ tylko zmodyfikujemy nieco rozważane elementy — np.: 3 monety 5 złotowe rozumiemy jako trzy różne sumy: $5$, $10$ oraz $15$. Załatwia nam to problem zachowania nierozróżnialności oraz ograniczenie liczby monet danego typu.

Pozostaje jeszcze jeden problem z reprezentacją wartości monet — wagi elementów muszą być liczbami naturalnymi. Tutaj rozwiązanie jest proste — nominały zapisujemy w liczbach groszy, a nie złotych.

Określamy klasę kombinatoryczną:
$$
\mathcal{A} = \Big( \left\{ \epsilon, a_1, a_2, a_3 \right\} \times \left\{ \epsilon, b_1, \dots, b_5 \right\} \times\\
\left\{ \epsilon, c_1, \dots, c_{10} \right\} \times \left\{ \epsilon, d_1, \dots, d_{100} \right\}, |\cdot| \Big)
$$
($\mathcal{B}$ to klasa pomocnicza, bazowa; skupiamy się na $\mathcal{A}$)\
gdzie:
- $a_i = 500i$
- $b_i = 200i$
- $c_i = 100i$
- $d_i = 10i$
- $\epsilon = 0$

OGF: $A(z) = \left( 1 + z^{500} + z^{1000} + z^{1500} \right) \cdot \left( 1 + z^{200} + z^{400} + z^{600} + z^{800} + z^{1000} \right) \cdot \left( 1 + z^{100} + \dots + z^{1000} \right) \cdot \left( 1 + z^{10} + \dots + z^{1000} \right)$

Żądana wartość wynosi $[z^{1600}]A(z) = 106$.

[Kod programu](ex-4.wls) znajduje się w pliku `ex-4.wls`.

---

## Zadanie 5.

> Na ile sposobów można przedstawić liczbę $200$ jako sumę $30$ liczb ze zbioru $\{1, 2, 3, 4, 5, 10, 50, 100\}$?\
Zakładamy, że kolejność sumowania ma znaczenie ($10 = 2 + 8 = 8 + 2$ to dwie *różne* interpretacje).

Określamy klasą kombinatoryczną:
$$
\mathcal{B} = (\{1,2,3,4,5,10,50,100\}, |\cdot|)\\
\mathcal{A} = \underbrace{\mathcal{B} \times \dotsb \times \mathcal{B}}_{30}
$$
($\mathcal{B}$ to klasa pomocnicza, bazowa; skupiamy się na $\mathcal{A}$)

OGFs:
- $B(z) = z + z^2 + z^3 + z^4 + z^5 + z^{10} + z^{50} + z^{100}$
- $A(z) = (B(z))^{30}$

Żądana wartość wynosi $[z^{200}]A(z) = 59115949907090587181520 = 5.9115949907 \cdot 10^{22}$.

[Kod programu](ex-5.wls) znajduje się w pliku `ex-5.wls`.

---

## Zadanie 6.

>  Ile jest naszyjników 3-kolorowych o długości 5? Który jest najładniejszy?

Określamy klasę kombinatoryczną:
$$
\mathcal{B} = \Big( \{1,2,3\}, |\cdot| \Big)\\
\mathcal{A} = \operatorname{CYC}(\mathcal{B})
$$
($\mathcal{B}$ to klasa pomocnicza, bazowa; skupiamy się na $\mathcal{A}$)

OGFs:
- $B(z) = 3z$
- $A(z) = \sum_{k=1}^{\infty} \frac{\varphi(k)}{k} \ln\frac{1}{1 - B\left( z^k \right)}$ gdzie $\varphi$ to funkcja Eulera

Żądana wartość wynosi $[z^5]A(z) = 51$.

*(najładniejszy naszyjnik to taki który ma dwie połowy takiego samego koloru)*

[Kod programu](ex-6.wls) znajduje się w pliku `ex-6.wls`.

---

## Zadanie 7.

> Ile jest naszyjników 4-kolorowych o długości 20?

Sytuacja prawie identyczna, jak w [zadaniu 6.](#zadanie-6) — jedynie zmieniamy nieco parametry:
- $B(z) = 4z$ (mamy cztery kolory)
- szukamy wartości $[z^{20}]A(z)$

Żądana wartość wynosi $[z^{20}]A(z) = 54975633976 = 5.4975633976 \cdot 10^{10}$.

[Kod programu](ex-7.wls) znajduje się w pliku `ex-7.wls`.

---
