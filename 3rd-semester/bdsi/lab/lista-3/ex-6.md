
# BDSI-Lab Lista 3 Zadanie 6
## Raport dotyczący zadań z sekcji SQL Injection (Advanced) - WebGoat

Zadania polegały na wykorzystaniu błędu braku sanityzacji inputu użytkownika. Aplikacja bezpośrednio konkatenowała wejście
użytkownika z kwerendą i ją wykonywała, przez co bardzo łatwo można było manipulować bazą danych.

Celem w zadaniu 3 było wyciągnięcie dodatkowych informacji (tablicy zawierającej hasła użytkowników) z bazy danych.
Jednym z rozwiązań było wykorzystanie komendy UNION, która łączy wyniki kwerend wybierających (SELECT) pod warunkiem,
że liczba kolumn i ich typy zgadzają się pomiędzy tymi kwerendami wybierającymi.

Zadanie 5 było nieco trudniejsze. Należało uzyskać hasło innego użytkownika i zalogować się na jego konto. Tutaj
kluczowym elementem było wykrycie błędu formularza rejestracji, a dokładniej pola nazwy użytkownika. Program po stronie
serwera najpierw sprawdza czy już nie istnieje użytkownik o podanej nazwie. Jednakże, input użytkownika nie jest w żaden
sposób sanityzowany, więc można dodać dodatkowy warunek trywialny (np. 1 = 1 w celu uzyskania wartości TRUE, lub 1 = 2
w przeciwnym przypadku), lub też warunek sprawdzający na przykład część hasła (funkcja SUBSTRING). Przy wykorzystaniu
cierpliwości lub odpowiednio automatyzując czynności uzyskuje się znak po znaku hasło do konta użytkownika "Tom".
Co kończy zadanie.

Ostatnie zadanie 6 to quiz sprawdzający wiedzę z Prepared Statements, które zapobiegają SQL Injection.

## Wnioski: **nigdy nie można ufać użytkownikowi.**
Należy zawsze filtrować input użytkownika i nigdy nie konkatenować kwerendy bezpośrednio z wejściem użytkownika.
Najlepiej używać Prepared Statements.
