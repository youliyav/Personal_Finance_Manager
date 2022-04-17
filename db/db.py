"""Работа с таблицами
   Создать в tables.sql таблицы clients, platform, account, tax"""

import os
import sqlite3
from typing import Dict, List


conn = sqlite3.connect(os.path.join("db", "finance.db"))
cursor = conn.cursor()


def insert_data(table: str, dict_col: Dict) -> None:
    """db.insert("users", {"email": 'youliya',
                           "password": '1234',
                           "name": 'Julia',
                           "surname": 'Bro'})"""

    columns = ', '.join(dict_col.keys())  # email, password, name, surname
    values = [tuple(dict_col.values())]  # [('youliya', '1234', 'Julia', 'Bro')]
    placeholders = ", ".join("?" * len(dict_col.keys()))  # ?, ?, ?, ?
    cursor.executemany(
        f"INSERT INTO {table} "
        f"({columns}) "
        f"VALUES ({placeholders})",
        values)
    conn.commit()


def fetchall(table: str, list_col: List[str]) -> List[Dict]:
    """ db.fetchall('users', ['user_id',
                              'email',
                              'password',
                              'name',
                              'surname']) """
    columns = ", ".join(list_col)
    cursor.execute(f"SELECT {columns} FROM {table}")
    rows = cursor.fetchall()  # [(...), (...), (1, 'youliya', '1234', 'Julia', 'Bro'), (...)]
    res = []
    for row in rows:
        dict_row = {}
        for i, column in enumerate(list_col):
            dict_row[column] = row[i]
        res.append(dict_row)
    return res  # [{...}, {...}, {"email": "youliya", ...}]


def delete(table: str, row_id: int) -> None:
    row_id = int(row_id)
    cursor.execute(f"DELETE FROM {table} WHERE id={row_id}")
    conn.commit()


def get_cursor():
    return cursor


def _init_db():
    """Инициализирует БД"""
    with open('tables.sql', 'r', encoding='utf-8') as f:
        sql = f.read()
    cursor.executescript(sql)
    conn.commit()


def check_db_users():
    """Проверяет инициализирована ли БД users"""
    cursor.execute('SELECT name FROM sqlite_master '
                   'WHERE type="table" AND name="users"')
    table_users = cursor.fetchall()
    if table_users:
        return print('БД users уже инициализирована!')
    _init_db()


check_db_users()
