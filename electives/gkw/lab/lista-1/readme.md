---
lang: 'pl'
title: 'Lista 1.'
subtitle: 'Grafika komputerowa i wizualizacje, Laboratorium'
author: 'Jerzy Wroczyński'
---

- [Informacje techniczne](#informacje-techniczne)
- [Zadania 1. 2. 3.](#zadania-1-2-3)
    - [Rozwiązanie](#rozwiązanie)
    - [Gramatyka zmodyfikowanej wersji języka Logo](#gramatyka-zmodyfikowanej-wersji-języka-logo)
    - [Zadanie 1. — Grafika żółwia](#zadanie-1--grafika-żółwia)
    - [Zadanie 2. — Fraktale](#zadanie-2--fraktale)
    - [Zadanie 3. — Fraktale w SVG](#zadanie-3--fraktale-w-svg)
- [Zadanie 4. — Gra 3d z grafiką wire-frame](#zadanie-4--gra-3d-z-grafiką-wire-frame)
- [Zadanie 5. — Trójwymiarowa grafika żółwia 3d z grafiką wire-frame](#zadanie-5--trójwymiarowa-grafika-żółwia-3d-z-grafiką-wire-frame)

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

## Zadania 1. 2. 3.

### Rozwiązanie

Kolektywne rozwiązanie wszystkich poniższych zadań znajduje się na [jednej stronie](dist/ex-1-2-3/index.html).

Wyjaśnienia gdzie na stronie znajdują się rozwiązania poszczególnych zadań, mieszczą się w sekcjach:
- [Zadanie 1.](#zadanie-1--grafika-żółwia),
- [Zadanie 2.](#zadanie-2--fraktale),
- oraz [Zadanie 3.](#zadanie-3--fraktale-w-svg).

### Gramatyka zmodyfikowanej wersji języka Logo

| Polecenie                    | Opis polecenia                                                                                  |
| ---------------------------- | ----------------------------------------------------------------------------------------------- |
| `F`                          | Pójdź naprzód.                                                                                  |
| `B`                          | Pójdź wstecz.                                                                                   |
| `R`                          | Obróć się w prawo.                                                                              |
| `L`                          | Obróć się w lewo.                                                                               |
| `RE x`                       | Powtórz `x` razy następny blok zamknięty w `[]`.                                                |
| `BE name x arg1 arg2 … argx` | Zdefiniuj procedurę o nazwie `name`, która przyjmuje `x` argumentów.                            |
| `EN`                         | Zakończ definicję procedury.                                                                    |
| `TE`                         | Zakończ działanie programu/procedury.                                                           |
| `IF`                         | Sprawdź, czy warunek został spełniony. Jeśli tak, wykonaj sekwencję poleceń zamkniętych w `[]`. |
| `CA`                         | Oblicz proste binarne wyrażenie matematyczne.                                                   |

Przykłady zastosowań można zobaczyć przy pomocy przycisków z przykładami znajdującymi się na [stronie](dist/ex-1-2-3/index.html).

---

### Zadanie 1. — Grafika żółwia

> Zaimplementować [procedury grafiki żółwia](https://pl.wikipedia.org/wiki/Logo_(j%C4%99zyk_programowania)) na elemencie `<canvas>`.
>
> Parametry żółwia, takie jak położenie i orientacja na płaszczyźnie mają być pamiętane jako liczby rzeczywiste.
> Przyjmij, że okno graficzne reprezentuje prostokąt `[minX, maxX] × [minY, maxY]` i widoczne są jedynie fragmenty śladów pozostawione w tym prostokącie.
>
> Parametry `minX`, `maxX`, `minY`, `maxY` są zapisywane jako pewne parametry niezależne od rozmiaru okna w pikselach.
> Przeliczaj współrzędne rzeczywiste na współrzędne pikseli tak, aby współrzędna X rosła w prawo a współrzędna Y rosła w górę.
>
> Zaimplementuj jeden program wykonujący kilka rysunków demonstracyjnych (np. wielokąty foremne w różnych kolorach) z wykorzystaniem swoich procedur oraz drugi program na innej stronie HTML, zawierającej okienko tekstowe, w którym użytkownik może wpisywać interaktywnie polecenia dla żółwia na ekranie.
> (Dla ułatwienia stosować skrócone nazwy poleceń, np. `lt` zamiast `left`.)

Na [stronie](dist/ex-1-2-3/index.html) znajduje się pole na polecenia. Żeby wykonać zadaną sekwencję poleceń, należy wcisnąć przycisk `Execute`.

[Strona](dist/ex-1-2-3/index.html) zawiera przyciski `Load Example X.`.
Każdy z nich ładuje do pola na polecenia jedną z przykładowych procedur.

Niniejsze pole na polecenie może być modyfikowane przez użytkownika.

---

### Zadanie 2. — Fraktale

> Wykorzystując grafikę żółwia z rozwiązania poprzedniego zadania napisz program rysujący na ekranie trójkąt Sierpińskiego i płatek Kocha dowolnego stopnia.
> Zrób to tak, aby użytkownik mógł zmieniać stopień rysowanej krzywej.

Na [stronie](dist/ex-1-2-3/index.html) znajdują się przyciski `Load Koch` oraz `Load Sierpiński`.

Po załadowaniu tych procedur można zmienić ich stopień w polu na polecenia.
Po zmianie należy wcisnąć przycisk `Clear`, a następnie `Execute` celem narysowania wersji o innym stopniu.

*Uwaga: obrazki o wysokich stopniach mogą być długo przetwarzane.*
*Zalecane jest utrzymanie stopnia w zakresie `1-8`.*

*Uwaga: obrazki o wysokich stopniach wymagają dłuższych odcinków.*
*Język JavaScript ma ograniczoną liczbę miejsc po przecinku dla liczb rzeczywistych.*

---

### Zadanie 3. — Fraktale w SVG

> Wykorzystaj SVG do rysowania krzywych z [poprzedniego zadania](#zadanie-2--fraktale) różnego stopnia.

Na [stronie](dist/ex-1-2-3/index.html) znajduje się przycisk `Switch canvas mode`.
Pozwala on na zmianę sposobu rysowania.

Do wyboru są dwa tryby rysowania:
- `CANVAS` — obrazki są rysowane na elemencie `<canvas>`,
- `SVG` — obrazki są rysowane na elemencie `<svg>`.

---

## Zadanie 4. — Gra 3d z grafiką wire-frame

> Zaimplementować prostą grę, w której należy przeprowadzić gracza z jednego punktu w przestrzeni do innego, omijając losowo rozmieszczone prostopadłościany.
> Aby uniknąć problemów z widocznością i zasłanianiem, zastosuj grafikę wire-frame i przyjmij, że wszystkie linie są tego samego koloru.

Rozwiązanie znajduje się na [stronie](dist/ex-4/index.html).

Gra polega na przejściu postacią oznaczoną różowym kółkiem do prostopadłościanu o takim samym kolorze.

---

## Zadanie 5. — Trójwymiarowa grafika żółwia 3d z grafiką wire-frame

> Zaimplementować grafikę żółwia w trzech wymiarach.
>
> Oprócz skręcania w lewo i w prawo żółw może skręcać w górę i w dół.
> Okno ma postać prostopadłościanu, w którym widać fragmenty śladów pozostawionych przez żółwia,
> które mieszczą się w oknie.
> Użytkownik widzi całe okno wraz ze śladami żółwia i może je obracać tak, aby widzieć je z różnych pozycji.

*Uwaga: zadanie niedokończone.*

W celu obrócenia widoku należy użyć strzałek na klawiaturze.

---
