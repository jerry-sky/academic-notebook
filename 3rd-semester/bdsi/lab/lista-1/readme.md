---
lang: 'pl'
title: 'Lista-1'
author: 'Jerry Sky'
---

---

> Ściągnij [bazę danych `menagerie database`](https://dev.mysql.com/doc/index-other.html), a następnie utwórz i wypełnij bazę danych zgodnie z instrukcjami w pliku `README`. Wykonaj poniższe polecenia, zapisz potrzebne kwerendy SQL.
>
> 1. Wypisz wszystkie znajdujące się w bazie tabele.
> 2. Dla każdego właściciela wypisz jedynie jego imię oraz imię jego pupila.
> 3. Wypisz daty urodzenia wszystkich psów.
> 4. Wypisz imiona psów urodzonych w pierwszej połowie roku oraz imiona ich właścicieli.
> 5. Wypisz gatunki zwierząt, w których w bazie wystąpiły samce.
> 6. Wypisz imiona zwierząt oraz datę wydarzenia, kiedy zwierzę otrzymało jakiś prezent.
> 7. Wypisz imiona właścicieli, którzy posiadają zwierzę z imieniem kończącym się sufiksem -ffy.
> 8. Analogicznie jak w pkt. 2, dla każdego właściciela wypisz jedynie jego imię oraz imię jego pupila, jednak uwzględnij tylko właścicieli z żyjącymi zwierzętami.
> 9. Wypisz właścicieli, którzy posiadają więcej niż jedno zwierze.
> 10. Wypisz imiona właścicieli oraz imiona ich psów poza tymi, które obchodziły urodziny. Wynik posortuj malejąco względem imienia psa.
> 11. Wypisz zwierzęta urodzone między rokiem 1992 a czerwcem 1994.
> 12. Wypisz 2 najstarsze żyjące zwierzęta.
> 13. Wypisz najmłodsze żyjące zwierzę, w sposób który nie będzie wymagał sortowania danych.
> 14. Wypisz imiona właścicieli posiadających zwierzę, dla którego wystąpiło wydarzenie później niż wizyta u weterynarza `Slima`.
> 15. Wypisz imiona właścicieli, którzy nie posiadają zwierzęcia obchodzącego urodziny. Wyniki posortuj rosnąco względem daty urodzenia zwierzęcia.
> 16. Wypisz pary imion właścicieli, którzy posiadają ten sam gatunek zwierzęcia. (Uwaga: Jeśli występuje para $(X, Y)$, to wynik nie powinien zawierać pary $(Y, X)$).
> 17. Do tabeli `event` dodaj, po dacie, kolumnę performer, wskazującą na osobę przeprowadzającą zdarzenie.
> 18. Dla wszystkich zdarzeń uzupełnij kolumnę `performer` – wszystkie zdarzenia o typach innych niż `vet` oraz `litter` przeprowadzają obecni właściciele, dla wymienionych dwóch typów tabelę uzupełnij przynajmniej 2 różnymi nazwiskami weterynarzy.
> 19. Zmień wartości w kolumnie właściciel dla wszystkich kotów na wartość `Diane`.
> 20. Dla każdego gatunku wypisz liczbę zwierząt do niego należącą. Wyniki posortuj malejąco względem liczby.
> 21. Usuń z bazy danych informacje o nieżyjących zwierzętach.
> 22. Z tabeli `pet` usuń kolumnę `death`.
> 23. Do bazy danych dodaj informacje o 3 nowych właścicielach, posiadających łącznie 2 psy, 1 chomika, 3 kozy i 1 owcę. Dla każdego nowego zwierzaka dodaj przynajmniej jeden wpis w tabeli `event`. Uzupełnij pola tak, by w nowych wpisach nie występowały wartości `NULL`.
>
> **Uwaga:** Wyniki powinny zawierać tylko wymienione kolumny. Jeśli nie jest zaznaczone inaczej, wyniki nie powinny zawierać powtarzających się krotek.

Zadane kwerendy zawierają się w plikach `ex-*.sql`.
