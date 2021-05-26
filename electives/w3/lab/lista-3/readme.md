---
lang: 'pl'
title: 'Lista 3.'
subtitle: 'Nowoczesne technologie WWW, Laboratorium'
author: 'Jerry Sky'
---

- [Zadanie 1.](#zadanie-1)
- [Zadanie 2.](#zadanie-2)

---

## Zadanie 1.

> Wygeneruj arkusz styli dla swojego portfolio przy użyciu preprocesora CSS Sass.
>
> - Postaraj się optymalnie wykorzystać jego możliwości (zmienne, funkcje, domieszki, rozszerzenia etc.).
>
> - Stwórz plik wyjściowy skompresowany (ten wykorzystaj w projekcie) oraz jeden w wersji deweloperskiej,
>     który łatwo będzie można przeglądać.
>     Porównaj wielkość plików.

W pliku [`makefile`](makefile) znajdują się odwołania do skryptów do pobierania programu kompilującego
oraz do kompilowania plików Sass.

- Pobieranie programu kompilującego:
    ```bash
    make sass
    ```

- Kompilacja (bez minifikacji plików):
    ```bash
    make
    ```

- Kompilacja (z minifikacją plików):
    ```bash
    make css-compressed
    ```

- Kompilacja (na bieżąco):
    ```bash
    make css-dev
    ```

- Kompilacja (z minifikacją plików do katalogu `minified/css` — do porównania wielkości plików skompresowanych oraz zwykłych):
    ```bash
    make css-compressed-prefix
    ```

---

## Zadanie 2.

> Wykorzystaj język skryptowy PHP do:
>
> - Generowania swojego portfolio zgodnie z zasadą DRY (Don’t Repeat Yourself)
>     — elementy powtarzające się na wszystkich podstronach (menu nawigacyjne, nagłówek, stopkę, etc.)
>     przerzucamy do osobnych plików.
>
> - Wzbogacenia swojego portfolio o:
>     1. Licznik odwiedzin, który będzie wzrastał przy odwiedzeniu (czy odświeżeniu) strony z danego urządzenia.
>         Postaraj się to zrobić tak, żeby licznik nie wzrastał częściej niż raz na dobę dla jednego numeru IP.
>     2. Możliwość komentowania twoich projektów. Zadbaj o dodawanie, usuwanie kont użytkownikom i odpowiednią
>         obsługę sesji (logowanie, wylogowywanie, a wyłącznie dla zalogowanych użytkowników możliwość dodawania
>         komentarzy do prezentowanych treści).
>         Zadbaj również o automatyczne wylogowywanie użytkownika po 5 minutach bezczynności.
>
> **Uwagi**:
>     - Jeżeli wykorzystujesz ciasteczka, zorientuj się w obowiązujących przepisach prawnych, czy jest to konieczne,
>         a jeżeli tak, to w jaki sposób możesz pozyskać zgodę użytkowników na ich stosowanie.

---
