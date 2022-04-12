"""
Инструкция по работе с библиотекой Loguru
manual - https://github.com/Delgan/loguru#readme
pip install loguru
"""

from loguru import logger

# logger.add("debug.log", format="{time} {level} {message}", level="DEBUG")
#
# logger.debug("That's it, beautiful and simple logging!(debug)")
# logger.info("Hello! (info)")
# logger.error("Hi!(error)")

# -----------------
# Ротирование логов (архивирование, удаление старых логов) для сохранение памяти на диске
# Добавляем: rotation="10 KB" и compression="zip"
# Примеры использования:
# logger.add("file_1.log", rotation="500 MB")    # Automatically rotate too big file
# logger.add("file_2.log", rotation="12:00")     # New file is created each day at noon
# logger.add("file_3.log", rotation="1 week")    # Once the file is too old, it's rotated
# logger.add("file_X.log", retention="10 days")  # Cleanup after some time
# logger.add("file_Y.log", compression="zip")    # Save some loved space

# Использовать можно так:
# logger.add("debug.log", format="{time} {level} {message}", level="DEBUG",
#            rotation="10 KB", compression="zip")
#
# for _ in range(1000):
#     logger.debug("Hello (debug)!")


# -----------------------
# Декоратор @logger.catch

# logger.add("debug.log", format="{time} {level} {message}", level="DEBUG",
#            rotation="10 KB", compression="zip")

# -------- без декоратора @logger.catch
# def func(a, b):
#     return a / b
#
# def nested(c):
#     try:
#         func(5, c)
#     except ZeroDivisionError:
#         logger.exception("What?!")
#
# nested(0)


# ------ используя @logger.catch получим тоже error и исключение ZeroDivisionError

# def divide(a, b):
#     return a / b
#
# @logger.catch()
# def main():
#     divide(5, 0)
#
# main()

# ----------------------------------------------------------
# Для парсинга удобно сообщения логов хранить в формате json
# serialize="True"

# logger.add("debug.json", format="{time} {level} {message}", level="DEBUG",
#            serialize=True)
#
# def divide(a, b):
#     return a / b
#
# @logger.catch()
# def main():
#     divide(5, 0)
#
# main()


