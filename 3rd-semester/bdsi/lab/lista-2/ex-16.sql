Create View hobbies_people As
Select a.nazwa, count(*) as cnt
From (Select h.typ, n.nazwa
      From hobby h
               Join nauka n On h.id = n.id
      Where h.typ = 'nauka'
      UNION
      Select h.typ, s.nazwa
      From hobby h
               Join sport s on h.id = s.id
      Where h.typ = 'sport'
      UNION
      Select h.typ, i.nazwa
      From hobby h
               Join inne i on h.id = i.id
      Where h.typ = 'inne') a
GROUP BY a.nazwa