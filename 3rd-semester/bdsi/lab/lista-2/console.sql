
# Select ELT(1 + RAND() * 2, 'sport', 'nauka', 'inne');

# Select Round(RAND());

Call fill_out_random('hobby', 1300);

Call get_all_hobbies(5);

Insert Into hobby (osoba, id, typ) VALUES (6, 302, 'nauka');

Delete From sport Where id = 5;

Update nauka Set nazwa = '***CHANGED***' WHERE id = 5;

Call biggest_number_of_hobbies();

