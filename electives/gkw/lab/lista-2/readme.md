---
lang: 'pl'
title: 'Lista 2.'
subtitle: 'Grafika komputerowa i wizualizacje, Laboratorium'
author: 'Jerry Sky'
---

- [Informacje techniczne](#informacje-techniczne)
- [Zadanie 1. — Testowanie WebGL](#zadanie-1--testowanie-webgl)
- [Zadanie 2. — Fraktale](#zadanie-2--fraktale)
- [Zadanie 3. — Gra komputerowa 2D](#zadanie-3--gra-komputerowa-2d)

---

## Informacje techniczne

Pliki źródłowe TypeScript znajdują się w:
- `types.ts` — podstawowe typy,
- `ex-*` — rozwiązania zadań z listy.

W katalogu `dist` znajduje się skompilowana wersja, której podgląd można zobaczyć przy pomocy przeglądarki.
Wystarczy otworzyć plik `index.html` w danym pod-katalogu `dist/` z zadaniem.
Przykładowo skompilowane rozwiązanie zadania 1. znajduje się w pliku `dist/ex-1/index.html`.

Do rozwiązań dołączony jest plik `makefile` umożliwiający następujące polecenia:
- `make` —  buduje rozwiązania do wszystkich zadań,
- `make dev` — uruchamia całą listę jako program w trybie deweloperskim
    (program jest rekompilowany przy każdej zmianie któregokolwiek z plików),
- `make clean` — usuwa wszystkie tymczasowe pliki pomocnicze (łącznie ze skompilowaną wersją).

Przed wykorzystaniem powyższych poleceń należy zainstalować wszystkie potrzebne paczki przy pomocy polecenia `npm i`.
Wymaga to `node` oraz `npm` zainstalowanych w systemie.

---

## Zadanie 1. — Testowanie WebGL

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

## Zadanie 2. — Fraktale

> Wygeneruj zbiory odcinków / trójkątów składających się na trójkąty Sierpińskiego / płatki Kocha różnego stopnia.
>
> Umieść odpowiednie dane w buforach i zaimplementuj shader-y rysujące te dane w kontekście WebGL.
> Napisz interakcyjny program,
> który rysuje krzywe różnego stopnia w różnych kolorach na różnych głębokościach (współrzędna z),
> tak aby krzywe o większych głębokościach stanowiły tło krzywej o najmniejszej głębokości,
> i umożliwia przy pomocy klawiszy lub przycisków operacje takie jak przesuwanie krzywych,
> zmiany głębokości.

[»Strona«](dist/ex-2/index.html)

---

## Zadanie 3. — Gra komputerowa 2D

> Zaimplementować w WebGL prostą dwuwymiarową grę zręcznościową typu:
> Pong, Arkanoid, Space Invaders,
> lub inną podobną, ale w taki sposób,
> aby tło zawierało jakiś rysunek utworzony z elementów geometrycznych (np. boisko).
>
> Wykorzystaj bufor głębokości tak,
> aby elementy pierwszoplanowe były rysowane z mniejszą współrzędną Z niż elementy tła.
> Zaimplementuj animację w zalecany sposób jak w przykładowym programie:
> <http://156.17.7.16/public/dydaktyka/kik/grafika/animation/animation.html>
> Zwróć uwagę, że callback animacji jest wywoływany w określonych punktach czasowych
> zależnych od częstotliwości wyświetlania obrazy na ekranie,
> natomiast zdarzenia istotne dla stanu gry,
> takie jak np. zderzenie obiektów, mogą wystąpić między tymi punktami czasowymi.
> Zadbaj o poprawną implementację takich sytuacji.
>
> Skoncentruj się na graficznej prezentacji gry.
> Pomiń takie rzeczy jak obliczanie punktacji
> i gromadzenie statystyk dotyczących wyników.

Akcje na klawiaturze:
- strzałki w prawo i lewo — poruszanie się postacią (różowy kwadrat),
- spacja — wystrzelenie pocisku.

[»Strona«](dist/ex-3/index.html)

---
