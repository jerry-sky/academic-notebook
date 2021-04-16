---
lang: 'pl'
title: 'Lista 3.'
subtitle: 'Aplikacje mobilne'
author: 'Jerry Sky'
---

- [Zadanie 1.](#zadanie-1)
    - [Zarys](#zarys)
- [Zadanie 2.](#zadanie-2)
- [Zadanie 3.](#zadanie-3)
- [Zadanie 4.](#zadanie-4)

---

## Zadanie 1.

> Napisz prostą aplikację „To-Do”,
> czyli listę zadań do zrobienia.
> Aplikacja zawiera `RecyclerView` z potencjalną listą zadań.
> Na początku lista jest pusta, ale na dole aktywności znajduje się `Button` (Dodaj),
> gdzie użytkownik może uruchomić drugą aktywność, aby wprowadzić opis nowego zadania.
>
> Dalej mamy możliwość wyboru ikonki zadania (obrazek) oraz czas i data wykonania zadania.
> Zaprojektuj odpowiedni layout pojedynczej pozycji `RecyclerView`, który zawiera co najmniej obrazek, treść zadania oraz czas i datę wykonania.
>
> Aplikacja powinna też mieć możliwość usuwania zadań z listy, przez dołączenie słuchacza do listy, który usuwa wybraną pozycję.
> Najlepiej wykorzystać do tego *long click* (metoda `setOnItemLongClickListener`) lub *swipe*.
>
> Uwaga: W tym zadaniu aplikacja powinna być w pełni funkcjonalna.
> Uwzględniana będzie też wygoda i użyteczność aplikacji.
>
> Powinna również udostępniać podstawowe funkcje tj.:
> - sortowanie zadań po czasie,
> - ustalenie priorytetów zadań,
> - sortowanie po ikonce (typ zadania),
> - ... (za co można dostać dodatkowe punkty).

Pliki projektu znajdują się w katalogu `ex-1-2-4/Devoir`.

---

## Zadanie 2.

> Zrób też tak, aby aplikacja pamiętała listę zadań po rotacji ekranu, czyli po zmianie z *portrait* na *landscape* i odwrotnie.
> Tutaj należy wykorzystać tylko [`onSaveInstanceState`](https://developer.android.com/guide/components/activities/activity-lifecycle) i [`onRestoreInstanceState`](https://developer.android.com/guide/components/activities/activity-lifecycle).

Pliki projektu znajdują się w katalogu `ex-1-2-4/Devoir`.

---

## Zadanie 3.

> Wykorzystaj lokalną bazę danych do przechowywania danych aplikacji „To-Do” przez użycie [Room-a](https://developer.android.com/training/data-storage/room),
> czyli warstwę abstrakcji na *SQLite*.

---

## Zadanie 4.

> Zrób w aplikacji „To-Do” [powiadomienie](https://developer.android.com/guide/topics/ui/notifiers/notifications) użytkownika,
> że zbliża się termin wykonania zadania.

Pliki projektu znajdują się w katalogu `ex-1-2-4/Devoir`.

---
