Drop trigger if exists adding_new_hobby;

DELIMITER $$
Create trigger adding_new_hobby
    After insert
    on hobby
    FOR EACH ROW
Begin
    IF new.typ = 'inne' And (Select count(*) from inne Where id = new.id) = 0 Then
        Insert Into inne (id, nazwa, lokacja, towarzysze)
        Values (new.id, generate_random_string(7), generate_random_string(11), Round(rand()));
    ELSEIF new.typ = 'nauka' And (Select count(*) from nauka Where id = new.id) = 0 Then
        Insert Into nauka (id, nazwa, lokacja)
        Values (new.id, generate_random_string(7), generate_random_string(11));
    ELSEIF new.typ = 'sport' And (Select count(*) from sport Where id = new.id) = 0 Then
        Insert Into sport (id, nazwa, typ, lokacja)
        VALUES (new.id, generate_random_string(7), ELT(1 + rand() * 2, 'indywidualny', 'drużynowy', 'mieszany'),
                generate_random_string(11));
    end IF;
end
$$
DELIMITER ;