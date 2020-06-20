Drop View IF EXISTS people;

Create View people As
Select *
From (Select h.osoba, h.typ, n.nazwa as `hobby/zwierzak`
      From hobby h
               Join nauka n On h.id = n.id
      Where h.typ = 'nauka'
      UNION
      Select h.osoba, h.typ, s.nazwa
      From hobby h
               Join sport s on h.id = s.id
      Where h.typ = 'sport'
      UNION
      Select h.osoba, h.typ, i.nazwa
      From hobby h
               Join inne i on h.id = i.id
      Where h.typ = 'inne'
      UNION
      Select owner as osoba, 'animal' as typ, species as nazwa
      From zwierzak) a
         Join osoba On a.osoba = osoba.id
ORDER BY a.osoba;

Select *
From people;