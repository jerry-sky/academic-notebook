Drop trigger if exists deleting_nauka_hobby;
Drop trigger if exists updating_nauka_hobby;

DELIMITER $$
Create trigger deleting_nauka_hobby
    After Delete
    on nauka
    FOR EACH ROW
Begin
    Delete From hobby Where hobby.typ = 'nauka' And hobby.id = old.id;
end $$

Create trigger updating_nauka_hobby
    After Update
    on nauka
    FOR EACH ROW
Begin
    Delete From hobby Where hobby.typ = 'nauka' And hobby.id = old.id;
end $$

DELIMITER ;