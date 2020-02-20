"""3. Напишите функцию, которая получает два аргумента
  1)путь к файлу изображения jpeg на компьютере (строка);
  2)имя целевого файла (строка)
  отправляет файл HTTP POST запросом на https://postman-echo.com/post .
  В ответе будет получен файл изображения jpeg, в виде octet-stream, который нужно раскодировать и
  сохранить на компьютере под целевым именем, переданным в аргументе.
  Функция должна вернуть размер сохраненного файла.
"""


import requests

def new_picture_size(jpeg_path, file_name):
    """Функция должна вернуть размер сохраненного файла"""
    url = 'https://postman-echo.com/post'
    files = {'file': (open('jpeg_path', 'rb'), 'image/jpeg')}
    response = requests.post(url, files=files)
    response.raise_for_status()
    file = open('file_name', 'w')
    file.write(response.text)
    file.close()
    return len(file_name)
