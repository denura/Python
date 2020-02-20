"""1. Напишите функцию, которая возвращает размер HTML документа по адресу https://google.com.
  Т.е. нужно получить страницу и вернуть ее размер (количество символов)."""

import requests


def html_page_size(url):
    html_length = len(requests.get(url).text)
    return html_length

url = 'https://google.com'
print("Размер HTML документа по адресу", url, "равен", html_page_size(url), "(символов)")
