Drop PROCEDURE IF EXISTS biggest_number_of_hobbies;

DELIMITER $$

CREATE PROCEDURE biggest_number_of_hobbies()
BEGIN
    Set @max = (Select count(*) From hobby GROUP BY osoba ORDER BY count(*) DESC Limit 1);
    Set @osoba = (Select osoba From hobby GROUP BY osoba Having count(*) = @max);
    Select imię, TIMESTAMPDIFF(YEAR, dataUrodzenia, NOW()) as wiek From osoba Where id = @osoba;
END $$
DELIMITER ;
