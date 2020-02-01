"""2. Написать функцию, которая принимает 3 числа (a,b,c) и проверяет сколько чисел между ‘a’ и ‘b’
делятся на ‘c’.
"""


def divisibility(low_limit, high_limit, denominator):
    """
    :type low_limit: int
    :type high_limit: int
    :type denominator: int
    """
    divisibility_counter = 0
    while low_limit <= high_limit:
        if low_limit % denominator == 0:
            print("Число %.d делится на %.d" % (low_limit, denominator))
            divisibility_counter += 1
        low_limit += 1
    print("Количество чисел в нашем интервале, делящихся на %.d: %.d" % (denominator, divisibility_counter))


low_limit = int(input("Введите число - нижнюю границу диапазона: "))
high_limit = int(input("Введите число - верхнюю границу диапазона: "))
denominator = int(input("Введите число - делитель для чисел заданного диапазона: "))
divisibility(low_limit, high_limit, denominator)
