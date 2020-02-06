"""6. В корневой директории ("Lesson 4") создайте файл main.py, который при запуске спрашивает у
пользователя адрес сайта, который необходимо проверить. Дальше делает проверку, используя пакет
website_alive, и пишет, доступен ли сайт."""

import website_alive.check_response

URL = input("Введите адрес сайта для проверки, например, http://ya.ru: ")
if website_alive.check_response.get_url(URL):
    print("Сайт доступен")
else:
    print("Сайт недоступен")
