"""Работа с login авторизация регистрация"""
from user.users import validate_credentials, add_user, read_users_table
from typing import Tuple


def select_login_form() -> str:
    """ Спрашивает, есть ли у пользователя аккаунт """
    print('Do you have an account?')
    ans = input("Please type 'yes' or 'no'\n")
    return ans


def log_in() -> Tuple[str, str]:
    """ Просит предоставить учетные данные """
    print('Please log in by providing your user credentials')
    email = input('Email: ')
    password = input('Password: ')
    return email, password


def sign_up() -> Tuple[str, str, str, str]:
    """ Вызывает форму регистрации """
    print('Please register. Input your credentials')
    email = input('Email: ')
    password = input('Password: ')
    name = input('Name: ')
    surname = input('Surname: ')

    raw_data = (email, password, name, surname)
    print("You will be registered and added to DB")
    return raw_data


def authorize(email, passw, db_email, db_passw):
    """ Вызывает форму авторизации """
    if email in db_email:
        if passw == db_passw:
            print(f'{email.capitalize()} you have successfully logged in!')
            return email
        else:
            print('Your password is not correct. Please try again!')
            select_login_form()


def send_welcome():
    """
    select_login_form() возвращает ответ user
    == yes: вызывает функцию log_in() --> tuple(email, password)
    == no: вызывает функцию sign_up() --> tuple(email, password, name, surname)
    def validate_credentials() делает проверку по email --> tuple(email, password)
    def authorize() вызывает форму авторизации --> str(email)
    """
    ans_user = select_login_form()
    if ans_user == 'yes':
        login = log_in()
        email_input = login[0]
        password_input = login[1]

        validation_data = validate_credentials(check_email=email_input)
        db_email = validation_data[0]
        db_passw = validation_data[1]
        res = authorize(email=email_input,
                        passw=password_input,
                        db_email=db_email,
                        db_passw=db_passw)
        return res

    if ans_user == 'no':
        user_raw_data = sign_up()
        try:
            add_user(user_raw_data)
            print(read_users_table())
            send_welcome()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    send_welcome()
