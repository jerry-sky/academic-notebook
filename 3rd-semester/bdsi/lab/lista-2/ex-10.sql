Drop PROCEDURE IF EXISTS get_all_hobbies;

DELIMITER $$

CREATE PROCEDURE get_all_hobbies(IN osoba_id int)
BEGIN
    Select h.typ, n.nazwa
    From hobby h
             Join nauka n On h.id = n.id
    Where osoba = osoba_id
      And h.typ = 'nauka'
    UNION
    Select h.typ, s.nazwa
    From hobby h
             Join sport s on h.id = s.id
    Where osoba = osoba_id
      And h.typ = 'sport'
    UNION
    Select h.typ, i.nazwa
    From hobby h
             Join inne i on h.id = i.id
    Where osoba = osoba_id
      And h.typ = 'inne'
    UNION
    Select 'animal' as typ, species as nazwa
    From zwierzak
    WHERE owner = osoba_id
    GROUP BY species;
END $$
DELIMITER ;