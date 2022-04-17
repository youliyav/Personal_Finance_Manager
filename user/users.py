from typing import Dict, List, Tuple
import db.db as db


def add_user(user_raw_data: tuple):
    """Добавляет новые данные.
    Принимает на вход учетные данные, заполненные пользователем."""
    db.insert_data("users", {
        "email": user_raw_data[0],
        "password": user_raw_data[1],
        "name": user_raw_data[2],
        "surname": user_raw_data[3]
    })
    print("Data to insert: ", user_raw_data)  # ('youl', 'passw', 'jul', 'bra')


def read_users_table() -> List[Dict]:
    print("The users table contains the following data: ")
    return db.fetchall('users', ['user_id', 'email', 'password', 'name', 'surname'])
    # [{...}, {...}, {"email": "youl", ...}]


def validate_credentials(check_email):
    cursor = db.get_cursor()
    check_data = (check_email,)
    cursor.execute("SELECT email, password FROM users WHERE email=?", check_data)
    res = cursor.fetchone()
    # print("User's email and password: ", res)
    return res





