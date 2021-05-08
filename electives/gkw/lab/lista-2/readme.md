---
lang: 'pl'
title: 'Lista 2.'
subtitle: 'Grafika komputerowa i wizualizacje, Laboratorium'
author: 'Jerzy Wroczyński'
---

- [Informacje techniczne](#informacje-techniczne)
- [Zadanie 1. Testowanie WebGL](#zadanie-1-testowanie-webgl)
- [Zadanie 2.](#zadanie-2)

---

## Informacje techniczne

Pliki źródłowe TypeScript znajdują się w:
- `types.ts` — podstawowe typy,
- `ex-1-2-3` — zadania 1. 2. i 3,
- `ex-4` — zadanie 4,
- `ex-5` — zadanie 5.

W katalogu `dist` znajduje się skompilowana wersja, której podgląd można zobaczyć przy pomocy przeglądarki.
Wystarczy otworzyć plik `index.html` w danym pod-katalogu `dist/` z zadaniem.
Przykładowo rozwiązanie zadania 1. znajduje się w pliku `dist/ex-1-2-3/index.html`.

Do rozwiązań dołączony jest plik `makefile` umożliwiający następujące polecenia:
- `make` —  buduje rozwiązania do wszystkich zadań,
- `make dev` — uruchamia całą listę jako program w trybie deweloperskim
(program jest rekompilowany przy każdej zmianie któregokolwiek z plików).

Przed wykorzystaniem powyższych poleceń należy zainstalować wszystkie potrzebne paczki przy pomocy polecenia `npm i`.
Wymaga to `node` oraz `npm` zainstalowanych w systemie.

---

## Zadanie 1. Testowanie WebGL

> Napisz prosty program, który demonstruje rysowanie w WebGL obiektów geometrycznych:
> - `POINTS`,
> - `LINE_STRIP`,
> - `LINE_LOOP`,
> - `LINES`,
> - `TRIANGLE_STRIP`,
> - `TRIANGLE_FAN`,
> - `TRIANGLES`.
>
> Zastosować zmienne uniform do ustalania pewnych parametrów rysowania
> (np. kolorów, przekształceń geometrycznych itp.)
>
> Należy także:
> - wypisać w konsoli lub na stronie listę aktywnych atrybutów,
>     zgodnie z przykładem na stronie <https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/getActiveAttrib>,
> - analogicznie wykorzystać `getActiveUniform`, aby wypisać listę zmiennych uniform.
>     <https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/getActiveUniform>
> - zademonstrować działanie `bindAttribLocation`, aby przypisać zmienne *attribute variable* do ustalonych przez użytkownika indeksów *generic vertex index*.
>     <https://developer.mozilla.org/en-US/docs/Web/API/WebGLRenderingContext/bindAttribLocation>

[»Strona«](dist/ex-1/index.html)

---

## Zadanie 2.

> Wygeneruj zbiory odcinków / trójkątów składających się na trójkąty Sierpińskiego / płatki Kocha różnego stopnia,
>
> Umieść odpowiednie dane w buforach i zaimplementuj shadery rysujące te dane w kontekście webgl.
> Napisz interakcyjny program,
> który rysuje krzywe różnego stopnia w różnych kolorach na różnych głębokościach (współrzędna z),
> tak aby krzywe o większych głębokościach stanowiły tło krzywej o najmniejszej głębokości,
> i umożliwia przy pomocy klawiszy lub przycisków operacje takie jak przesuwanie krzywych,
> zmiany głębokości.

[»Strona«](dist/ex-2/index.html)

---
