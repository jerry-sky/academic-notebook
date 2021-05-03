---
lang: 'pl'
title: 'Lista 2.'
subtitle: 'Nowoczesne Technologie WWW, Laboratorium'
author: 'Jerzy Wroczyński'
date: '2021-05-06'
---

- [Zadanie 1.](#zadanie-1)
- [Zadanie 2.](#zadanie-2)

---

## Zadanie 1.

Do swojego portfolio:
- dołącz w osobnym pliku `js` i wykorzystaj skrypt generujący responsywne,
dynamicznie zmieniające się pod wpływem zdarzeń menu
(dla najmniejszych ekranów mobilnych stwórz tzw. „menu hamburgerowe”),
- przepuść skrypt przez JS LINT (<http://www.jslint.com/>)
i postaraj się wyeliminować wszystkie błędy i ostrzeżenia,
- uwzględnij w projekcie alternatywną wersję menu dla przeglądarek nieobsługujących
lub mających wyłączoną obsługę JavaScript.

[»Strona«](ex-1/index.html)

---

## Zadanie 2.

Wykorzystując wyłącznie HTML, CSS oraz JavaScript napisz od podstaw układankę obrazkową,
spełniającą następujące wymagania:
- przyjmuje jeden z dostępnych obrazków oraz `liczbaKolumn = liczbaWierszy = 4`
    jako parametry domyślne gry,
- dla zadanych parametrów (obrazek, liczba kolumn i wierszy) na elemencie `<canvas>`
    uruchamiana jest gra o następujących zasadach:
    - obrazek zostaje pocięty w pionie i poziomie na klocki zgodnie z przy-
    jętymi parametrami,
    - klocki są pierwotnie wymieszane (w sposób odwracalny zgodnie z zasadami gry),
    - klocek w górnym lewym rogu jest zamalowany na czerwono,
    - użytkownik, naciskając na klocek przylegający jedynym bokiem do czerwonego,
        może zamienić je miejscami,
    - najechanie na klocek przylegający do czerwonego powoduje jego podświetlenie,
    - kliknięcie klocka nieprzylegającego do czerwonego nie wyzwala żadnych akcji,
    - celem gry jest ułożenie obrazka z dokładnością do czerwonego klocka,
    - po spełnieniu celu gra zaczyna się od nowa,
- w dowolnym momencie użytkownik może przerwać grę i uruchomić ją od nowa,
- w dowolnym momencie użytkownik może zmienić parametry gry
    (obrazek liczba kolumn, liczba wierszy układanki) i zacząć nową rozgrywkę.
    W celu wybrania obrazka wyświetl prostą galerię 12 obrazków,
    spośród których użytkownik może wybrać jeden do układania
    (najpierw załaduj zdjęcia skompresowane, a potem wykorzystaj obietnice
    do ładowania równoległego zdjęć dobrej jakości).

[»Strona«](ex-2/index.html)

---
