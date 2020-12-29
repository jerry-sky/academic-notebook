---
lang: 'pl'
title: 'Problem znalezienia $k$tej statystyki pozycyjnej w nieposortowanej tablicy'
author: 'Jerry Sky'
date: '2020-03-23'
---

---

- [Specyfikacja](#specyfikacja)
- [Outline problemu](#outline-problemu)

---

## Specyfikacja

`input : ` $A = (a_1,\dots,a_n),~k\in \{1,\dots,n\}$\
`output: ` $k$ty najmniejszy element z tablicy $A$

## Outline problemu

1. Naiwny algorytm mógłby najpierw posortować tablicę $A$ *(złożoność obliczeniowa conajmniej $O(n\ln n)$)* i zwrócić $k$ty element

2. Jeśli $k=1$ to wyznaczamy $\min$ z $A$,\
natomiast gdy $k=n$ to wyznaczamy $\max$ z $A$ - potrafimy to trywialnie zrobić w złożoności $O(n)$ zwyczajnie przeglądając całą tablicę

3. Jeśli $k = \big\lfloor \frac{n}{2} \big\rfloor$ to wyznaczamy medianę - wykonanie tego w złożoności liniowej jest nietrywialne - więcej informacji [tutaj *(2.4 Medians)*][algorithms].

[algorithms]: http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf
