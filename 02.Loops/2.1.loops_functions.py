"""1. Написать функцию, которая печатает квадраты всех нечетных чисел в произвольном интервале
[0, Х]. А так же количество таких чисел.
"""


def is_even(number):
    odd_counter = 0
    for i in number:
        if i % 2 == 0:
            print("Четное число: ", i)
        else:
            print("Нечентное число: ", i)
            odd_counter += 1
            square = i * i
            print("Квадрат нечетного числа %.d: = %.d" %(i, square))
    print("Количество нечетных чисел: ", square)


number = input("Введите верхнюю границу интервала: ")
is_even(number)