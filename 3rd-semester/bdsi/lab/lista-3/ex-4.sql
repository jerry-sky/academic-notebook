DROP PROCEDURE IF EXISTS fire_aggregation_func;

DELIMITER $$
CREATE PROCEDURE fire_aggregation_func(IN agg VARCHAR(20), kol VARCHAR(255))
BEGIN
    SET @query = 'SELECT \'ERROR: Incorrect data submitted.\'';
    SET @_agg = LOWER(agg);
    IF @_agg = 'count' AND kol IN ('imię', 'plec') THEN
        SET @query = CONCAT('SELECT \'', kol, '\' as kol, \'COUNT\' as agg, COUNT(', kol, ') as X FROM osoba');

    ELSEIF @_agg = 'group_concat' AND kol IN ('imię', 'nazwisko', 'dataUrodzenia', 'plec') THEN
        SET @query =
                CONCAT('SELECT \'', kol, '\' as kol, \'GROUP_CONCAT\' as agg, GROUP_CONCAT(', kol, ') as X FROM osoba');

    ELSEIF @_agg IN ('min', 'max') AND kol = 'dataUrodzenia' THEN
        SET @query = CONCAT('SELECT \'', kol, '\' as kol, \'', UPPER(@_agg), '\' as agg, ', @_agg, '(', kol,
                            ') as X FROM osoba');

    ELSEIF @_agg = 'avg' AND kol = 'dataUrodzenia' THEN
        SET @query = CONCAT(
                'SELECT \'dataUrodzenia\' as kol, \'AVG\' as agg, AVG(TIMESTAMPDIFF(YEAR, dataUrodzenia, NOW())) as X FROM osoba');

    ELSEIF @_agg IN ('std', 'var_pop') AND kol = 'dataUrodzenia' THEN
        SET @query = CONCAT('SELECT \'dataUrodzenia\' as kol, \'', UPPER(@_agg), '\' as agg, ', @_agg,
                            '(TIMESTAMPDIFF(YEAR, dataUrodzenia, NOW())) as X FROM osoba');

    END IF;
    PREPARE stmt FROM @query;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END $$
DELIMITER ;

CALL fire_aggregation_func('var_pop', 'dataUrodzenia');



# SET @query = 'SELECT ?, COUNT(?) FROM osoba';
# SET @param = '*';
#
# PREPARE stmt from @query;
# EXECUTE stmt USING @param, @param;
# DEALLOCATE PREPARE stmt;