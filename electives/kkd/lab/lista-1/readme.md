---
lang: 'pl'
title: 'Lista-1'
author: 'Jerry Sky'
---

---

## Zadanie na laboratorium

> Dla dyskretnych zmiennych losowych $X$ i $Y$ entropia $Y$ warunkowana przez $X$ jest określona wzorem
> $$
> H(Y|X) = \sum_{x\in X}P(x) \cdot H(Y|x)
> $$
> gdzie
> $$
> H(Y|x) = \sum_{y\in Y}P(y|x) \cdot I(y|x)
> $$
> a $P(z)$ oznacza prawdopodobieństwo $z$ a $I(z)$ informację związaną z $z$.
>
> Napisz program który dla podanego pliku traktowanego jako ciąg 8-bitowych symboli policzy częstość występowania tych symboli oraz częstość występowania symboli po danym symbolu (częstość występowania pod warunkiem, że poprzedni znak jest dany, dla pierwszego znaku przyjmij, że przed nim jest znak o kodzie $0$). Dopisz funkcje które dla policzonych częstości traktowanych jako zmienne losowe policzy entropię i entropię warunkową (warunkowaną znajomością poprzedniego symbolu), oraz poda różnicę między nimi.
>
> Program ma wypisywać wyniki w sposób czytelny i łatwy do dalszego przetwarzania.
>
> Przeanalizuj wyniki działania swojego programu dla przykładowych plików tekstowych, `doc`, `pdf`, `mp4` czy `jpg` (weź pliki o rozmiarze co najmniej 1MB).

## Uruchomienie programu

W celu uruchomienia programu należy najpierw go skompilować przy pomocy `make` a następnie `./main.out <plik do otwarcia>` (przykładowe uruchomienie `./main.out pan-tadeusz.txt`).

Cały [kod](main.cpp) jest zawarty w pliku `main.cpp`.

---

Poniżej znajdują się dodatkowe uproszczenia wzorów w celu dokładniejszego działania programu.

## Entropia warunkowa

$P(y|x) = \frac{P(y~\cap~x)}{P(x)} = \frac{|y~\cap~x|}{|x|}$

$I(y|x) = -\log_2(~P(y|x)~)$

$H(Y|x) = \sum_{y \in Y}P(y|x)\cdot I(y|x)$

$H(Y|X) = \sum_{x \in X}P(x)\cdot H(Y|x)$

podstawmy:\
$H(Y|X) = \sum_{x \in X}(~P(x)\cdot \sum_{y \in Y}P(y|x)\cdot I(y|x)~)$\
$H(Y|X) = \sum_{x \in X}(~P(x)\cdot \sum_{y \in Y}P(y|x)\cdot (-\log_2(~P(y|x))~)$

mamy przecież:
$$
P(x) = \frac{|x|}{|\Omega|}
$$
oraz:
$$
P(y|x) = \frac{P(y \cap x)}{P(x)} = \frac{|y \cap x|}{|x|}
$$
wówczas:
$$
H(Y|X) = \sum_{x \in X}(~\frac{|x|}{|\Omega|}\cdot \sum_{y \in Y}\frac{|y \cap x|}{|x|}\cdot (-\log_2(~\frac{|y \cap x|}{|x|})~)
$$
$$
H(Y|X) = \sum_{x \in X}(~\sum_{y \in Y} \frac{|x|}{|\Omega|} \cdot \frac{|y \cap x|}{|x|}\cdot (-\log_2(~\frac{|y \cap x|}{|x|})~)
$$
$$
H(Y|X) = \sum_{x \in X}(~\sum_{y \in Y} \frac{|y \cap x|}{|\Omega|}\cdot (-\log_2(~\frac{|y \cap x|}{|x|})~)
$$
$$
H(Y|X) = \sum_{x \in X}(~\sum_{y \in Y} \frac{|y \cap x|}{|\Omega|}\cdot (-\log_2(~|y \cap x|)~ + log_2|x|)
$$
$$
H(Y|X) = \sum_{x \in X}(~\sum_{y \in Y} \frac{|y \cap x|}{|\Omega|}\cdot (-\log_2(~|y \cap x|)~ + log_2|x|)
$$

## Zwykła entropia

$$
H(X) = \sum_{x \in X}P(x)\cdot I(x)
$$
przy czym $I(x) = -\log_2 P(x)$
$$
H(X) = \sum_{x \in X}\frac{|x|}{|\Omega|}\cdot (-\log_2 \frac{|x|}{|\Omega|})
$$
$$
H(X) = \frac{1}{|\Omega|}\cdot\sum_{x \in X}|x|\cdot (-\log_2 \frac{|x|}{|\Omega|})
$$
$$
H(X) = \frac{1}{|\Omega|}\cdot\sum_{x \in X}|x|\cdot (-\log_2 |x| + log_2 |\Omega|)
$$
$$
H(X) = \frac{1}{|\Omega|}\cdot\sum_{x \in X}|x|\cdot (-\log_2 |x|) + \frac{1}{|\Omega|} \cdot log_2 |\Omega| \cdot \sum_{x \in X} |x|)
$$
$$
H(X) = \frac{1}{|\Omega|}\cdot\sum_{x \in X}|x|\cdot (-\log_2 |x|) + log_2 |\Omega|
$$
