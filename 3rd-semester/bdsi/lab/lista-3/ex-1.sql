
CREATE INDEX imię_index ON osoba (`imię`);

CREATE INDEX dataUrodzenia_index ON osoba (`dataUrodzenia`);

CREATE INDEX id_nazwa_index ON sport (`id`, `nazwa`);

CREATE INDEX nazwa_id_index ON inne (`nazwa`, `id`);

CREATE INDEX osoba_id_typ ON hobby (`osoba`, `id`, `typ`);