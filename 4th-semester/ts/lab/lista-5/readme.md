# Lista-5

- [Lista-5](#lista-5)
  - [Treść zadania](#treść-zadania)
  - [Oryginalny skrypt `server3.pl`](#oryginalny-skrypt-server3pl)
  - [Prosty serwer `express.js`](#prosty-serwer-expressjs)
  - [Analiza przechwyconych komunikatów](#analiza-przechwyconych-komunikatów)

## Treść zadania

1. Plik [`server3.pl`](server3.pl) zawiera przykładowy program serwera protokołu HTTP.
   1. Uruchom ten skrypt, przetestuj, zastanów się jak działa.
   2. Nawiąż połączenie za pomocą przeglądarki internetowej.
   3. Zmień skrypt (lub napisz własny serwer w dowolnym języku programowania) tak aby wysyłał do klienta nagłówek jego żądania.
   4. Zmień skrypt (lub napisz własny serwer w dowolnym języku programowania) tak aby obsugiwał żądania klienta do prostego tekstowego serwisu WWW (kilka statycznych ston z wzajemnymi odwołaniami) zapisanego w pewnym katalogu dysku lokalnego komputera na którym uruchomiony jest skrypt serwera.
   5. Przechwyć komunikaty do/od serwera za pomocą analizatora sieciowego - przeanalizuj ich konstrukcję.

## Oryginalny skrypt `server3.pl`

Aby uruchomić oryginalny skrypt podstawowego serwera lokalnego HTTP należy wykonać `./server3.pl` upewniwszy się że `perl` jest zainstalowany w systemie.

## Prosty serwer `express.js`

Przed uruchomieniem serwera należy mieć zainstalowane `node` oraz `npm` w systemie.

Żeby zainstalować potrzebne paczki należy wykonać `npm install`.

W celu uruchomienia serwera należy wykonać `node .`, `./index.js` lub `npm run start`.

Po uruchomieniu należy otworzyć [stronę localhost:3000](http://localhost:3000) w przeglądarce.

## Analiza przechwyconych komunikatów

Wszystkie zapytania i odpowiedzi są przechwytywane bez problemu i można odczytać ich zawartość jako, że nie używamy tutaj protokołu SSL.

W prawie wszystkich przypadkach zapytanie o daną podstronę statyczną skutkuje odpowiedzią `304 NOT MODIFIED` co wskazuje na brak zmian w danym pliku `.html`. Oczywiście, jeśli dodamy lub usuniemy część zawartości w danym pliku odpowiedź `200 OK` będzie zawierać nową wersję danego pliku `.html`.\
Warto zaznaczyć, że w przypadku [podstrony localhost:3000/request-headers](http://localhost/request-headers) zawsze mamy do czynienia z zapytaniem wynikającym odpowiedzi `200 OK` jako, że dane zwrotne są generowane na bieżąco, „dynamicznie” w przeciwieństwie do serwowania zwykłego statycznego pliku.
