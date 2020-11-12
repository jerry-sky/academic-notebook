# Lista-2

*(Termin oddania: 2020-11-11)*

- [Zadanie 1.](#zadanie-1)
- [Zadanie 2.](#zadanie-2)
- [Zadanie 3.](#zadanie-3)
- [Zadanie 4.](#zadanie-4)
- [Zadanie 5.](#zadanie-5)
- [Zadanie 6.](#zadanie-6)

---

Wszystkie zadania znajdują się w plikach `ex-*.cast`, które są nagraniami wykonanymi przy pomocy programu `asciinema`.

Zapisy te mogą zostać odtworzone przy pomocy komendy
```bash
asciinema play recording.cast
```
przy zainstalowanym programie `asciinema` w systemie.

---

## Zadanie 1.

> Utworzyć dwie kopie robocze własnego repozytorium. Na przykładowym pliku tekstowym doprowadzić do konfliktu, a następnie ręcznie rozwiązać konflikt.\
W sprawozdaniu przedstawić, oprócz wykonywanych poleceń, zawartości plików ze znacznikami konfliktu.

Zapis w pliku `ex-1.cast`.

---

## Zadanie 2.

> Utworzyć we własnym repozytorium poddrzewa katalogów (wykorzystać dane z [listy 1.](../lista-1/readme.md)), a następnie utworzyć kopie robocze, w których zostanie zademonstrowane wykorzystanie „sparse directories” do sprowadzenia różnych wybranych fragmentów podkatalogów.
Do wyświetlania drzew katalogów do sprawozdania użyć polecenia `tree`.

Zapis w pliku `ex-2.cast`.

---

## Zadanie 3.

> Sprawdzić i zademonstrować jaki ma wpływ ustawienie i skasowanie własności   `svn:executable` na skryptach. (Mogą być to skrypty z [poprzedniej listy zadań](../lista-1/readme.md).)

Zapis w pliku `ex-3.cast`.

---

## Zadanie 4.

> Utworzyć we własnym repozytorium podkatalog (np. o nazwie `externals`) i ustawić na nim własność (property) `svn:externals`, tak aby w odpowiednim podkatalogu znalazła się kopia robocza repozytorium zewnętrznego:
> ```
> https://repo.cs.pwr.edu.pl/info/
> ```
> Sprawdzić na dodatkowych kopiach roboczych jak działają `svn up`, `svn co` bez opcji `--ignore-externals` oraz z tą opcją.

Zapis w pliku `ex-4.cast`.

---

## Zadanie 5.

> Przetestować zakładanie, usuwanie, zrywanie i podkradanie blokady plików (`svn lock` i związane z nim polecenia).

Zapis w pliku `ex-5.cast`.

---

## Zadanie 6.

> W następujących po sobie kolejnych «commitach»:
> - dodać dwa pliki o różnych zawartościach: `a.txt` i `b.txt` (`svn add ...`)
> - usunąć `b.txt` (`svn delete ...`)
> - dopisać wiersz tekstu do `a.txt` i przenieść `a.txt` do `b.txt` (`svn move ...`)
> - dopisać wiersz tekstu do `b.txt` i przenieść `b.txt` do `c.txt` (`svn move ...`)
> - dodać nowy plik `b.txt` (`svn add ...`)
>
> Wyświetlić historię każdego obiektu i historię całego podkatalogu (`svn log -v ...`). Wykorzystując „peg-revision” i „operative revision” wyświetl zawartości pliku `c.txt` i wszystkich jego wcześniejszych wersji.

Zapis w pliku `ex-6.cast`.

---
