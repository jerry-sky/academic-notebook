# Lista 1

## Droga do Japonii *(Amazon)*

### `traceroute amazon.jp`
  Po uruchomieniu
  ```bash
  traceroute --back amazon.jp
  ```
  ze standardowymi ustawieniami *(60 bajtów)*
  przechodzimy przez wiele serwerów, również tych, które nawet po trzech próbach nie odpowiadają. Jednakże, dochodzimy do jakiegoś serwera Cloudfront'a który jest ostatnim na liście drogi do `amazon.jp`.

  #### Przypadek pierwszy
  Dzieli go od komputera podłączonego do routera we **Wrocławiu 28 hopów oraz 25 hopów w drugą stronę**.

  #### Przypadek drugi
  Przy zmniejszeniu **liczby bajtów do tylko 28** (28 bajtów mają nagłówki - minimum) liczba hopów zmniejsza się do **tylko 19 hopów oraz 16 z powrotem**, bo trafiamy na serwer Cloudfront'a o nieco innej subdomenie zarządzającej innym adresem IP.

  #### Różne liczby bajtów
  - *Nietypowe zachowanie*: po zmianie liczby bajtów na **wartość różną od 60** zazwyczaj natrafiało się na [**przypadek drugi**](#przypadek-drugi) (19 hopów i 16 z powrotem), chociaż z rzadka również pojawiał się [przypadek pierwszy](#przypadek-pierwszy) (28 hopów i 25 z powrotem).
  - Po wysłaniu 1500 bajtów (max bajtów bez procesu defragmentacji) wracamy do [przypadku pierwszego](#przypadek-pierwszy).
  - Po przekroczeniu 1500 bajtów (chociażby 1501 bajtów) `traceroute` nie potrafi ukończyć drogi, wypisuje wiele linijek zawierających `* * *` co oznacza trzy nieudane próby połączenia się z serwerem na drodze do `amazon.jp`. Po dodaniu flagi `-F` *(don't fragment)* nie jesteśmy w stanie przejść dalej niż jeden hop.

### `ping amazon.jp`
  Po uruchomieniu
  ```bash
  ping -t <TTL> amazon.jp
  ```
  gdzie `TTL` jest większe bądź równe 28 dostajemy odpowiedź - taki sam wynik jak przy programie [`ping`](#ping-amazonjp). Pakiet odpowiedzi ma `TTL` równe 232, czyli hopów od serwera do komputera we Wrocławiu było `255-226 = 29`

  - Po dodaniu flagi `-M do` nie możemy wyjść dalej niż jeden hop.
  - Po dodaniu flagi `-M want` nie fragmentujemy lokalnie i jesteśmy w stanie wysłać maksymalną liczbę bajtów, na którą pozwala `ping` jaką jest 65507 bajtów.

## Droga do Chin *(Amazon)*

### `traceroute amazon.cn`
  Po uruchomieniu
  ```bash
  traceroute --back amazon.cn
  ```
  dochodzimy do 14 hopa *(22 z powrotem)* a dalej nie ma odpowiedzi od serwerów po drodze do `amazon.cn`. Musimy użyć [`ping`a](#ping-amazoncn).

### `ping amazon.cn`
  Przy użyciu
  ```bash
  ping -t <TTL> amazon.cn
  ```
  dla wartości większych bądź równych 20 dostajemy odpowiedź - czyli **dzieli nas 20 hopów**. Pakiet odpowiedzi miał `TTL` równy 229 czyli hopów z powrotem było `255 - 229 = 26`.\
  Co ciekawe, zazwyczaj *pierwsze dwa pakiety są tracone*, dopiero trzeci i następne dostają odpowiedź.

## Droga do serwerowni PPT

## `traceroute cs.pwr.edu.pl`
  Po uruchomieniu
  ```bash
  traceroute --back cs.pwr.edu.pl
  ```
  dostajemy wynik 11 hopów oraz 12 z powrotem.

## `ping cs.pwr.edu.pl`
  Po uruchomieniu
  ```bash
  ping -M want -s 34700 cs.pwr.edu.pl
  ```
  dostajemy odpowiedź i jest to najwyższa liczba bajtów jaka mogła zostać wysłana zakładając, że chcemy dostać odpowiedź.

## Opis programów

### `ping`
Program do wysyłania małych paczek, *pakietów* danych do wybranego hosta. Może być użyty do sprawdzenia czy mam połączenie z Internetem, albo czy jesteśmy w stanie połączyć się z kimś innym w sieci.

### `traceroute`
Wypisz poszczególne przystanki, przez które pakiet danych przechodzi kiedy zmierza do danego hosta. Może być użyty do debugowania sieci, lub po prostu do sprawdzenia jak daleko jesteśmy od innego urządzenia w sieci.

### `wireshark`
Program pozwalający na podgląd tego co zostaje wysyłane i przysyłane z danego komputera. Jako, że większość stron internetowych szyfruje połączenia poprzez certyfikaty SSL, widzimy tylko zaszyfrowane dane, które są odczytywane jako ciąg losowych znaków.\
Jedyne co ciekawe to rodzaj danych wysyłanych przez `ping`. Otóż `ping` wysyła sekwencję list znaków ASCII jedna po drugiej do wypełnienia należnego rozmiaru pakietu jaki nadaje parametr `-s <SIZE>`.
