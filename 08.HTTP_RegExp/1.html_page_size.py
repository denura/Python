"""1. Напишите функцию, которая возвращает размер HTML документа по адресу https://google.com.
  Т.е. нужно получить страницу и вернуть ее размер (количество символов)."""

import requests


def html_page_size(url):
    """функция, которая возвращает размер HTML документа по переданному адресу"""
    return len(requests.get(url).text)


url = "https://google.com"
print("Размер HTML документа по адресу", url, "равен", html_page_size(url), "(символов)")
