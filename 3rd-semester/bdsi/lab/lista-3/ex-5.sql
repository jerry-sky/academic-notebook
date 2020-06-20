
CREATE TABLE hasła (
    osoba INT NOT NULL,
    hasło TEXT NOT NULL,
    PRIMARY KEY (osoba),
    FOREIGN KEY (osoba) REFERENCES osoba (id)
);

INSERT INTO hasła (osoba, hasło) VALUES (1, md5('a strong password'));

DROP PROCEDURE IF EXISTS get_dataUrodzenia;

DELIMITER $$

CREATE PROCEDURE get_dataUrodzenia(IN _imię VARCHAR(20), _hasło TEXT, OUT _dataUrodzenia DATE)
BEGIN
    SET @hashed = md5(_hasło);
    SET @osoba_id = (SELECT id FROM osoba WHERE `imię` = _imię LIMIT 1);
    SET @pseudo_auth = (SELECT count(*) FROM hasła WHERE osoba = @osoba_id AND hasło = @hashed);
    IF @pseudo_auth > 0 THEN
        SET _dataUrodzenia = (SELECT `dataUrodzenia` FROM osoba WHERE `id` = @osoba_id);
    ELSE
        SET _dataUrodzenia = generate_random_date('1970-01-02', '1999-12-31');
    END IF;

END $$
DELIMITER ;

CALL get_dataUrodzenia('Harold', 'a strong password', @dataUrodzenia);

SELECT @dataUrodzenia;


