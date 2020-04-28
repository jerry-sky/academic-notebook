# Longest Common Subsequence (LCS)
*(2020-04-20)*

[clrs]: https://web.ist.utl.pt/~fabio.ferreira/material/asa/clrs.pdf

## Problem

Znalezienie najdłuższego wspólnego podciągu dwóch ciągów $x[1\dots m],~y[1\dots n]$.

## Przykład

Mamy $x = (A,B,C,B,D,A,B)$ oraz $y = (B,D,C,A,B,A)$.\
Najdłuższym wspólnym podciągiem tych ciągów są $\text{BDAB}$, $\text{BCAB}$ oraz $\text{BCBA}$.

## Brute force

Dla każdego podciągu ciągu $x$ sprawdź czy taki istnieje w ciągu $y$ i zapamiętaj najdłuższy do tej pory znaleziony.\
Liczba możliwych podciągów ciągu $x$ o długości $m$ to $2^m$. Sprawdzenie czy jakiś podciąg $x$ występuje w $y$ długości $n$ zajmuje $O(n)$, zatem złożoność obliczeniowa takiego algorytmu to $O(n2^m)$ — wykładnicza złożoność obliczeniowa.

## Podejście programowania dynamicznego

Musimy zdefiniować pod-problemy, ich kolejność oraz relację pomiędzy nimi, co da nam DAG-a odpowiadającego problemowi LCS. Podobnie jak w poprzednio rozpatrywanych problemach, tutaj również zaczniemy od znalezienia długości najdłuższego wspólnego podciągu $|\mathrm{LCS}(x,y)|$, a następnie podamy procedurę odtworzenia $\mathrm{LCS}(x,y)$.

Niech $c(i,j) = |\mathrm{LCS}(x[1\dots i], y[\dots j])|$ będzie długością najdłuższego wspólnego podciągu prefiksów ciągów $x$ oraz $y$. Dla każdego $i = 1,\dots,m$ oraz $j = 1,\dots,n: c(i,j)$ będą pod-problemami, a $c(m,n)$ będzie długością najdłuższego wspólnego pociągu ciągów $x$ oraz $y$.

Zauważmy, że
$$
c(i,j) =
\begin{cases}
  0 & i = 0 \lor j = 0\\
  c(i - 1, j - 1) + 1 & x[i] = y[j]\\
  \max\{~c(i-1, j),~c(i,j-1)~\} & \text{otherwise}
\end{cases}
$$
Powyższy fakt ma dowód pochodzący z [rozdziału 15.4 książki Introduction to algorithms by CLRS][clrs]:

### Theorem Optimal substructure of an LCS

Let $X = \langle x_1,x_2,\dots,x_m\rangle$ and $Y = \langle y_1,y_2,\dots,y_n\rangle$ be sequences and let $Z = \langle z_1,z_2,\dots,z_k\rangle$ be any LCS of $X$ and $Y$.

*A prefix of $A$ is noted as $A_t$. $A_t$ contains first $t$ elements of $A$.*

1. If $x_m = y_n$, then $z_k = x_m = y_n$ and $Z_{k-1}$ is an LCS of $X_{m-1}$ and $Y_{n-1}$.
2. If $x_m \neq y_n$, then $z_k \neq x_m$ implies that $Z$ in an LCS of $X_{m-1}$ and $Y$.
3. If $x_m \neq y_n$, then $z_k \neq y_n$ implies that $Z$ is an LCS of $X$ and $Y_{n-1}$.

