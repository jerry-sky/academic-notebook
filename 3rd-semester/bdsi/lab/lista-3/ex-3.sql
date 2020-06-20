CREATE TABLE zawody
(
    id         INT UNSIGNED AUTO_INCREMENT NOT NULL,
    nazwa      VARCHAR(20)                 NOT NULL,
    pensja_min INT UNSIGNED                NOT NULL,
    pensja_max INT UNSIGNED                NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE praca
(
    zawod  INT UNSIGNED NOT NULL,
    osoba  INT          NOT NULL,
    pensja INT UNSIGNED NOT NULL,
    PRIMARY KEY (zawod, osoba)
);

ALTER TABLE praca
    ADD FOREIGN KEY (zawod) REFERENCES zawody (id),
    ADD FOREIGN KEY (osoba) REFERENCES osoba (id);

DELIMITER $$
CREATE PROCEDURE _TMP()
BEGIN
    DECLARE iterator INT DEFAULT 10;
    WHILE iterator > 0
        DO
            SET @_min = FLOOR(RAND() * 1500 + 1200);
            SET @_max = FLOOR(RAND() * 8000 + @_min);
            INSERT INTO zawody (nazwa, pensja_min, pensja_max)
            VALUES (generate_random_string(5), @_min, @_max);
            SET iterator = iterator - 1;
        END WHILE;
END $$
DELIMITER ;

CALL _TMP();
DROP PROCEDURE _TMP;

TRUNCATE praca;

DELIMITER $$
CREATE PROCEDURE _TMP()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE osoba_id INT;
    DECLARE osoba_cursor CURSOR FOR (SELECT id FROM osoba);
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
    OPEN osoba_cursor;
    read_loop:
    LOOP
        FETCH osoba_cursor INTO osoba_id;
        IF done THEN
            LEAVE read_loop;
        END IF;
        SET @zawody_id = FLOOR(RAND() * 10 + 1);
        SET @pensja_min = (SELECT pensja_min FROM zawody WHERE id = @zawody_id);
        SET @pensja_max = (SELECT pensja_max FROM zawody WHERE id = @zawody_id);
        INSERT INTO praca (zawod, osoba, pensja)
        VALUES (@zawody_id, osoba_id, FLOOR(RAND() * (@pensja_max - @pensja_min) + @pensja_min));
    END LOOP;
END $$
DELIMITER ;

CALL _TMP();
DROP PROCEDURE _TMP;
