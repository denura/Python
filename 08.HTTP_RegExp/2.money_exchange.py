"""2. Напишите функцию, которая принимает три аргумента
  1)число, количество денег в исходной валюте, float;
  2)исходная валюта, трехсимвольная строка, str;
  3)целевая валюта, трехсимвольная строка, str;
  и возвращает количество денег в целевой валюте (тип float).
  Для получения курса валют воспользуйтесь https://api.exchangerate-api.com ."""


import requests


def money_exchange(money_count, source_money, destination_money):
    return new_money_count