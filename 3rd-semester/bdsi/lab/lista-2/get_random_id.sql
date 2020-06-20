DELIMITER $$

Create Or REPLACE Function get_random_id(table_name VARCHAR(255)) Returns INT DETERMINISTIC
Begin
    Prepare stmt_min from CONCAT('SET @min = (Select MIN(id)
    from ', table_name, ');');
    EXECUTE stmt_min;

    Prepare stmt_max from CONCAT('SET @max = (Select MAX(id)
    from ', table_name, ');');
    EXECUTE stmt_max;

    Prepare stmt_final from CONCAT('SET @id =
            (Select id
             from ', table_name, '
             Where id >= Round(@min + rand() * (@max - @min))
             LIMIT 1);');
    EXECUTE stmt_final;
    DEALLOCATE PREPARE stmt_min;
    DEALLOCATE PREPARE stmt_max;
    DEALLOCATE PREPARE stmt_final;

    return @id;
End $$

DELIMITER ;