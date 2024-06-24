import sqlite3

connection = sqlite3.Connection('SQLite.db')
cursor = connection.cursor()

#cursor.execute('create table Table1 (id int, name text, stringss text)')
#cursor.execute('create table Table2 (num int, color str, animal str, time int, game str)')

#cursor.execute('insert into Table1 (id, name, stringss) values (1, "Grinch", "brother")')
#cursor.execute('insert into Table1 (id, name, stringss) values (2, "Grag", "bro")')
#cursor.execute('insert into Table1 (id, name, stringss) values (3, "Georgi", "brotella")')


cursor.execute('insert into Table2 (num, color, animal, time, game) values (1, "brown", "cat", 13.00, "scratches") ')
cursor.execute('insert into Table2 (num, color, animal, time, game) values (2, "beige", "dog", 9.00, "ball") ')
cursor.execute('insert into Table2 (num, color, animal, time, game) values (3, "green", "snake", 13.00, "mouse" ) ')

connection.commit()
cursor.close()