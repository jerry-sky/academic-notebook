PREPARE stmt From
    'Select h.osoba, h.typ, n.nazwa
    From hobby h
        Join nauka n On h.id = n.id
    Where h.typ = \'nauka\'
    UNION
    Select h.osoba, h.typ, s.nazwa
    From hobby h
        Join sport s on h.id = s.id
    Where h.typ = \'sport\'
    UNION
    Select h.osoba, h.typ, i.nazwa
    From hobby h
        Join inne i on h.id = i.id
    Where h.typ = \'inne\'';

EXECUTE stmt;
DEALLOCATE PREPARE stmt;
