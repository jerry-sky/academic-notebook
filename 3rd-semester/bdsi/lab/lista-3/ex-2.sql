EXPLAIN
SELECT osoba.imię, osoba.plec
FROM osoba
WHERE osoba.imię LIKE 'A%';

EXPLAIN
SELECT sport.nazwa
FROM sport
ORDER BY nazwa;

EXPLAIN
SELECT a.id as a, b.id as b
FROM sport a JOIN sport b on a.id > b.id AND a.lokacja = b.lokacja
WHERE a.typ = 'indywidualny' AND b.typ = 'indywidualny';

EXPLAIN
SELECT osoba.imię, osoba.dataUrodzenia
FROM osoba FORCE INDEX (dataUrodzenia_index)
Where dataUrodzenia < '2000-01-01';

EXPLAIN
SELECT *
FROM hobbies_people
ORDER BY cnt DESC
LIMIT 1;
# WHERE nazwa IN (SELECT nazwa FROM hobbies_people ORDER BY cnt DESC LIMIT 1);

EXPLAIN
SELECT imię, dataUrodzenia
FROM osoba
WHERE id IN (SELECT owner FROM zwierzak WHERE species = 'dog')
ORDER BY dataUrodzenia
LIMIT 1;

SHOW ENGINES;

SHOW INDEXES FROM sport;