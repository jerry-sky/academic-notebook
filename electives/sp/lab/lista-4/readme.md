---
lang: 'pl'
title: 'Lista-4'
author: 'Jerry Sky'
date: '2020-12-09'
---

---

- [Zadanie 1.](#zadanie-1)
- [Zadanie 2.](#zadanie-2)

---

Wszystkie zadania są reprezentowane przez pliki `ex-*.cast`, które są nagraniami wykonanymi przy pomocy programu `asciinema`.

Zapisy te mogą zostać odtworzone przy pomocy komendy
```bash
asciinema play <recording>.cast
```
przy zainstalowanym programie `asciinema` w systemie.

---

## Zadanie 1.

> Każdy student (który dostarczył poprawny klucz publiczny)
> ma dostęp do repozytoriów GIT na serwerze: `156.17.7.16` przez system
> [*Gitolite*](http://gitolite.com/gitolite/index.html).
>
> Podobnie jak w [zadaniu 1. listy 3.](../lista-3/readme.md#zadanie-1), studenci są podzieleni na grupy ze względu na dwie ostatnie cyfry numeru indeksu i mają dostęp do jednej z piaskownic:
> ```
> git@156.17.7.16:sandbox-20-21_00
> git@156.17.7.16:sandbox-20-21_25
> git@156.17.7.16:sandbox-20-21_50
> git@156.17.7.16:sandbox-20-21_75
> ```
>
> Repozytorium można sobie sklonować jak w poniższym przykładzie:
>
> ```bash
> $ git clone git@156.17.7.16:sandbox-20-21_00
> ```
>
> Należy wykonać w GIT zadanie analogiczne do zadania 1 z listy 3, wykorzystując mechanizmy tworzenia rozgałęzień i etykietowania (branching, tagging) typowe dla GITa.
>
> Podobnie jak poprzednio, student `999` wykonał już swoje zadanie.
> Należy uważnie prześledzić historię:
> ```bash
> $ git log --all --graph --decorate
> ```
> oraz przejrzeć utworzonego tag-a:
> ```bash
> $ git show s999
> ```
> Następnie wykonać analogiczne czynności na tej piaskownicy.
> (Nie zapomnieć o wypchnięciu na serwer również swoich tag-ów: `git push --tags`).
>
> Sprawozdanie `asciinema` z wykonanych czynności należy wrzucić do swojego repozytorium SVN. Powinno ono zawierać na końcu:
> - sklonowanie z serwera piaskownicy (zawierającej już własne rozwiązanie) do nowego katalogu,
> - `checkout` własnego tag-a,
> - `git show <własny tag>`,
> sprawdzenie: kompilacja `make` i uruchomienie programu,
> - `git log --all --graph --decorate`


Odpowiednie nagranie wykonane przy pomocy programu `asciinema` znajduje się w pliku `ex-1.cast`.

## Zadanie 2.

> Napisz skrypt, który dla danych dwóch numerów rewizji $r_1$ i  $r_2$, gdzie $r_1 \le r_2$, oraz adresu URL katalogu w repozytorium SVN (istniejącego w rewizjach od $r_1$ do $r_2$), generuje repozytorium GIT, które zawiera zawiera jedną gałąź master jako ciąg commit-ów  odpowiadających tym rewizjom z repozytorium SVN, które zmieniały dany katalog.
> Każdy commit w repozytorium GIT ma zawierać taki sam stan katalogu i „commit message” jak stan katalogu i „log message” odpowiedniej rewizji z repozytorium SVN.
> (Daty i autor nie muszą być kopiowane.).
>
> Zakładamy, że wersjonowaniu nie podlegają pliki ani katalogi o nazwach:
> ```
> .git
> .svn
> .gitignore
> ```
>
> Przyjmijmy, że skrypt ma nazwę `l4z2.bash`. W sprawozdaniu `asciinema`  zademonstruj działanie wywołania skryptu:
> ```bash
> l4z2.bash 15 21 https://repo.cs.pwr.edu.pl/info/SP-20-21/l3/
> ```
>
> W bieżącym katalogu powinno zostać utworzone repozytorium GIT o nazwie `l3` zawierające odpowiednie commit-y.  Sprawozdanie na końcu ma zawierać wyświetlenie w tym repozytorium polecenia:
> ```bash
> git log --stat
> ```
> oraz:
> ```bash
> git log --stat | grep -v '^commit ' | grep -v '^Author: ' | grep -v '^Date: '
> ```


Plik wykonywalny [`l4z2.bash`](l4z2.bash) jest rozwiązaniem tego zadania. Jego działanie można zobaczyć na nagraniu `ex-2.cast`.

---
