# Lista-3

> 1. Uruchom bazę danych Hobby z listy 2. Utwórz indeksy dla tabel:
>    - dla tabeli `osoba` indeks na kolumnie `imię`,
>    - dla tabeli `osoba` indeks na kolumnie `dataUrodzenia`,
>    - dla tabeli `sport` indeks na grupie kolumn (`id`, `nazwa`),
>    - dla tabeli `inne` indeks na grupie kolumn (`nazwa`, `id`),
>    - dla tabeli `hobby` indeks na grupie kolumn (`osoba`, `id`, `typ`).
>
>    Wskaż które indeksy istniały wcześniej. Wskaż te, do których istniał wcześniej podobny indeks. Uzasadnij wybór typu indeksu dla każdego z podpunktów.
>
> 2. Utwórz zapytania zgodne z poniższą specyfikacją. Sprawdź, w których przypadkach zostaną wykorzystane indeksy. Czy wybór typu indeksu miał wpływ na wykorzystanie indeksu?
>    - Znajdź płeć wszystkich osób o imieniu rozpoczynającym się od 'A'.
>    - Wypisz posortowaną listę nazw sportów drużynowych.
>    - Wypisz pary (id) sportów indywidualnych, które uprawiane są w tej samej lokacji.
>    - Znajdź wszystkie osoby urodzone przed 2000-01-01.
>    - Znajdź nazwę najpopularniejszego hobby.
>    - Wypisz imię najstarszego posiadacza psa.
>
> 3. Utwórz tablę `zawody` o kolumnach `id`, `nazwa`, `pensja min`, `pensja max` oraz tabelę `praca` zawierającą informację o id zawodu, id osoby oraz jej zarobkach.\
> Korzystając z pętli uzupełnij tabelę `zawody` przynajmniej 10 różnymi zawodami (zadbaj o poprawne widełki płacowe), a następnie, z wykorzystaniem kursora na tabeli `osoba`, przypisz każdej osobie zawód (wraz z odpowiednią pensją) i uzupełnij tabelę `praca`.
>
> 4. Napisz procedurę, która przyjmując dwa parametry wejściowe: `agg` oraz `kol` wypisuje wynik o schemacie (`kol`, `agg`, $X$), gdzie $X$ jest wynikiem zastosowania funkcji agregującej `agg` na kolumnie `kol` w tabeli `osoba` lub zwróci informację o błędzie. Możliwe wykorzystanie:
>    - funkcja `COUNT` na kolumnie imię lub płeć
>    - funkcja `GROUP_CONCAT` na dowolnej kolumnie nie będącej id
>    - funkcja `MIN`, `MAX` oraz `AVG` na kolumnie `dataUrodzenia`, przy czym wynik `AVG` (w związku z działaniem średniej na dacie) powinien zwracać średni wiek w dniu wywołania procedury
>    - funkcja `STD` oraz `VAR_POP` na kolumnie `dataUrodzenia`, działająca analogicznie do funkcji `AVG`
>
>    Załóż obecność użytkownika, próbującego dokonać zmian w strukturze jak i zawartości bazy danych, próbującego wywołać błąd funkcji lub poznać strukturę tabel. Zadbaj o poprawność i bezpieczeństwo działania.
>
> 5. Utwórz tabelę `hasła` zawierającą informacje o id osoby oraz jej haśle. W kolumnie odnoszącej się do hasła przechowuj tylko hash hasła (wykorzystaj funkcję `md5()` lub `sha1()`. Napisz procedurę przyjmujacą jako parametry imię osoby oraz jej hasło, a następnie hashuje je (wykorzystując odpowiednią funkcję) i w przypadku zgodności, zwraca datę urodzenia osoby, w przypadku braku zgodności wypisuje losową datę (losowa data powinna uwzględniać wymagania odnośnie pełnoletności oraz nie implikować osób ponad 100letnich).
>
> 6. Pobierz WebGoat i uruchom na swoim komputerze (w celu uniknięcia podatności możesz rozłączyć się z internetem). Wykonaj tutorial odnośnie *Injection Flaws*:
>    - opcjonalnie – SQL Injection (introduction)
>    - SQL Injection (advanced)
>    - SQL Injection (mitigation)
>
>    Wybierz jedną z sekcji (advanced lub mitigation) i opisz wykonane ćwiczenia oraz wyciągnięte wnioski. Raport wyślij prowadzącemu zajęcia co najmniej 24 godziny przed terminem oddania.
> 7. Wykorzystując CTE oraz rekursję napisz zapytanie obliczające liczbę $\binom{n}{k}$ dla nieujemnych liczb całkowitych $n\ge k$. Pamiętaj o warunkach brzegowych $\binom{n}{0} = \binom{n}{n} = 1$. Wywołaj zapytanie dla $n \in \{5, 7, 8, 9\}$ oraz $k \in \{2, 3, . . . , 5\}$.
>
> 8. Napisz procedurę, która jako parametr wejściowy przyjmuję nazwę zawodu, a następnie daje wszystkim wykonującym ten zawód 10% podwyżki przy zachowaniu ograniczeń wynikającymi z widełek płacowych w tabeli `zawody`. Operacja powinna wykonać się transakcyjnie, tzn. albo wszyscy pracownicy danego zawodu dostają podwyżkę albo (przy przekroczeniu widełek przez przynajmniej jedną osobę) nikt.
>
> 9. Napisz procedurę, która przyjmuje jako parametr nazwę zawodu, a następnie zwraca, na podstawie tabeli `praca`, informacje na temat średniej pensji osób pracujących w danym zawodzie przy zachowaniu 0.03–prywatności różnicowej. Zadbaj o to, by zwracany wynik nie wykraczał poza widełki dla danego zawodu.
>
> 10. Zrób Backup bazy danych tej listy. Usuń bazę danych, a następnie ją przywróć z backupu. Sporządź krótki raport z wykonanych czynności. Uwzględnij zarówno obsługę w swoim IDE jak i wykorzystanie wyłącznie linii komend. Wyjaśnij różnicę między backupem pełnym a różnicowym. Raport wyślij prowadzącemu zajęcia co najmniej 24 godziny przed terminem oddania.

Pliki `ex-*.sql` zawierają zadane kwerendy.

Raporty do zadań [6](ex-6.md) oraz [10](ex-10.md) znajdują się w osobnych dokumentach MD.