**Proof**:
1. If $z_k \neq x_m$, then we could append $x_m = y_n$ to $Z$ to obtain a common subsequence of $X$ and $Y$ of length $k+1$, contradicting the supposition that $Z$ is a *longest* common subsequence of $X$ and $Y$. Thus, we must have $z_k = x_m = y_n$. Now, the prefix $Z_{k-1}$ is a length-$(k-1)$ common subsequence of $X_{m-1}$ and $Y_{n-1}$. We wish to show that is in an LCS. Suppose for the puprose of contradiction that there exists a common subsequence $W$ of $X_{m-1}$ and $Y_{n-1}$ with length greater than $k-1$. Then appending $x_m = y_n$ to $W$ produces a common subsequence of $X$ and $Y$ whose length is greater than $k$, which is a contradiction \[with the supposition that $Z$ is the LCM of $X$ and $Y$].
2. If $z_k \neq x_m$, then $Z$ is a common subsequence of $X_{m-1}$ and $Y$. If there were a common subsequence $W$ of $X_{m-1}$ and $Y$ with length greater than $k$, then $W$ would also be a common sequence of $X_m$ and $Y$, contradicting assumption is an LCS of $X$ and $Y$.
3. The proof is symmetric to `2.`.

### Kolejność pod-problemów

Fakt ten określa nam kolejność pod-problemów
$c(i -1, j -1)$, $c(i-1,j)$, $c(i,j-1)$ są w porządku przed problemem $c(i,j)$, oraz relację pomiędzy nimi.\
Możemy zatem zauważyć, że DAG odpowiadający problemowi LCS jest kratą z wierzchołkami $c(i,j)$ i krawędziami $c(i-1,j-1) \rightarrow c(i,j)$, $c(i,j-1) \rightarrow c(i,j)$ oraz $c(i-1,j) \rightarrow c(i,j)$ dla $i = 0,\dots,m$ oraz $j = 0,\dots,n$.

Algorytm obliczający długość najdłuższego wspólnego podciągu sprowadza się do zaimplementowania obliczania $c(i,j)$ w porządku określonym przez stworzony DAG (zapamiętując rozwiązania pod-problemów) oraz wykorzystując relację pomiędzy pod-problemami opisaną w powyższym fakcie.

### Pseudokod

```
LCS-Length(X,Y):
  m = X.length
  n = Y.length
  let b[1..m, 1..n] and c[0..,0..n] be new tables

  for i = 1 to m:
    c[i,0] = 0
  for j = 0 to n:
    c[0,j] = 0
  for i = 1 to m:
    for j = 1 to n:
      if x_i == y_j:
        c[i,j] = c[i-1, j-1] + 1
        b[i,j] = „↖”
      elif c[i-1, j] ≥ c[i, j-1]:
        c[i,j] = c[i-1,j]
        b[i,j] = „↑”
      else:
        b[i,j] = „←”

  return c and b
```
[Source (Chapter 15.4)][clrs]

Złożoność obliczeniowa tak zdefiniowanego algorytmu wynosi $O(n\cdot m)$: mamy $n\cdot m$ pod-problemów, każdy rozwiązujemy w czasie stałym (wyniki to z relacji pomiędzy pod-problemami) jeśli mamy już rozwiązane pod-problemy, które występują wcześniej w określonym porządku.

## Odtwarzanie LCS

W celu odtworzenia jednego ze zbioru najdłuższych wspólnych podciągów, obliczając $c(i,j)$ musimy zapamiętać z którego pod-problemu korzystamy: $c(i-1,j-1)$, $c(i-1,j)$, $c(i,j-1)$. Następnie po obliczeniu wszystkich $c(i,j)$ zaczynamy przechodzić po naszym DAG-u rozpoczynając od wierzchołka $c(m,n)$ według następujących zasad:
- jeśli rozwiązując $c(i,j)$ użyliśmy $c(i-1,j-1)$ to dodajemy $x[i]$ (tożsame z $y[j]$) do naszego rozwiązanie i przechodzimy do $c(i-1, j-1)$
- jeśli rozwiązując $c(i,j)$ użyliśmy $c(i, j-1)$ to przechodzimy do $c(i,j-1)$ (nie dodajemy nic do rozwiązania)
- jeśli rozwiązując $c(i,j)$ użyliśmy $c(i-1,j)$ to przechodzimy do $c(i-1, j)$ (nie dodajemy nic do rozwiązania)
- kończymy jeśli $i=0 \lor j=0$.
