Alter Table zwierzak
    Add FOREIGN KEY (owner) REFERENCES osoba (id);

Alter Table hobby
    Add FOREIGN KEY (osoba) REFERENCES osoba (id);