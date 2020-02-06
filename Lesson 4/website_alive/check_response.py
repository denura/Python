"""5. Внутри модуля check_response напишите функцию, которая на вход принимает URL как строку
(например, 'http://google.ru/') и использует функцию из предыдущего файла, чтобы сделать запрос.
Если status_code равен 200, функция возвращает True, иначе False."""

import website_alive.make_request


def get_url(url):
    """функция на вход принимает URL как строку (например, 'http://google.ru/') и использует
    функцию из предыдущего файла, чтобы сделать запрос. Если status_code равен 200, функция
    возвращает True, иначе False."""
    website_alive.make_request.get(url)
    if website_alive.make_request.get(url).status_code == 200:
        return True
    return False
