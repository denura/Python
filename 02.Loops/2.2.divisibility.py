"""2. Написать функцию, которая принимает 3 числа (a,b,c) и проверяет сколько чисел между ‘a’ и ‘b’
делятся на ‘c’.
"""
DIVISER = diviser
HIGH_LIMIT = high_limit


def divisibility(low_limit, HIGH_LIMIT, DIVISER):
    """
    :type low_limit: int
    :type HIGH_LIMIT: int
    :type DIVISER: int
    """
    divisibility_counter = 0
    while low_limit <= HIGH_LIMIT:
        if low_limit % DIVISER == 0:
            print("Число %.d делится на %.d" % (low_limit, DIVISER))
            divisibility_counter += 1
        low_limit += 1
    print("Количество чисел в нашем интервале, делящихся на %.d: %.d" % (DIVISER, divisibility_counter))


low_limit = int(input("Введите число - нижнюю границу диапазона: "))
HIGH_LIMIT = int(input("Введите число - верхнюю границу диапазона: "))
DIVISER = int(input("Введите число - делитель для чисел заданного диапазона: "))
divisibility(low_limit, HIGH_LIMIT, DIVISER)
