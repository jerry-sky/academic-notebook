-- Constraint merdas Check (
--   DATE_ADD(dataUrodzenia, Interval 18 Year) < CURRENT_DATE();
-- )
Create Table If not exists osoba (
  id int Not null AUTO_INCREMENT,
  imię varchar(20) Not null,
  dataUrodzenia date Not null,
  plec char(1) Not null,
  Primary key (id)
);
Create Table If not exists sport (
  id int Not null AUTO_INCREMENT,
  nazwa varchar(20) Not null,
  typ enum('indywidualny', 'drużynowy', 'mieszany') Not null Default 'drużynowy',
  lokacja varchar(20),
  Primary key (id)
);
Create Table If not exists nauka (
  id int Not null AUTO_INCREMENT,
  nazwa varchar(20) Not null,
  lokacja varchar(20) Not null,
  Primary key (id)
);
Create Table If not exists inne (
  id int Not null AUTO_INCREMENT,
  nazwa varchar(20) Not null,
  lokacja varchar(20),
  towarzysze bool Not null Default True,
  Primary key (id)
);
Create Table If not exists hobby (
  osoba int Not null,
  id int Not Null,
  typ enum('sport', 'nauka', 'inne'),
  Primary key (id, osoba, typ)
);