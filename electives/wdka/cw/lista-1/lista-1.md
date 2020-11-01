# Lista-1

*(Termin oddania: 2020-10-31)*

- [Zadanie 1.](#zadanie-1)
- [Zadanie 2.](#zadanie-2)
- [Zadanie 4.](#zadanie-4)
- [Zadanie 5.](#zadanie-5)
- [Zadanie 6.](#zadanie-6)

---

*Przyjmujemy, że OFG klasy $\mathcal{A}$ to $A(z)$.*

---

## Zadanie 1.

> Ciąg $(a_1, a_2, \dots)$ odpowiada funkcji generującej $A(z)$. Jakim ciągom odpowiadają funkcje:
> 1. $A'(z) + A(z)$
> 2. $2A(z)$
> 3. $A^2(z)$

1. $A'(z) + A(z) = \left(\sum_{n\ge1} a_n z^n\right)' + \sum_{n\ge1} a_n z^n = \sum_{n\ge0} (n+1) a_{n+1} z^{n} + \sum_{n\ge1} a_n z^n = a_1 + \sum_{n\ge1} ((n+1) a_{n+1} + a_n)z^n \overset{\text{zakładamy, że }a_0 = 0}{=} \sum_{n\ge0}((n+1)a_{n+1} + a_n)z^n$\
czyli mamy ciąg $(a_1 + 2a_2, a_2 + 3a_3, a_3 + 4a_4, \dots)$

2. $2A(z) = 2\cdot\left( \sum_{n\ge1} a_n z^n \right) = \sum_{n\ge1} (2\cdot a_n) \cdot z^n$\
czyli mamy ciąg $(2a_1, 2a_2, 2a_3, 2a_4, \dots)$

1. $\left( A(z) \right)^2 = \left( \sum_{n\ge1} a_n z^n \right)^2 = \sum_{n\ge1} \left( \sum_{k=0}^n a_k \cdot a_{n-k} \right) z^n$\
czyli mamy ciąg $a_n' = \sum_{k=0}^n a_k \cdot a_{n-k}$

---

## Zadanie 2.

> Rozważamy dwie klasy kombinatoryczne:
> - $\mathcal{A} = (A = \left\{ \star, 1, 2, \epsilon \right\}, |\cdot|_A = \left\{ \star \to 5, 1 \to 1, 2 \to 2, \epsilon \to 0 \right\})$
> - $\mathcal{B} = (B = \left\{ a \right\}, |\cdot|_B = \left\{ a \to 1 \right\})$
>
> Opisz poniższe klasy (jeśli istnieją) i podaj ich funkcje generujące:

OGFs:
- $A(z) = 1 + z + z^2 + z^5$
- $B(z) = z$

1. $\mathcal{A} + \mathcal{B} = (A \cup B, |\cdot|_{A\cup B})$

    określamy nową funkcję wagi:
    $$
    |\cdot|_{A\cup B} =
    \begin{cases}
        |x|_A & x \in A\\
        |x|_B & x \in B\\
    \end{cases}
    $$
    gdzie $A$ to zbiór elementów w klasie $\mathcal{A}$, $B$ to zbiór elementów w klasie $\mathcal{B}$, $|\cdot|_A$ to funkcja wagi w klasie $\mathcal{A}$ a $|\cdot|_B$ to funkcja wagi w klasie $\mathcal{B}$

    OGF: $(\mathcal{A} + \mathcal{B})(z) = 1 + 2z + z^2 + z^5$

2. $\mathcal{A} \times \mathcal{B} = (A \times B, |\cdot|)$

    określamy nową funkcją wagi:\
    $\forall a\in A, b\in B \enspace |(a,b)| = |a|_A + |b|_B$

    OGF: $(\mathcal{A} \times \mathcal{B})(z) = A(z) \cdot B(z) = z + z^2 + z^3 + z^6$\
    (to się zgadza, bo klasę $\mathcal{A}$ mnożymy przez klasę $\mathcal{B} \cong \mathcal{Z}$, czyli „kolorujemy” każdy element z $A$ elementem o wadze $1$)

3. $\operatorname{SEQ}(\mathcal{A})$ nie działa, bo ma element wagi zero

4. $\operatorname{SEQ}(\mathcal{B}) = (\left\{ \varepsilon, a, (a,a), (a,a,a), \dots \right\}, |(\beta_1, \dots, \beta_n)| = n)$

    OGF: $\operatorname{SEQ}(\mathcal{B})(z) = \frac{1}{1 - B(z)} = \frac{1}{1 - z}$

    (liczby naturalne)

5. $\operatorname{SEQ}(\mathcal{A} + \mathcal{B})$ nie działa, bo ma element wagi zero

6. $\operatorname{SEQ}(\mathcal{A}) + \operatorname{SEQ}(\mathcal{B})$ tak samo jak dla $\operatorname{SEQ}(\mathcal{A})$; ewentualnie możemy po prostu rozważać jak dla podpunktu 4. i zignorować $\operatorname{SEQ}(\mathcal{A})$.

7. $\operatorname{MSET}(\mathcal{B}) = (\left\{ \varepsilon, \{a\}, \{a,a\}, \{a,a,a\}, \dots \right\}, |\{\underbrace{a,\dots,a}_{n}\}| = n)$

    Ewentualnie, zamiast pisać $n$ razy element $a$, można zapisywać po prostu liczbę, która mówi ile mamy powtórzeń elementu $a$.

    OGF: $\operatorname{MSET}(\mathcal{B})(z) = \prod_{b \in B} \frac{1}{1 - z^{|b|_B}} = \frac{1}{1 - z}$

8. $\operatorname{PSET}(\mathcal{A}) + \operatorname{PSET}(\mathcal{B}) = (\left\{ \varepsilon, \{\star\}, \{1\}, \{2\}, \{\epsilon\}, \{a\}, \{\star, 1\}, \dots \right\}, |X| = \sum_{x \in X}|x|_{A \cup B})$

    **Tutaj nie ma tutaj sytuacji, w której jeden zbiorek ma elementy i ze zbioru $A$ i ze zbioru $B$ jednocześnie.**  (np.: nie ma tutaj zbioru $\{a, \star\}$) Sumujemy dwa $\operatorname{PSET}$-y osobno.

    OGF: $(\operatorname{PSET}(\mathcal{A}) + \operatorname{PSET}(\mathcal{B}))(z) = \prod_{a \in A} (1 + z^{|a|}) + \prod_{b \in B} (1 + z^{|b|}) = (1 + z^5)(1 + z)(1 + z^2)(1 + z^0) + (1 + z) = (1+z)(1 + 2\cdot(1 + z^5)(1 + z^2)) = 2z^8 + 2z^7 + 2z^6 +2z^5 + 2z^3 + 2z^2 + 3z + 3$

9. $\operatorname{CYC}(\mathcal{A})$ nie działa, bo ma element o wagi zero

---

## Zadanie 4.

> Policzyć $[z^{30}] \frac{1}{(1-z)^7}$ (bez użycia komputera).

Funkcję $\frac{1}{(1-z)^7}$ możemy zapisać inaczej:
$$
A(x) = \frac{1}{(1-z)^7} = \sum_{n\ge0} \binom{6 + n}{6} z^n
$$
korzystając ze wzoru 6. z [zadania 5.](#zadanie-5).

Wówczas naszym wynikiem będzie $\binom{36}{6}$.

---

## Zadanie 5.

> Przepisać sobie wszystkie 6. opisanych na wykładzie 1 równań (tożsamości kombinatorycznych). Zapamiętać i zrozumieć nierówności 1-4.

1. $(x+y)^n = \sum_{k = 0}^n \binom{n}{k} x^k y^{n-k}$\
    Mnożymy ze sobą $n$ razy sumę $x+y$ i chcemy uzyskać sumę takiego ciągu, w którym element to jest pewien współczynnik oraz wyrażenie postaci $x^k y^{n-k}$. Należy zauważyć, że taka konfiguracja elementów w tym mnożeniu pojawia się odpowiednią liczbę razy — spośród $n$ wystąpień wybieramy ile ($k$) razy pojawił się symbol $x^k y^{n-k}$ z dokładnie taką potęgą $k$.

2. $\sum_{i=0}^\infty q_i = \frac{1}{1-q} \qquad (|q| < 1)$\
    Suma nieskończona ciągu geometrycznego. Wzór jest szczególnym przypadkiem — sumujemy po wszystkich liczbach naturalnych, przez co dla $|q| < 1$ zachodzi: $\lim_{n\to \infty} \frac{1 - q^n}{1 - q} = \frac{1}{1 - q}$ (ułamek podniesiony do $n \to \infty$ dąży do zera).

3. $\left( \sum_{n=0}^{\infty} a_n x^n \right)\cdot \left( \sum_{n=0}^{\infty} b_n x^n \right) = \sum_{n=0}^\infty \left( \sum_{k=0}^n a_k \cdot b_{n-k} x^n \right)$\
    Przeplatające się ze sobą iloczyny szeregów.

4. $\binom{n+m}{k} = \sum_{j = 0}^{k} \binom{n}{j} \binom{m}{k-j}$\
    Lewa strona: Mamy zbiór $(n+m)$–elementowy i wybieramy spośród nich $k$-elementowy zespół.\
    Prawa strona: Dzielimy ten zespół na dwie części — jeden zbiór $n$-elementowy, drugi $m$-elementowy i wybieramy dwa podzbiory, które razem dadzą $k$-elementowy zbiór. (Musimy rozważyć wszystkie przypadki po ile elementów jest we wspomnianych częściach, dlatego używamy tutaj sumy.)

---
5. $\frac{y^k}{(1-y)^{k+1}} = \sum_{n\ge0} \binom{n}{k} y^n$
6. $\frac{1}{(1-y)^{k+1}} = \sum_{a\ge0} \binom{k+a}{k}y^a$

---

## Zadanie 6.

> Niech $\mathcal{N}$ oznacza klasę kombinatoryczną liczb naturalnych z funkcją rozmiaru równą wartości liczby. Niech $\mathcal{N}_{r,k}$ oznacza klasę liczb naturalnych, które dają resztę $r$ z dzielenie przez $k$. Uzasadnij, że
> $$
> \mathcal{N} \cong \mathcal{N}_{0,k} + \dotsb + \mathcal{N}_{k-1, k}.
> $$

Idea: dzielimy klasę liczb naturalnych na podklasy, w których mamy liczby wielokrotności $k$ z przesunięciem $r$, czyli właśnie wszystkie reszty z dzielenia przez $k$.

Formalna definicja jednej podklasy:
$$
\mathcal{N}_{r,k} = \Big(N_{r,k} = \{x \in \mathbb{N} : x \operatorname{mod} k = r\}, |x| = x \Big)
$$

Zsumujmy wszystkie zbiory podklas w rozumieniu wszystkich reszt z dzielenia przez $k$:
$$
\bigcup_{r = 0}^{k - 1} N_{r,k} = \bigcup_{r = 0}^{k - 1} \left\{ x \in \mathbb{N}: x \operatorname{mod} k = r \right\} =\\
\left\{ x \in \mathbb{N}: x \operatorname{mod} k = r \land r \in \{0, \dots, k-1\} \right\} = (*)
$$
a przez to, że rozważamy $r$ jako wszystkie możliwe reszty z dzielenia przez $k$ wówczas
$$
(*) = \mathbb{N}
$$

Zatem
$$
\mathcal{N} \cong \mathcal{N}_{0,k} + \dotsb + \mathcal{N}_{k-1, k}.
$$

---
