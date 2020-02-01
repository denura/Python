"""2. Написать функцию, которая принимает 3 числа (a,b,c) и проверяет сколько чисел между ‘a’ и ‘b’
делятся на ‘c’.
"""


def divisibility(a, b, c):
    """
    :type a: int
    :type b: int
    :type c: int
    """
    divisibility_counter = 0
    while a <= b:
        if a % c == 0:
            print("Число %.d делится на %.d" % (a, c))
            divisibility_counter += 1
        a += 1
    print("Количество чисел в нашем интервале, делящихся на %.d: %.d" % (c, divisibility_counter))


a = int(input("Введите число a - нижнюю границу диапазона: "))
b = int(input("Введите число b - верхнюю границу диапазона: "))
c = int(input("Введите число c - делитель для чисел заданного диапазона: "))
divisibility(a, b, c)
