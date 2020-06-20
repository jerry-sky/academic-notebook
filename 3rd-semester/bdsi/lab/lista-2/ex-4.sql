Alter Table osoba
    Add Column `nazwisko` varchar(20) After `imię`;

Alter Table zwierzak
    Add Column `ownerID` int After `owner`;

Update zwierzak Set zwierzak.ownerID = (Select id From osoba Where osoba.imię = zwierzak.owner);

Alter Table zwierzak
    Drop Column `owner`,
    Change Column `ownerID` `owner` int Not null