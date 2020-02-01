"""1. Написать функцию, которая печатает квадраты всех нечетных чисел в произвольном интервале
[0, Х]. А так же количество таких чисел.
"""


def is_even(number):
    """
    :type number: int
    """
    odd_counter = 0
    i = 0
    while i < number:
        i += 1
        if i % 2 > 0:
            print("Нечентное число: ", i)
            odd_counter += 1
            square = i * i
            print("Квадрат нечетного числа %.d = %.d" % (i, square))

    print("Количество нечетных чисел: ", odd_counter)


number = int(input("Введите верхнюю границу интервала: "))
is_even(number)
