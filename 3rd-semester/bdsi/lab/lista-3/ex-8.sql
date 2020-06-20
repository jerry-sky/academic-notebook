DROP PROCEDURE IF EXISTS give_raises;

DELIMITER $$

CREATE PROCEDURE give_raises(IN _zawod VARCHAR(20))
BEGIN

    SET @zawod_id = (SELECT id FROM zawody WHERE nazwa = _zawod LIMIT 1);
    SET @pensja_max = (SELECT pensja_max FROM zawody WHERE id = @zawod_id);
    SET autocommit = 0;

    START TRANSACTION;

    UPDATE praca SET pensja = FLOOR(pensja * 1.1) WHERE zawod = @zawod_id;

    IF (SELECT COUNT(*) FROM praca WHERE pensja > @pensja_max AND zawod = @zawod_id) > 0 THEN
        SELECT 'Giving raises has been cancelled due to existance of a person that would exceed the maximum salary.' as Result;
        ROLLBACK;
    ELSE
        SELECT 'Raises have been applied.' as Result;
        COMMIT;
    END IF;

END $$

DELIMITER ;

CALL give_raises('FUJJV');
