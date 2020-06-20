# Lista-4

> ## Zasady
> Celem listy jest praktyczne zapoznanie z NoSQL, na rozwiązanie zadań składać się powinny przygotowane wcześniej komendy, których działanie zostanie zaprezentowane na laboratorium. Zadania można rozwiązywać korzystając wyłącznie z konsoli Mongo lub po połączeniu się z bazą Mongo za pomocą wybranego języka programowania.\
> Po uzgodnieniu z prowadzącym laboratorium listę można wykonać z wykorzystaniem innego systemu nierelacyjnych baz danych – efekt wykonywania odpowiednich poleceń powinien pozostać bez zmian. W celu uzyskania oceny 5.0 z listy wykonaj 4 pierwsze zadania oraz 5 wybranych z pozostałych.
>
> ## Zadania
> 1. Zainstaluj MongoDB. Utwórz bazę danych `MDBHobby`. W skład bazy danych powinny wchodzić 3 kolekcje: `zwierzęta`, `sport`, `osoby`. **Uwaga**: dane do uzupełnienia bazy mogą być generowano losowo, częściowo wyeksportowane z rozwiązań list poprzednich lub pobrane (np. w formacie JSON) z gotowego źródła. W przypadku braku dokumentu w bazie spełniającego kryterium któregoś z zadań, dodaj odpowiednie dokumenty i powtórz zadanie.
> 2. Dodaj przynajmniej 10 sportów. Każdy dokument powinien zawierać przynajmniej informacje o nazwie, miejscu wykonywania (hala, na zewnątrz) oraz tego czy jest sportem indywidualny czy zespołowym – 2 ostatnie atrybuty mogą mieć więcej niż jedną wartość dla wybranych sportów. Dla wybranych sportów dodaj inne atrybuty.
> 3. Dodaj przynajmniej 10 gatunków zwierząt. Gatunek może, lecz nie musi, dzielić się na różne rasy (uwzględnij w bazie przynajmniej jeden gatunek z rasami). Każdy dokument powinien zawierać informację o minimalnej i maksymalnej wadze, dopuszczalnej gamie ubarwienia oraz oczekiwanej długości życia.
> 4. Dodaj do bazy danych przynajmniej 50osób, w każdym dokumencie powinno znajdować się przynajmniej imię i nazwisko, dodatkowo w większości dokumentów powinna być informacja o ich wieku, wzroście, zainteresowaniach (każda z osób ma więcej niż jedno zainteresowanie) oraz narodowości. Dla osób posiadających więcej niż jedno obywatelstwo uwzględnij te informacje korzystając z `array`, w przypadku krajów federalnych, jak np. USA, Niemcy, czy Rosja, wykorzystaj `embedded document` w celu podania również kraju związkowego. Korzystając z dokumentów zagnieżdżonych dodaj wszystkim posiadaczom zwierząt informację o gatunku oraz imieniu pupila lub pupili.
> 5. Wyświetl wszystkie kolekcje w `MDBHobby`. Wyświetl wszystkie nie puste kolekcje w `MDBHobby`.
> 6. Utwórz zapytanie wyświetlające wszystkie znajdujące się w bazie koty wraz z ich posiadaczem.
> 7. Wypisz wszystkie osoby o imieniu *Jan* i obywatelstwie *polskim* lub posiadające więcej niż 1 obywatelstwo. Zadbaj by nie wyświetlało się pole z identyfikatorem dokumentu.
> 8. Wypisz sporty, którymi interesuje się przynajmniej 5 osób.
> 9. Pamiętając, iż MongoDB nie udostępnia bezpośrednio funkcjonalności odpowiadającej `JOIN`om, dla każdej osoby o nazwisku *Nowak* wypisz hobby. W wyniku wypisz imię, nazwisko i narodowość oraz nazwę i typ (indwydidualny lub zespołowy) sportu. Zadbaj by nie przypisać hobby niewłaściwej osobie o tym samym nazwisku.
> 10. Usuń z bazy wszystkie osoby, które w hobby mają parę `['koszykówka', 'hokej']`.
> 11. Dla wszystkich osób, które mają w hobby zarówno strzelectwo jak i narciarstwo, zamień je na biatlon.
> 12. Wszystkim osobom z *Rosji* usuń informację o kraju związkowym (zastąp ją tylko informacją o rosyjskim obywatelstwie).
> 13. Wyświetl imiona i nazwiska oraz narodowość wszystkich miłośników psów, wyniki uporządkuj rosnąco względem wieku.
> 14. Wyświetl osoby, których imiona i nazwiska nie zawierają liter v, x, q, ł, ą, z pominięciem tych, którzy mają obywatelstwo polskie. Możesz wykorzystać wyrażenia regularne.

## Rozwiązania i uruchomienie programów

Pliki `ex-*.ts` zawierają implementację zadanych programów.

Uruchomienie powyższych programów działa na takiej samej zasadzie jak na [liście zerowej](../lista-0/readme.md#uruchomienie-programów).
