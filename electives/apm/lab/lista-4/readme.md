---
lang: 'pl'
title: 'Lista 4.'
subtitle: 'Aplikacje mobilne, Laboratorium'
author: 'Jerry Sky'
---

- [Zadanie 1.](#zadanie-1)
- [Zadanie 2.](#zadanie-2)
- [Zadanie 3.](#zadanie-3)

---

## Zadanie 1.

> Napisz aplikację (galeria) przechowującą zdjęcia np. ludzi, krajobrazów, zwierząt, ... i każde zdjęcie dodatkowo zawiera krótki opis.
> Po uruchomieniu aplikacji, na początku pokazuje ona dostępne zdjęcia.
> Użytkownik może wybrać dowolną pozycję, aby zobaczyć większe zdjęcie i opis.
> Na ekranie dodatkowo, mamy możliwość ocenienia zdjęcia przez
> np. "gwiazdki" (zobacz [`RatingBar`](http://developer.android.com/reference/kotlin/android/widget/RatingBar.html)).
>
> Proszę pamiętać, że na tym etapie poznania Androida nie ma to być w pełni funkcjonalna aplikacja
> np. nie potrzeba tworzyć kont dla użytkowników lub nie potrzeba przechowywać nowych zdjęć.
>
> Aplikacja powinna natomiast obsługiwać:
> - co najmniej dwie aktywności,
> - przekazywać informacje z jednej aktywności do drugiej wykorzystując intencje
>     (tutaj proszę przemyśleć jak to zrobić, dane wysyłane w intencji mają ograniczony rozmiar),
> - druga aktywność powinna wracać informacje do pierwszej o liczbie gwiazdek,
>     po czym w pierwszej aktywności obrazki zostają odpowiednio posortowane po liczbie gwiazdek,
> - poprawnie obsługiwać cykl życia aktywności
>     tzn. `onCreate`, `onStart`, `onResume`, `onPause`, `onStop`, `onDestroy`, ...
>     (te, które są potrzebne),
> - wykorzystywać fragmenty przy zmianie orientacji ekranu,
> - zapamiętywać swój stan po zmianie orientacji ekranu.

Pliki projektu znajdują się w katalogu `Tousvoir`.

---

## Zadanie 2.

> Zmień powyższą aplikację na [*„tab layout”*](https://developer.android.com/guide/navigation/navigation-swipe-view-2)
> (`ViewPager2`) zamiast dwóch aktywności.

---

## Zadanie 3.

> Uzupełnij poprzednie zadanie o możliwość robienia zdjęć
> (obsługa [CameraX](https://developer.android.com/training/camerax))
> i dodawania do kolekcji.

---
