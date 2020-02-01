"""1. Написать функцию, которая печатает квадраты всех нечетных чисел в произвольном интервале
[0, Х]. А так же количество таких чисел.
"""
NUMBER = number


def is_even(NUMBER):
    """
    :type NUMBER: int
    """
    odd_counter = 0
    i = 0
    while i < NUMBER:
        i += 1
        if i % 2 > 0:
            print("Нечентное число: ", i)
            odd_counter += 1
            square = i * i
            print("Квадрат нечетного числа %.d = %.d" % (i, square))

    print("Количество нечетных чисел: ", odd_counter)


NUMBER = int(input("Введите верхнюю границу интервала: "))
is_even(NUMBER)
