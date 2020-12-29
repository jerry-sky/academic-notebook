---
lang: 'pl'
title: 'Koszt zamortyzowany'
author: 'Jerry Sky'
date: '2020-04-22'
---

---

- [$\text {Def}$](#text-def)
- [Metody analizy kosztu zamortyzowanego](#metody-analizy-kosztu-zamortyzowanego)
    - [Metoda kosztu sumarycznego](#metoda-kosztu-sumarycznego)
    - [Metoda księgowania](#metoda-księgowania)
    - [Metoda potencjału](#metoda-potencjału)
- [Stosujemy metodę potencjału](#stosujemy-metodę-potencjału)
- [Przykład, `Increment`](#przykład-increment)
    - [Wykorzystanie metody potencjału](#wykorzystanie-metody-potencjału)

---

## $\text {Def}$

Koszt zamortyzowany (zamortyzowana złożoność obliczeniowa) operacji jest jej średnim kosztem w najgorszym przypadku.

## Metody analizy kosztu zamortyzowanego

### Metoda kosztu sumarycznego

Określa się górne ograniczenie $T(n)$ na całkowitą złożoność obliczeniową (w pesymistycznym przypadku) ciągu $n$ badanych operacji. Koszt zamortyzowany każdej operacji rozumiemy wtedy przez $T(n)/n$.

### Metoda księgowania

Rozpatrując ciąg operacji, zawyżamy koszt operacji znajdujących się na początku ciągu. Nadpłaty te zostają potem zużyte na „zapłacenie” za operacje, których złożoność jest mniejsza niż faktycznie poniesione koszty.

### Metoda potencjału

Podobnie jak w [metodzie księgowania](#metoda-ksi%c4%99gowania), przypisujemy większy koszt wcześniejszym operacjom, aby skompensować późniejsze nadmierne wydatki. W metodzie potencjału „kredyt” jest reprezentowany jako „energia potencjalna” całej struktury danych i nie jest związana z pojedynczymi obiektami (jak to ma miejsce w [metodzie księgowania](#metoda-ksi%c4%99gowania)).\
Skupimy się na metodzie potencjału.

## Stosujemy metodę potencjału

Będziemy rozpatrywali ciąg $n+1$ struktur $D_0,D_1,\dots,D_n$, gdzie $D_i$ będzie strukturą danych powstałą ze struktury $D_{i-1}$ po wykonaniu $i$-tej operacji.

Rozważmy funkcją potencjału $\Phi$ przyporządkowującą każdej strukturze $D_i$ liczbę rzeczywistę nazywaną potencjałem struktury $D_i$.

Dla każdego $i = 1,\dots,n$ niech $c_i$ oznacza faktyczną złożoność obliczeniową $i$-tej operacji, a $\hat c_i$ oznacza koszt zamortyzowany dla $i$-tej operacji i definiujemy go jako $\hat c_i = c_i + \Phi(D_i) - \Phi(D_{i-1})$.

Zatem po prostych przekształceniach koszt zamortyzowany ciągu $n$ operacji wynosi:
$$
\sum_{i=1}^{n}\hat{c}_i = \sum_{i=1}^{n}c_i + \Phi(D_n) - \Phi(D_0)
$$
Zwykle dla wygody definiuje się $\Phi(D_0) = 0$. Jeśli jesteśmy w stanie pokazać, że $\Phi(D_j) \ge 0$ dla każdego $j =1,\dots,n$ wówczas koszt zamortyzowany ciąg $j$ operacji (dla dowolnego $j$) ogranicza z góry koszt faktyczny ciąg $j$ operacji:
$$
\sum_{i=1}^{j}c_i \le \sum_{i=1}^{j}\hat{c}_i
$$

Koszt zamortyzowany zdefiniowany jak powyżej zależy od wybory funkcji potencjału $\Phi$. Używając różnych funkcji potencjału, można otrzymać różne koszty zamortyzowane i mimo wszystko otrzymać górne ograniczenie faktycznej złożoności obliczeniowej ciągu operacji.

## Przykład, `Increment`

W celu zilustrowania obliczania kosztu zamortyzowanego posłużymy się przykładem $k$ bitowego licznika binarnego, który zlicza od $0$ za pomocą operacji `Increment`. Licznik jest przetrzymywany w tablicy bitów $A[0\dots k-1]$ długości $k$. Najmniej znaczący bit występuje w $A[0]$, a najbardziej znaczący w $A[k-1]$, zatem jeśli licznik przechowuje liczbę $x$ to
$$
x = \sum_{i=0}^{k-1}A[i]\cdot2^i
$$
Licznik inicjalizujemy ustawiając bit $0$ w każdej komórce tablicy $A$. Aby zwiększyć wartość licznika o $1$ (modulo $2^k$), używamy wcześniej wspomnianej procedury:
```
Increment(A):
  i = 0
  while i < k and A[i] == 1:
    A[i] = 0
    i++
  if i < k:
    A[i] = 1
```
Operacja ta dokonuje zmiany odpowiednich bitów (zaczynając od najmniej znaczących): $1\to0$ i po natrafieniu na najmniej znaczący bit zerowy zamienia go na $1$.\
Koszt (złożoność obliczeniowa) każdej operacji `Increment` jest równy liczbie zmienionych bitów. Analizując złożoność obliczeniową pojedynczej operacji `Increment` w *worst case scenario*, widzimy, że asymptotycznie wynosi ona $\Theta(k)$, bo w najgorszym przypadku w tablicy wszystkie bity będą ustawione na $1$ i będziemy musieli je wyzerować lub wszystkie bity poza najbardziej znaczącym zostaną one wyzerowane, a bit $A[k-1]$ zostanie ustawiony na $1$.

Zauważmy natomiast, że w innych przypadkach liczba modyfikowanych bitów będzie mniejsza, więc istnieje szansa, że da się ograniczyć pesymistyczną złożoność ciągu $n$ operacji `Increment` przez coś mniejszego niż $O(n\cdot k)$.

### Wykorzystanie metody potencjału

Wykorzystajmy metodę potencjału do obliczenia kosztu zamortyzowanego operacji `Increment`.

1. Wybór funkcji potencjału: $\Phi(D_i)$ będzie liczbą jedynek w liczniku po $i$-tej operacji.
2. Załóżmy, że $i$-ta operacja `Increment` zeruje $t_i$ bitów. Faktyczny koszt tej operacji jest więc ograniczony przez $c_i \le t_i + 1$, ponieważ oprócz zerowania $t_i$ bitów może ona przypisać wartość co najwyżej jednemu bitowi.
3. Z poprzedniego punktu możemy uzyskać ograniczenie na wyżej zdefiniowaną funkcję potencjału:
    $$
    \Phi(D_i) \le \Phi(D_{i-1}) - t_i + 1.
    $$
4. Stąd koszt zamortyzowany $i$-tej operacji możemy wyliczyć w następujący sposób:
    $$
    \hat c_i = c_i + \Phi(D_i) - \Phi(D_{i-1}) \le (t_i + 1) - (-t_i + 1) = 2 = \Theta(1).
    $$
    Jeśli zaczynamy zliczać za pomocą licznika od zera, to $\Phi(D_0) = 0$.

    Ponieważ $\Phi(D_i) \ge 0$ dla każdego $i$, to koszt zamortyzowany ciągu $n$ operacji `Increment` jest górnym ograniczeniem kosztu faktycznego, co daje pesymistyczny koszt ciągu $n$ operacji równy $O(n)$.
5. Za pomocą metody potencjału łatwo jest również dokonać analizy w przypadku gdy licznik nie startuje od $0$.

    Załóżmy, że początkowo było $b_0$ zer oraz po wykonaniu $n$ razy operacji `Increment` mamy $b_n$ jedynek., gdzie $0 \le b_0 \land b_n \le k$, wówczas:
    $$
    \sum_{i=1}^{n} = \sum_{i=1}^{n}\hat c_i - \Phi(D_n) + \Phi(D_0).
    $$
    Mamy $\forall_{1\le i\le n}~ \hat c_i \le 2$. Skoro $\Phi(D_0) = b_0$ oraz $\Phi(D_n) = b_n$, całkowity koszt wykonania $n$ razy operacji `Increment` wynosi
    $$
    \sum_{i=1}^{n} \le \sum_{i=1}^{n}2 - b_n + b_0 = 2n - b_n + b_0.
    $$
    Należy zauważyć, że jeśli $k = O(n)$ to $b_0 \le k$ co daje nam całkowity koszt równy $O(n)$.

    **Oznacza to tyle, że jeśli wykonamy przynajmniej $n=\Omega(k)$** razy operację `Increment` całkowity koszt zawsze będzie złożoności $O(n)$ niezależnie od początkowego stanu licznika.

    [Section 17.3](https://web.ist.utl.pt/~fabio.ferreira/material/asa/clrs.pdf)
