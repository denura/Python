"""5. Внутри модуля check_response напишите функцию, которая на вход принимает URL как строку
(например, 'http://google.ru/') и использует функцию из предыдущего файла, чтобы сделать запрос.
Если status_code равен 200, функция возвращает True, иначе False."""

import make_request


def get_url(url):
    """функция на вход принимает URL как строку (например, 'http://google.ru/') и использует
    функцию из предыдущего файла, чтобы сделать запрос. Если status_code равен 200, функция
    возвращает True, иначе False."""
    make_request.get(url)
    print(make_request.status_code)
    if make_request.status_code == 200:
        print("True")
        return True
    else:
        print("False")
        return False

url = 'http://google.ru/'
get_url(url)
