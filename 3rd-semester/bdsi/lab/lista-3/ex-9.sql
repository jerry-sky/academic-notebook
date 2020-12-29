DELIMITER $$
CREATE OR REPLACE FUNCTION get_random_var_laplace(_sensitivity INT) RETURNS DECIMAL DETERMINISTIC
BEGIN
    SET @_random = RAND() - 0.5;
    SET @_var = 0 - ((_sensitivity / 0.03) * SIGN(@_random) * Log(1 - (2 * ABS(@_random))));
    RETURN @_var;
end $$
DELIMITER ;

DROP PROCEDURE IF EXISTS average_salary;

DELIMITER $$
CREATE PROCEDURE average_salary(IN _zawod VARCHAR(20))
BEGIN

    SET @zawod_id = (SELECT id FROM zawody WHERE nazwa = _zawod LIMIT 1);

    SET @sensitivity = (SELECT MAX(pensja) FROM praca WHERE zawod = @zawod_id) -
                       (SELECT MIN(pensja) FROM praca WHERE zawod = @zawod_id);

    SET @_max = (SELECT pensja_max FROM zawody WHERE id = @zawod_id);
    SET @_min = (SELECT pensja_min FROM zawody WHERE id = @zawod_id);


    SET @result = (SELECT AVG(a.pensja) as average_salary
                   FROM (SELECT pensja
                         FROM praca
                         WHERE zawod = @zawod_id
                         UNION
                         SELECT get_random_var_laplace(@sensitivity) as pensja) a);
#     SELECT FLOOR(AVG(pensja)) FROM praca WHERE zawod = @zawod_id;
    IF @result > @_max THEN
        SELECT @_max as average_salary;
    ELSEIF @result < @_min THEN
        SELECT @_min as average_salary;
    ELSE
        SELECT FLOOR(@result) as average_salary;
    END IF;


END $$
DELIMITER ;

CALL average_salary('NCTRC');