# .venv/bin/activate
# SQLite
"""
- cоздание файла .sql
    $ touch flights.sql

- запуск файла .sql
    $ sqlite3 flights.sql

- создание таблицы flights (NOT NULL ячейка обязательна к заполнению)
    $ sqlite> CREATE TABLE flights (
         ...> id INTEGER PRIMARY KEY AUTOINCREMENT,
         ...> origin TEXT NOT NULL,
         ...> destination TEXT NOT NULL,
         ...> duration INTEGER NOT NULL
         ...> );

- показывает какие таблицы созданы
    $ sqlite> .tables
      flights

- ничего не выведет, тк мы только создали таблицу и не заполнили ее
    $ sqlite> SELECT * FROM flights;

- вставка строки в flights
    $ sqlite> INSERT INTO flights (origin, destination, duration) VALUES ("New York", "London", 415);

- вывод все данных из таблицы flights
    $ sqlite> SELECT * FROM flights;
      1|New York|London|415

- прекращение работы в sqllite
    $ sqlite> ^D


    $ vim inserts.sql


- вставка строк в таблицу flights
    $ sqlite> INSERT INTO flights (origin, destination, duration) VALUES ("Shanghai", "Paris", 760);
    $ sqlite> INSERT INTO flights (origin, destination, duration) VALUES ("Istanbul", "Tokio", 700);
    $ ...

- вывод всех строк
    $ sqlite> SELECT * FROM flights;
1|New York|London|415
2|Shanghai|Paris|760
3|Istanbul|Tokio|700
4|New York|Paris|435
5|Moscow|Paris|245
6|Lima|New York|455

- делает красивый вывод колонок
    $ sqlite> .mode columns

- показывает заголовки
    $ sqlite> .headers yes

    $ sqlite> SELECT * FROM flights;

id  origin    destination  duration
--  --------  -----------  --------
1   New York  London       415
2   Shanghai  Paris        760
3   Istanbul  Tokio        700
4   New York  Paris        435
5   Moscow    Paris        245
6   Lima      New York     455

    $ sqlite> ^D

"""