Drop trigger if exists deleting_osoba;

DELIMITER $$
Create trigger deleting_osoba
    After Delete
    on osoba
    FOR EACH ROW
Begin
    Delete From hobby Where hobby.osoba = old.id;
    SET @min = (Select MIN(id) from osoba);
    SET @max = (Select MAX(id) from osoba);
    SET @new_owner =
            (Select id
             from osoba
             Where id >= Round(@min + rand() * (@max - @min))
             LIMIT 1);
    Update zwierzak
    Set owner = @new_owner
    Where owner = old.id;
end $$

DELIMITER ;