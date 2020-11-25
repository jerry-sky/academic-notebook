# Lista-3

*(Termin oddania: 2020-11-29)*

- [Zadanie 1.](#zadanie-1)
    - [Nagrania `asciinema`](#nagrania-asciinema)
    - [Polecenia, które należy wykonać w celu realizacji zadania](#polecenia-które-należy-wykonać-w-celu-realizacji-zadania)
- [Skrypt pomocniczy do zadań 2. i 3.](#skrypt-pomocniczy-do-zadań-2-i-3)
- [Zadanie 2.](#zadanie-2)
- [Zadanie 3.](#zadanie-3)

---

Wszystkie zadania są reprezentowane przez pliki `ex-*.cast`, które są nagraniami wykonanymi przy pomocy programu `asciinema`.

Zapisy te mogą zostać odtworzone przy pomocy komendy
```bash
asciinema play <recording>.cast
```
przy zainstalowanym programie `asciinema` w systemie.

---

## Zadanie 1.

> Studenci zostali podzieleni na cztery grupy ze względu na dwie ostatnie cyfry numeru indeksu i uzyskali dostęp do odpowiednich repozytoriów.
>
> Każda grupa ma wspólnie pracować nad stworzeniem aplikacji `app_1` w swoim repozytorium. W ramach każdej grupy każdy student ma dorobić swój własny moduł dodający jakąś funkcjonalność, wykonując następujące czynności:
> - utworzyć swoją kopię roboczą projektu,
> - przejrzeć plik README i pozostałe pliki, aby zorientować się w zasadach organizacji projektu i nazywania plików i katalogów,
> - utworzyć własne rozgałęzienie w `app1/branches` , w którym zaimplementuje swój własny podprogram,
> - zsynchronizować swoją gałąź z `trunk`-iem (być może kilka razy)
> - zreintegrować swoją gałąź z `trunk`-iem
> - usunąć niepotrzebną gałąź po reintegracji
> - utworzyć `tag`-a z poprawną wersją projektu zawierającą własny podprogram.
> - w prezentacji pokazać, że program z utworzonego `tag`-a kompiluje się i wykonuje poprawnie.
>
> Wykonując polecenia należy je nagrywać z terminala wraz z wyświetlanymi komunikatami do sprawozdań `asciinema`.
>
> Można utworzyć więcej niż jedno nagranie, ale ich nazwy powinny zawierać numery wskazujące, w jakiej kolejności należy je wyświetlać. Ostatnie nagranie zakończyć wyświetleniem `svn log -v …` dla utworzonego przez siebie `tag`-a. Utworzone prezentacje można skleić w jedną, nagrywając wykonanie skryptu, który odtwarza je w kolejności. Przykład można obejrzeć, wykonując polecenie:
>
> ```bash
> svn cat https://repo.cs.pwr.edu.pl/info/asciinema/6_sklejanie_prezentacji.cast | asciinema play -i 0.1 -
> ```
>
> W każdym repozytorium, swoje zadanie wykonał „Sztuczny Student” o numerze indeksu `999`. Nie uzyskał jeszcze zaliczenia bo zapomniał usunąć swoją gałąź i nie przygotował sprawozdania. Pozostałe czynności wykonał poprawnie i można prześledzić jego działania (poleceniami `svn log …`, `svn diff …`).
>
> Uwaga: Zadania 1. nie warto odkładać na ostatnią chwilę, gdyż wtedy jest najwięcej konfliktów.

### Nagrania `asciinema`

Odpowiednie nagrania wykonane przy pomocy programu `asciinema` znajdują się w plikach `ex-1.1.cast` oraz `ex-1.2.cast`.

### Polecenia, które należy wykonać w celu realizacji zadania

0. Wykonujemy
    ```bash
    . ../repo.sh
    ```
    żeby pod zmienną `$RP` znajdował się adres główny do wszystkich repozytoriów z tego kursu.
1. Tworzymy kopię roboczą projektu
    ```bash
    svn co $RP/p_75
    ```
2. Wchodzimy w katalog `app_1/trunk` i odczytujemy plik `README`.
3. W tym pliku będziemy zapisywać opis naszego podprogramu.
4. Rozglądając się dalej widzimy pliki `program.h`, `main.c`, `program_usage.c` oraz podprogramy innych studentów `s*_podprogram.c`.
5. Po rozeznaniu się z projektem tworzymy nową gałąź:
    ```bash
    svn copy $RP/p_75/app_1/trunk $RP/p_75/app_1/branches/250075
    ```
6. Tworzymy nowy plik `s250075_podprogram.c` z nowym programem (a dokładniej funkcją w języku *C*).
7. Odpowiednio modyfikujemy pliki `program.h`, `makefile` oraz `main.c`, żeby nasz program „podpiąć” pod główny program, który uruchamia poszczególne podprogramy.
8. Wykonujemy polecenie
    ```bash
    svn commit -m 'added a new subprogram that prints a given real number in its scientific notation'
    ```
    żeby zapisać nasze zmiany w aktualnej gałęzi.
9. Odpowiednio aktualizujemy plik `README` dodając opis naszego podprogramu i też `commit`ujemy zmiany.
10. Przechodzimy do katalogu `^/app_1/trunk`.
11. Przy pomocy komendy
    ```bash
    svn merge ^/app_1/branches/250075
    ```
    reintegrujemy zmiany z gałęzi `250075` do `trunk`a.
12. Poleceniem
    ```bash
    svn rm ^/app_1/branches/250075
    ```
    usuwamy niepotrzebną już gałąź.
13. Dodatkowo tworzymy nowego `tag`a dla naszego stanu całego programu:
    ```bash
    svn copy ^/app_1/trunk ^/app_1/tags/v_250075
    ```
14. Nagranie `ex-1.cast` pokazuje, że wersja programu dostępna w katalogu `^/app_1/tags/v_250075` kompiluje się i działa jak należy.

---

## Skrypt pomocniczy do zadań 2. i 3.

Do zadań 2. i 3. używamy tutaj skryptu pomocniczego `svn-ls-all.sh`, który jest niedalekim kuzynem skryptu z rozwiązania zadania 1. z listy 1. Wypisuje on wszystkie pliki w danym pod-katalogu danego repozytorium dla danej rewizji.

## Zadanie 2.

Napisz skrypt, który jako argument otrzymuje:

Nr rewizji w repozytorium SVN
URL do katalogu w repozytorium SVN (korzenia poddrzewa katalogów, zawierającego pliki tekstowe),
który dla wszystkich słów występujących w plikach w danym poddrzewie katalogów w danej rewizji, drukuje statystyki, ile razy dane słowo wystąpiło we wszystkich tych plikach. (Odpowiednik [zadania 2 z listy 1.](../lista-1/readme.md#zadanie-2))
Niech skrypt będzie w pliku: `./l3z2.bash`. W prezentacji umieść wykonania poleceń:
```bash
./l3z2.bash 15 https://repo.cs.pwr.edu.pl/info/SP-20-21/l3/a/
./l3z2.bash 18 https://repo.cs.pwr.edu.pl/info/SP-20-21/l3/a/
```

Plik wykonywalny [`l3z2.bash`](l3z2.bash) jest rozwiązaniem tego zadania. Jego działanie można zobaczyć na nagraniu `ex-2.cast`.

---

## Zadanie 3.

Skrypt, wywoływany jak w zadaniu 2, który dla każdego słowa pojawiającego się w plikach danego poddrzewa katalogów w danej rewizji, drukuje liczbę plików, w których to słowo występuje.
(Odpowiednik zadania 3 z listy 1.)
Niech skrypt będzie w pliku: `./l3z3.bash`. W prezentacji umieść wykonania poleceń:
```bash
./l3z3.bash 15 https://repo.cs.pwr.edu.pl/info/SP-20-21/l3/a/
./l3z3.bash 18 https://repo.cs.pwr.edu.pl/info/SP-20-21/l3/a/
```

Plik wykonywalny [`l3z3.bash`](l3z3.bash) jest rozwiązaniem tego zadania. Jego działanie można zobaczyć na nagraniu `ex-3.cast`.

---
