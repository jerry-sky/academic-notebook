---
lang: 'pl'
title: 'Lista 2.'
subtitle: 'Grafika komputerowa i wizualizacje, Laboratorium'
author: 'Jerzy Wroczyński'
---

- [Informacje techniczne](#informacje-techniczne)
- [Zadanie 1. Testowanie WebGL](#zadanie-1-testowanie-webgl)

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
