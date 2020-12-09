# Lista 4

- [Zadanie 1.](#zadanie-1)
- [Zadanie 4.](#zadanie-4)
- [Zadanie 5.](#zadanie-5)
    - [Zadanie 5.1.](#zadanie-51)
    - [Zadanie 5.2.](#zadanie-52)
    - [Zadanie 5.3.](#zadanie-53)

---

## Zadanie 1.

> Zbuduj automat ze stosem rozpoznający język dobrze rozstawionych nawiasów dwóch rodzajów generowany przez gramatykę
> $$
> S \to SS \,|\, (S) \,|\, [S] \,|\, \varepsilon
> $$
> która ma jeden symbol nieterminalny $S$ i cztery symbole terminalne $\texttt{(},\texttt{)}, \texttt{[}, \texttt{]}$.

Mamy [PDA](../../wyk/2020-11-05/automat-ze-stosem.md#1-def-pda) $M = (Q, \Sigma, \Gamma, q_0, Z_0, F)$, gdzie
- $Q = \{q\}$
- $q_0 = q$
- $\Sigma = \Gamma$

Definiujemy funkcję przejścia $\delta$:
- $\delta(q, \texttt{(}, Z_0) = (q, \texttt{(}Z_0)$
- $\delta(q, \texttt{[}, Z_0) = (q, \texttt{[}Z_0)$
- $\delta(q, \texttt{(}, \texttt{(}) = (q, \texttt{((})$
- $\delta(q, \texttt{[}, \texttt{(}) = (q, \texttt{[(})$
- $\delta(q, \texttt{(}, \texttt{[}) = (q, \texttt{([})$
- $\delta(q, \texttt{[}, \texttt{[}) = (q, \texttt{[[})$
- $\delta(q, \texttt{]}, \texttt{[}) = (q, \varepsilon)$ (ściągamy ze stosu)
- $\delta(q, \texttt{)}, \texttt{(}) = (q, \varepsilon)$
- $\delta(q, \varepsilon, Z_0) = (q, \varepsilon)$

Skonstruowany automat poprawnie wykonuje zadane polecenie, bo za każdym razem, kiedy napotyka otwierający nawias, zostawia go, ale kiedy ma na stosie aktualnie otwierający i natrafi na zamykający, usuwa go ze stosu.

---

## Zadanie 4.

> Zbuduj PDA i gramatykę bezkontekstową dla języka
> $$
> \{0,1\}^* \setminus \left\{ ww : w \in \{0,1\}^* \right\}.
> $$

Idea: słowa o długości nieparzystej należy do języka. Patrzymy na słowa o długości parzystej — przynajmniej jeden znak w jednej i w drugiej połówce (na tym samym miejscu) musi się różnić.

Niech długość słowa wynosi $2n$, czyli każda z połówek słowa ma $n$ znaków. Wówczas mamy:
$$
z = \underbrace{z_1 \dots z_{i-1}}_{i-1}\, 1\, \underbrace{z_{i+1} \dots z_{n+i-1}}_{n-1}\, 0\, \underbrace{z_{n+i+1} \dots z_{2n}}_{n-i}
$$
czyli $z = w 1 w' v 0 v'$ lub $z = w 0 w' v 1 v'$, gdzie $|w| = |w'|$ oraz $|v| = |v'|$, bo możemy zamienić ten środek długości $n-1$ (który składa się ze słów długości $(i-1)$, $(n-i)$) na dwa słowa długości $(i-1)$ oraz $(n-i)$.

Teraz możemy na tej podstawie stworzyć gramatykę o następujących produkcjach:
- $S \to J | Z | JZ | ZJ$
- $J \to 1 | 0J0 | 0J1 | 1J0 | 1J1$
- $Z \to 0 | 0Z0 | 0Z1 | 1Z0 | 1Z1$

PDA konstruujemy z [twierdzenia](../../wyk/2020-11-05/automat-ze-stosem.md#5-twierdzenie-język-bezkontekstowy-implies-pda). Generalnie taki automat musi akceptować wszystkie słowa długości nieparzystej oraz parzystej postaci $w0w' v1v'$ lub $w1w' v0v'$, gdzie $|w| = |w'|$ oraz $|v| = |v'|$.

---

## Zadanie 5.

> Pokaż, że następujące języki nie są bezkontekstowe

[«Uogólniony lemat o pompowaniu»](#1-lemat-o-pompowaniu-dla-języków-bezkontekstowych)

### Zadanie 5.1.
> $L_1 = \{a^i b^j b^k: i < j < k\}$

Niech $n$ będzie stałą z lematu o pompowaniu dla języków bezkontekstowych. Weźmy $z = a^n b^{n+1} c^{n+2}$. Musimy rozważyć wszystkie takie podziały słowa $z = uvwxy$ takie, że
- $|vx| \ge 1$
- $|vwx| \le n$

Warto zauważyć, że skoro $|vwx| \le n$ to nie będziemy pompować jednocześnie liter $a$ i $c$, bo pomiędzy nimi stoi $(n+1)$ liter $b$.

Pompujemy: $u v^i w x^i y = z'$

Przypadki:
1. pompujemy jednocześnie $a$ i $b$ (w $v$ lub w $x$ mamy dwie różne litery) — wówczas dla dowolnego $i$ mamy przeplatanie liter $a$ i $b$, czyli $z' \notin L_1$
2. pompujemy jednocześnie $b$ i $c$ (w $v$ lub w $x$ mamy dwie różne litery) — tak samo jak wyżej, $z' \notin L_1$
3. pompujemy tylko litery $a$ — dla dowolnego $i > 1$ będziemy mieli przynajmniej $(n+1)$ liter w słowie $z'$, a przecież liter $b$ jest też $(n+1)$, czyli $z' \notin L_1$
4. pompujemy tylko litery $b$ — tak samo jak wyżej, tylko tym razem zrówna się liczba liter $b$ z liczbą liter $c$
5. pompujemy tylko litery $c$ — dla $i = 0$ liczba liter $c$ zmniejszy się o co najmniej jeden — wówczas znowu będzie tyle samo liter $c$ co $b$ $\implies z' \notin L_1$
6. pompujemy tak, żeby w $v$ były litery $a$, a w $x$ litery $b$ (zakładamy, że $v$ i $x$ nie są puste; oth. obowiązuje punkt 1. lub 2.) — mamy zapewnione, że w $x$ mamy co najmniej jedną literę $b$, wówczas dla dowolnego $i > 1$ mamy więcej $b$ niż $c$
7. $v$ zawiera $b$; $x$ zawiera $c$ — analogicznie

---

### Zadanie 5.2.
> $L_2 = \{a^i b^j : i = j^2\}$

Patrzymy na słowo $z = a^{n^2} b^n$ z perspektywy długości. Długość tego słowa wynosi $n^2 + n = n(n+1)$. Rozważając standardowy zestaw podziałów z lematu $z = uvwxy$, gdzie $|vx| \ge 1$ oraz $|vwx| \le n$ po spompowaniu dla $i = 2$ mamy $z' = uvwxy$, czyli też inną długość:
$$
n(n+1) = n^2 + n < |z'| = |z| + |vx| \le\\
\le n^2 + n + n = n(n+2) < (n+1)(n+2)
$$
w środku mamy $\le$ bo $|vx|$ to conajwyżej $n$. Wówczas nowa długość słowa jest zamknięta między dwiema sąsiadującymi będących możliwymi długościami słowa z tego języka — między nimi nie ma takiej liczby. Zatem $z' \notin L_2$.

---

### Zadanie 5.3.
> $L_3 = \{a^i: i \in \mathrm{Prime}\}$

Niech $n$ będzie stałą pompowania. Weźmy słowo $z = a^p$, gdzie $p \ge n$ jest pierwsza. Rozważamy wszystkie możliwe podziały $z = uvwxy$ takie, że $|vx| \ge 1$, $|vwx| \le n$.

Dla każdego z tych podziałów bierzemy $i = p+1$: $z' = uv^{p+1} wx^{p+1} y$.\
Wówczas
$$
|z'| = |z| + p|vx| = p + p|vx| = p(1 + |vx|)
$$
co daje nam liczbę złożoną. Czyli $z' \notin L_3$.

---
