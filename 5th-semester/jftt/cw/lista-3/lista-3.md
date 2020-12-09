# Lista 3

- [Zadanie 1.](#zadanie-1)
    - [Zadanie 1.1.](#zadanie-11)
    - [Zadanie 1.2.](#zadanie-12)
- [Zadanie 2.](#zadanie-2)
- [Zadanie 3.](#zadanie-3)
- [Zadanie 4.](#zadanie-4)
    - [Postać normalna Chomsky’ego](#postać-normalna-chomskyego)
    - [Postać normalna Greibach](#postać-normalna-greibach)
- [Zadanie 5.](#zadanie-5)
- [Zadanie 6.](#zadanie-6)
    - [Zadanie 6.1.](#zadanie-61)
    - [Zadanie 6.2.](#zadanie-62)

---

## Zadanie 1.

> Podać gramatyki bezkontekstowe generujące następujące języki

### Zadanie 1.1.

> zbiór wszystkich słów nad alfabetem $\{0,1\}$, w których liczba zer jest nie mniejsza niż liczba jedynek i nie większa niż trzykrotna liczba jedynek.

Mamy język $L(G) = \left\{ w: w \in \{0,1\}^* \land |w|_1 \le |w|_0 \le 3 \cdot |w|_1 \right\}$

Rozważmy przypadek brzegowy $w = \epsilon \in L$, bo $0 \le 0 \le 0$. Czyli dla symbolu początkowego istnieje przejście $S \to \epsilon$. Zastanówmy się teraz, jak wygląda niepuste słowo $w$ z $L$:
$$
w = \dots 0 \dots 0 \dots 1 \dots 0 \dots
$$

Zasadniczo, w tym słowie każdej jedynce da się przyporządkować od $1$ do $3$ różnych zer (z dowolnego miejsca w słowie) tak, że każde zero jest przyporządkowane do dokładnie jednej jedynki. W miejscu $\dots$ znajduje się ciąg bitów o tej samej własności.

Możemy wypisać wszystkie takie ciągi *atomowe*, spełniające ten stosunek liczby jedynek do liczby zer:
- $10$
- $01$
- $001$
- $010$
- $100$
- $0001$
- $0010$
- $0100$
- $1000$

gdzie pomiędzy znakami powyższych ciągów możemy znowu znaleźć kolejne instancje takich ciągów.\
Zatem gramatyka $G$ jest postaci $(\{S\}, \{0,1\}, P, S)$ gdzie $P$:
$$
\begin{aligned}
    S &\to \epsilon\\
    S &\to S0S1S | S1S0S\\
    S &\to S0S0S1S | S0S1S0S | S1S0S0S\\
    S &\to S0S0S0S1S | S0S0S1S0S | S0S1S0S0S | S1S0S0S0S\\
\end{aligned}
$$

### Zadanie 1.2.

> zbiór wszystkich słów nad alfabetem $\{(,)\}$, gdzie nawiasy są dobrze rozstawione, tzn. każdy lewy nawias ma odpowiadający mu prawy nawias i pary odpowiadających nawiasów są odpowiednio zagnieżdżone.

Mamy język $L(G) = \left\{ w: w\in \{(,)\} \land \text{nawiasy w słowie są dobrze rozstawione} \right\}$.

Znowu możemy mieć $\epsilon$, żeby zakończyć dane słowo.
Jeśli mamy słowo $w \in L$ to możemy mieć też $(w) \in L$ i oczywiście możemy mieć złączenie $w,v \in L$: $wv \in L$.

Zatem mamy gramatykę $G = (\{S\}, \{(,)\}, P, S)$ gdzie $P$:
$$
S \to \epsilon | (S) | SS.
$$

---

## Zadanie 2.

> Niech $G$ będzie gramatyką
> $$
> S \to aS | aSbS | \epsilon
> $$
>
> Udowodnić, że
> $$
> L(G) = \{x: \text{każdy przedrostek ma co najmniej tyle symboli } a \text{, co symboli } b\}
> $$

Zaczynamy od $S$. Mamy trzy możliwości:
1. $S \to aS$
2. $S \to aSbS$
3. $S \to \epsilon$

W pierwszym przypadku nasz „licznik” literek $a$ zwiększamy o jeden, więc nawet jeśli przed wykonaniem przejścia „licznik” literek $b$ był o jeden większy niż „licznik” literek $a$ teraz mamy znowu równość między nimi.

W drugim przypadku mamy wszystko stałe — do obu „liczników” dodajemy jeden.

W trzecim przypadku „liczników” nie zmieniamy.

Za każdym razem, kiedy budujemy dane słowo (a co za tym idzie jego przedrostek) „licznik” literek $a$ nigdy nie spadnie poniżej „licznika” literek $b$.

---

## Zadanie 3.

> Znaleźć gramatykę bezkontekstową bez symboli bezużytecznych równoważną z gramatyką $G = \left( \{S, A, B, C, D\}, \{a,b,c\}, P, S \right)$, gdzie $P$ jest postaci
> $$
> \begin{aligned}
>     S &\to AB | CA\\
>     A &\to a\\
>     B &\to BC | AB\\
>     C &\to aB | b\\
>     D &\to DB | c
> \end{aligned}
> $$

Stosujemy algorytm usuwania symboli bezużytecznych: najpierw szukamy wszystkich nieterminali, które wytwarzają ciąg składających się wyłącznie z terminali (pośrednio lub bezpośrednio):
$$
N' = \{A,C,D\}^* \Rightarrow \{A,C,D,S\}^* \Rightarrow \{S,A,C,D\}
$$

Czyli usuwamy wszystkie produkcje z $B$, mamy nowy zestaw produkcji $P'$:
$$
\begin{aligned}
    S &\to CA\\
    A &\to a\\
    C &\to b\\
    D &\to c
\end{aligned}
$$

Następnie szukamy wszystkich nieterminali, które możemy otrzymać z $S$ stosując produkcje z $P'$:
$$
N'' = \{S\}* \Rightarrow \{S,A,C\}^* \Rightarrow \{S,A,C\}
$$

Czyli usuwamy zbędną produkcję $D$, która jest nieosiągalna.

Mamy nową gramatykę $G'' = \left( \{S,A,C\}, \{a,b\}, P'', S \right)$ gdzie $P''$:
$$
\begin{aligned}
    S &\to CA\\
    A &\to a\\
    C &\to b
\end{aligned}
$$
co tak naprawdę sprowadza się do jednego słowa $ac$.

---

## Zadanie 4.

> Niech $G$ będzie gramatyką generującą poprawnie zbudowane formuły rachunku zdań ze zmiennymi zdaniowymi $p$ i $q$. Symbolami terminalnymi w $G$ są $p,q,(,),\neg,\Rightarrow$, a produkcjami $S \to \neg S | (S \Rightarrow S) | p | q$.
>
> Znajdź gramatykę w postaci normalnej Chomsky’ego generującą ten sam język.\
> Dla uzyskanej gramatyki w [postaci normalnej Chomsky’ego](../../wyk/2020-10-29/gramatyki-bezkontekstowe.md#12-postać-normalna-chomskyego) znajdź równoważną gramatykę w [postaci normalnej Greibach](../../wyk/2020-10-29/gramatyki-bezkontekstowe.md#13-postać-normalna-greibach).

### Postać normalna Chomsky’ego

Najpierw przekształcamy do postaci normalnej Chomsky’ego.

Narazie mamy: $S \to p|q$.

Produkcję $S \to \neg S$ zastępujemy:
- $S \to AS$
- $A \to \neg$

Produkcję $S \to (S \Rightarrow S)$ zastępujemy:
- $S \to BC$
- $B \to ($
- $C \to SD$
- $D \to EF$
- $E \to \Rightarrow$
- $F \to SG$
- $G \to )$

---

### Postać normalna Greibach

Teraz przekształcamy do postaci normalnej Greibach.

Narazie mamy:
- $S \to p|q$
- $A \to \neg$
- $B \to ($
- $E \to \Rightarrow$
- $G \to )$

Produkcję $S \to AS$ zastępujemy przez $S \to \neg S$.

Produkcję $S \to BC$ zastępujemy przez $S \to (C$.

Produkcję $D \to EF$ zastępujemy przez $D \to \Rightarrow F$

Pozostają do przekształcenia produkcje $C \to SD$ oraz $F \to SG$. Ponieważ wszystkie produkcje z $S$ są w postaci normalnej Greibach, zastępujemy $S$ z prawej strony wszystkim, czym możemy:
- $C \to pD | qD | \neg SD | (CD$
- $F \to pG | qG | \neg SG | (CG$

Usuwamy już niepotrzebne produkcje $A,B,E$ .

Ostatecznie mamy produkcje:
$$
\begin{aligned}
    S &\to p | q | \neg S | (C\\
    C &\to pD | qD | \neg SD | (CD\\
    D &\to \Rightarrow F\\
    F &\to pG | qG | \neg SG | (CG\\
    G &\to )
\end{aligned}
$$

---

## Zadanie 5.

> Znaleźć gramatykę w [postaci normalnej Greibach](../../wyk/2020-10-29/gramatyki-bezkontekstowe.md#13-postać-normalna-greibach) równoważną z następującą gramatyką bezkontekstową:
> $$
> \begin{aligned}
>     S &\to AA | 0\\
>     A &\to SS | 1\\
> \end{aligned}
> $$
> z nieterminalami $S$ i $A$ oraz terminalami $0$ i $1$.

Mamy produkcje:
$$
\begin{aligned}
    A_1 &\to A_2 A_1 | 0\\
    A_2 &\to A_1 A_1 | 1\\
\end{aligned}
$$

Ponieważ prawe strony produkcji $A_1 \to A_2 A_2 | 0$ zaczynają się od terminali lub nieterminali o wyższych indeksach robimy podstawienie:
$$
\begin{aligned}
    A_1 &\to A_2 A_2 | 0\\
    A_2 &\to A_2 A_2 A_1 | 0 A_1 | 1\\
\end{aligned}
$$

Do produkcji $A_2 \to A_2 \underbrace{A_2 A_1}_{\alpha_1} | \underbrace{0 A_1}_{\beta_1} | \underbrace{1}_{\beta_2}$ wykorzystujemy [lemat z wykładu](../../wyk/2020-10-29/gramatyki-bezkontekstowe.md#132-lemat2).

Otrzymujemy zatem:
$$
\begin{aligned}
    A_2 &\to \overbrace{0 A_1}^{\beta_1} | \overbrace{1}^{\beta_2} | \overbrace{0 A_1 B}^{\beta_1 B} | \overbrace{1 B}^{\beta_2 B}\\
    B &\to \underbrace{A_2 A_1}_{\alpha_1} | \underbrace{A_2 A_1 B}_{\alpha_1 B}
\end{aligned}
$$

Ponieważ wszystkie produkcje z $A_2$ są w postaci normalnej Greibach, robimy podstawienie za pierwsze $A_2$ znajdujące się po prawej stronie produkcji z $A_1$ oraz z $B$:
$$
\begin{aligned}
    A_1 &\to 0 A_1 A_2 | 1 A_2 | 0 A_1 B A_2 | 1 B A_2 | 0\\
    A_2 &\to 0 A_1 | 1 | 0 A_1 B | 1B\\
    B   &\to 0 A_1 A_1 | 1 A_1 | 0 A_1 B A_1 | 1 B A_1 | 0 A_1 A_1 B | 1 A_1 B | 0 A_1 B A_1 B | 1 B A_1 B
\end{aligned}
$$

Teraz wystarczy tylko zamienić $A_1$ na $S$ oraz $A_2$ na $A$.

---

## Zadanie 6.

### Zadanie 6.1.

> Pokazać, że jeśli wszystkie produkcje gramatyki bezkontekstowej mają postać $A \to wB$ lub $A \to w$, gdzie $A$ i $B$ są symbolami nieterminalnymi a w słowem złożonym tylko z symboli terminalnych, to język generowany przez tą gramatykę jest regularny.

Mamy
- gramatykę $G = (N,T,P,S)$, gdzie
    - $P = \left\{ A \to wB \lor A \to w:\enspace w \in T^+ \land A,B \in N \right\}$
- NFA $M = \left(Q, T, \delta, S, \{q_F\}\right)$, gdzie
    - $Q = N \cup \{q_F\}$

**Cel: pokazać, że $L(M) = L(G)$**, bo jeżeli mamy NFA to mamy też wyrażenie regularne.

Definiujemy funkcję przejścia:\
Stanami są nieterminale, bo nieterminale oznaczają, że słowo się jeszcze nie skończyło — tak samo, jak w automacie, gdzie tylko jeden (ten dodatkowy) stan $q_F$ jest akceptujący, kiedy pozostałe są stanami „tymczasowymi”.
- $\delta(A, w) = \{B: (A \to wB) \in P\}$
- $\delta(A, w) = \{q_F\}$, jeśli $(A \to w) \in P$, bo jeśli nieterminal przechodzi na sam ciąg terminali oznacza to zamknięcie wyprowadzania słowa

Istotne jest zauważyć, że skoro w gramatyce dla pewnego słowa $w = w_1 w_2\dots w_n$\
mamy pewne wyprowadzenie $S \Rightarrow w_1 A_1 \Rightarrow w_1 w_2 A_2 \Rightarrow \dots \Rightarrow w_1 w_2 \dots w_{n-1} A_{n-1} \Rightarrow w_1 w_2 \dots w_n$,\
to również przy pomocy funkcji przejścia $\delta$ jesteśmy w stanie wyprowadzić takie same słowo, czyli dojść do stanu akceptującego $q_F$:\
$q_F \in \delta(A_{n-1}, w_n);\, A_{n-1} \in \delta(A_{n-2}, w_{n-1});\, \dots; A_2 \in \delta(A_1, w_2);\, A_1 \in \delta(S, w_1)$, a wynika to z definicji funkcji $\delta$, którą przed chwilą zdefiniowaliśmy.

Czyli jesteśmy w stanie „wystrugać” sobie takie samo słowo używając obu języków $L(G), L(M)$. Skłania to do stwierdzenia, że $L(G) = L(M)$.

---

### Zadanie 6.2.
> Pokazać, że jeśli język jest regularny, to istnieje gramatyka bezkontekstowa generująca ten język, w której wszystkie produkcje mają postać $A \to aB$ lub $A \to a$, gdzie $A$ i $B$ są symbolami nieterminalnymi a $a$ symbolem terminalnym.

Mamy
- DFA (odpowiadający wyrażeniu regularnemu) $M = (Q, \Sigma, \delta, S, F)$
- gramatykę $G = (Q, \Sigma, P, S)$ gdzie
    - $P = \left\{ A \to aB:\enspace a \in T \land A \in N \land (B \in N \lor B = \epsilon) \right\}$

**Cel: pokazać, że $L(M) = L(G)$**.

I znowu tłumaczymy zapis automatowy na gramatyczny, definiujemy produkcję $P$ tłumacząc $\delta(A, a) = B$ na produkcje:
- $A \to aB$ jeśli $B \notin F$ (nie jest stanem akceptującym, nie można zakończyć wyprowadzenia słowa)
- $A \to a$ jeśli $B \in F$ oth.

oczywiście $A,B \in Q$ (stany, przetłumaczone na nieterminale), kiedy $a$ to dany terminal.

Analogicznie do [zadania 6.1.](#zadanie-61) jesteśmy w stanie przetłumaczyć przejścia w automacie na przejścia w wyprowadzaniu słowa w gramatyce.

Należy zauważyć, że skoro w automacie dla pewnego słowa $a = a_1 a_2 \dots a_n$ możemy znaleźć drogę z stanu początkowego $S$ do pewnego stanu $B \in F$:\
$\delta(S, a_1) = A_1;\, \delta(A_1, a_2) = A_2;\, \dots; \delta(A_{n-2}, a_{n-1}) = A_{n-1};\, \delta(A_{n-1}, a_n) = B$,\
to również w gramatyce $G$ jesteśmy w stanie wyprowadzić takie samo słowo:\
$S \Rightarrow a_1 A_1 \Rightarrow a_1 a_2 A_2 \Rightarrow \dots \Rightarrow a_1 a_2 \dots a_{n-1} A_{n-1} \Rightarrow a_1 a_2 \dots a_n$\
a wynika to z budowy zbioru produkcji, który przed chwilą zdefiniowaliśmy. *(tutaj, w celu zobrazowania analogii, można na końcu jeszcze dopisać nieterminal $B$, który przechodzi na $\epsilon$)*

Czyli jesteśmy w stanie „wystrugać” sobie takie samo słowo używając obu języków $L(G), L(M)$. Skłania to do stwierdzenia, że $L(G) = L(M)$.

---
