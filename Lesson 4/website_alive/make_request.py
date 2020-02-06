"""4. Внутри модуля make_request напишите функцию, которая делает запрос на сайт с использованием
библиотеки requests, и возвращает объект (найдите документацию по библиотеке, вам будет достаточно
раздела QuickStart)
https://3.python-requests.org/user/quickstart/
"""

import requests


def get(url):
    """делает запрос на сайт с использованием библиотеки requests, и возвращает объект"""
    get_url_request = requests.get(url)
    print(get_url_request)
    return get_url_request
