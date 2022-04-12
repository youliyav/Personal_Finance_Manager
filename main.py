"""Запускает приложение"""
from user.login import send_welcome
from user.options import caller


def main():
    try:
        name = send_welcome()
        print(f'Hi, {name}')
        caller()
    except:
        print(Exception)


if __name__ == '__main__':
    main()

