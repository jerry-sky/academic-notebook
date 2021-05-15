---
lang: 'pl'
title: 'Lista 5.'
subtitle: 'Aplikacje mobilne, Laboratorium'
author: 'Jerry Sky'
---

- [Zadanie 1.](#zadanie-1)
- [Zadanie 2.](#zadanie-2)
    - [Odnośnie kwestii autoryzacji](#odnośnie-kwestii-autoryzacji)

---

## Zadanie 1.

> Napisz prostą dwuwymiarową grę w tenisa Pong lub Arkanoid.
> Wykorzystaj `SurfaceView`, który będzie odpowiedzialny za rysowanie gry.
> Wszystkie informacje o stanie gry mają być przechowywane w bazie SQLite z wykorzystaniem Room-a.

Pliki projektu znajdują się w katalogu `ex-1/Pingouin`.

---

## Zadanie 2.

> Celem tego zadania jest wykorzystanie bazy danych czasu rzeczywistego Firebase.
> Można wykorzystać ją w dowolnej aplikacji, gdzie jest logowanie na konto i komunikacja czasu rzeczywistego przez sieć.
>
> Przykłady:
> - Dopisz funkcjonalność „gry przez sieć” do aplikacji z Listy 2 - kółko i krzyżyk.
>     Wystarczy tutaj klasyczna rozgrywka na planszy 3×3,
>     czyli na początku mamy możliwość rejestracji lub jeśli mamy już konto to logowania.
>     Po czym możemy wybrać osobę do gry (która jest też zalogowana do systemu).
>     Następnie prowadzimy grę na zmianę przez sieć.
> - Program do rozmowy (chat) przez sieć z wykorzystaniem Firebase.
>     Logowanie i rozmowa w czasie rzeczywistym z zalogowanymi użytkownikami.
> - Dopisz możliwość gry przez sieć do zadania 1, czyli np. gry Pong.
>     Logowanie, tabela wyników i oczywiście sama gra prowadzona przez dwie osoby na różnych urządzeniach.
> - \[…\] — można napisać dowolną inną, która zawiera komunikację w czasie rzeczywistym oraz logowanie przez Firebase.

Rozwiązanie zawiera prostą aplikację do rozmów między użytkownikami.
Każdy(a) użytkownik(czka) musi się zalogować przy pomocy adresu e-mail i hasła.

Pliki projektu znajdują się w katalogu `ex-2/Discorde`.

### Odnośnie kwestii autoryzacji

Aktualne rozwiązanie nie jest w pełni bezpieczne pod względem podszywania się pod innych użytkowników.
Aplikacja sama dołącza pole `author` do wysyłanej wiadomości — serwer akceptuje tę wartość bez sprawdzania.

Rozwiązaniem byłoby uruchomienie funkcjonalności *Firebase Functions*,
która pozwalałaby na dodanie funkcji nasłuchującej zmian w bazie danych *Firebase Realtime DB*.
Funkcja ta pobierałaby faktyczną nazwę wyświetlaną użytkownika(czki) wysyłającego(ej) wiadomość,
a następnie nadpisywała tę wartość wysłaną przez aplikację.

W ten sposób zapewniamy, że wiadomość ma faktyczny podpis tego użytkownika(czki) w bazie danych.

Szkic funkcji:

```ts
import * as functions from 'firebase-functions'
import * as admin from 'firebase-admin'
import { Message } from '../model/message'

export const onMessageCreate = functions.database.ref('/path')
    .onCreate(async (snap, context) => {
        // get the message that was created
        const message = snap.val() as Message
        // get the ID of the user that created the message
        const userId = context.auth.uid

        // get the user’s actual display name
        const userData = await admin.auth()
            .getUser(userId)
        const userDisplayName = userData.displayName

        const newMessageValue: Partial<Message> = {
            author: userDisplayName
        }

        // update the author
        return snap.ref.update(newMessageValue)
    })

```

Oczywiście, w pełnoprawnej aplikacji nie zapisywalibyśmy wyświetlanej nazwy użytkownika,
a raczej jego identyfikator (`uid`).
Wówczas serwer mógłby działać w ten sposób, że za każdym razem,
kiedy pojawia się nowe zapytanie o listę wiadomości,
serwer zwraca listę z zamienionymi `uid` na nazwy wyświetlane użytkowników.\
Nie mielibyśmy wtedy oczywistego problemu duplikowania danych i niepotrzebnej redundancji.

---
