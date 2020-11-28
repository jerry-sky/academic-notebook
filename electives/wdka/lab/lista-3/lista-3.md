# Lista-3

*(Termin oddania: 2020-11-30)*

- [Zadanie 1.](#zadanie-1)
- [Zadanie 2.](#zadanie-2)
- [Zadanie 3.](#zadanie-3)

---

Do rozwiązań dołączone są pliki o rozszerzeniu `.wls` — są to pliki zawierające skrypty napisane w *WolframScript* i realizują praktyczną część danego zadania.

Uruchomienie na Linuxie (z zainstalowanym *Wolfram Mathematica* i *WolframScript*): `./ex-[numer zadania].wls`.

---

## Zadanie 1.

> Generujemy losowy ciąg bitowy $x$ długości $30$. Jaka jest oczekiwana wartość liczby wystąpień ukrytego ciągu $000111$?

Określamy klasę kombinatoryczną:
$$
\mathcal{A} = \operatorname{SEQ}(\{1\}) \times \{0\} \times \operatorname{SEQ}(\{1\})\times \{0\} \times \operatorname{SEQ}(\{1\})\times \{0\} \times \operatorname{SEQ}(\{1\}) \times\\
\times \{1\} \times \operatorname{SEQ}(\{0\}) \times \{1\} \times \operatorname{SEQ}(\{0\}) \times \{1\} \times \operatorname{SEQ}(\{0, 1\})
$$
wraz z OGF:
$$
A(z) = \left( \frac{1}{1-z} \right)^6 \cdot z^{6} \cdot \frac{1}{1-2z}.
$$

Żeby policzyć oczekiwaną wartość liczby wystąpień, wystarczy, że policzymy, ile jest ciągów o takiej charakterystyce oraz ile jest ciągów wszystkich długości $30$.

Czyli mamy $\frac{[z^{30}]A(z)}{2^{30}} = 0.9998375428840517997741699218750$.

[Kod programu](ex-1.wls) znajduje się w pliku `ex-1.wls`.

---

## Zadanie 2.

> Ile jest słów nad alfabetem $\{a, b\}$, które nie zawierają $\overline{p} = abba$?

Korzystamy ze [wzoru z wykładu](../../wyk/2020-10-26/języki.md#42-ciągi-długości-n-z-wzorcem-overlinep) na OGF dla klasy określającej taki zbiór słów bez danego wzorca.

Mamy
$$
S(z) = \frac{C(z)}{z^k + (1 - mz) \cdot C(z)}
$$
gdzie:
- $C(z) = 1 + z^3$ będący wielomianem charakterystycznym dla wzorca $\overline{p}$
- $k = 4$ bo wzorzec $\overline{p}$ ma długość $4$
- $m = 2$ bo liter w alfabecie mamy dwie

Czyli mamy ostatecznie:
$$
S(z) = \frac{1 + z^3}{z^4 + (1 - 2z) \cdot (1+z^3)}
$$

Teraz oczywiście wystarczy policzyć $[z^n]S(z)$.\
Dla przykładu policzmy dla $n = 30$: $[z^{30}]S(z) = 166654357 = 1.66654357 \cdot 10^{8}$.

[Kod programu](ex-2.wls) znajduje się w pliku `ex-2.wls`.

---

## Zadanie 3.

> Ile jest drzew uporządkowanych o $25$ węzłach takich, że każdy wierzchołek ma co najwyżej $4$ potomków?

Sytuacja podobna do [zadania 5. z listy 2. z laboratorium](../../lab/lista-2/lista-2.md#zadanie-5) — przy czym tutaj każdy węzeł może mieć od $0$ do $4$ potomków.

Mamy klasę kombinatoryczną:
$$
\mathcal{T} \cong \mathcal{Z} \times \operatorname{SEQ}_{\le4}(\mathcal{T}).
$$

I znowu budujemy OGF:
$$
T(z) = z \cdot \left( 1 + T(z) + T^2(z) + T^3(z) + T^4(z) \right)
$$
i dochodzimy do tego samego problemu — musimy tutaj użyć [Twierdzenia Lagrange’a o inwersji](../../wyk/2020-11-09/tw-lagrangea-o-inwersji.md). Określamy funkcję:
$$
\varphi(x) = 1 + x + x^2 + x^3 + x^4,
$$
która jest funkcją analityczną (wielomian; jest swoim rozwinięciem Taylora).

Wiemy również, że
$$
[z^n]T(z) = \frac{1}{n}[x^{n-1}]\varphi^n(x).
$$

Zatem, możemy uzyskać nasz wynik:
$$
[z^{25}]T(z) = \frac{1}{25} [x^{24}] (1 + x + x^2 + x^3 + x^4)^{25} =\\
= 601928551824 = 6.01928551824 \cdot 10^{11}
$$

[Kod programu](ex-3.wls) znajduje się w pliku `ex-3.wls`.

---
