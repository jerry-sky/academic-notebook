# Wzbogacanie struktur danych
*(2020-04-6)*

## Zarys

Podczas projektowania algorytmów często przeprowadza się wzbogacanie znanej struktury danych w celu przystosowania jej do wykonania dodatkowych zadań.

## Steps

1. Wybieramy *znaną* strukturą danych.
2. Ustalamy jaką dodatkową informację chcemy przechowywać w naszej strukturze.
3. Sprawdzamy czy możemy aktualizować efektywnie tą dodatkową informację podczas wykonywania operacji modyfikujących naszą podstawową strukturę danych.

    *Słowo „efektywnie” w powyższym zdaniu należy rozumieć jako „nie zwiększając asymptotycznej złożoności obliczeniowej operacji”, ale może się zdarzyć, że jest to niemożliwe. Wówczas dopuszczamy zwiększenie złożoności obliczeniowej operacji na strukturze dopóki użycie danej struktury „ma sens, jest uzasadnione innymi aspektami”.*
4. Zaprojektowanie nowych operacji, które używając dodatkowych informacji przechowywanych w strukturze danych pozwolą nam na osiągnięcie zakładanego celu.

## Przykład

Dynamiczne statystyki pozycyjne - mając dynamiczny zbiór danych chcemy szybko wyznaczać $i$tą statystyką pozycyjną oraz zwracać statystykę pozycyjną zadanego elementu.\
[**Rozszerzymy tutaj strukturę RB-Tree.**](rb-trees-ze-statystykami-pozycyjnymi.md)

## Więcej

Więcej na temat wzbogacania struktur danych:

- [Chapter 14](https://web.ist.utl.pt/~fabio.ferreira/material/asa/clrs.pdf)
- [aisd04.pdf](https://drive.google.com/drive/folders/0B83LMR1NBoUXLXdYZ2hsNFBqTTA)
