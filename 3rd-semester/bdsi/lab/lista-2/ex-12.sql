Drop trigger if exists deleting_sport_hobby;

DELIMITER $$
Create trigger deleting_sport_hobby
    After Delete
    on sport
    FOR EACH ROW
Begin
    Delete From hobby Where hobby.typ = 'sport' And hobby.id = old.id;
end
$$
DELIMITER ;