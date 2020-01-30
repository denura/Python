"""5. Написать программу, которая принимает от пользователя имя и пароль. Сравнивает пароль с
заданным в коде.
В случае совпадения печатает в консоль "Password for user: <Имя пользователя> is correct"
Если пароль не совпадает, то печатает в консоль
"Password for user: <Имя пользователя> is incorrect"
"Please try again..."
И снова запрашивает пароль (не завершается).
"""
NAME = input("Please enter your name: ")
DEFAULT_PASSWORD = "Pa$$w0rd"
password = ""
while password != DEFAULT_PASSWORD:
    password = input("Please enter your password: ")
    if password != DEFAULT_PASSWORD:
        print("Password for user: %s is incorrect. Please try again..." % NAME)
