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

# 2. Написать функцию, которая принимает 3 числа (a,b,c) и проверяет сколько чисел между ‘a’ и ‘b’
# делятся на ‘c’.


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

# 3. Написать функцию вычисления факториала числа


def calc_factorial(initial_val):
    """
    :type initial_val: int
    """
    factorial = 1
    if initial_val == 0:
        print("%.d! = %d" % (initial_val, factorial))
    else:
        while initial_val > 1:
            factorial *= initial_val
            initial_val -= 1
        print("Факториал введенного числа = ", factorial)


initial_val = int(input("Введите число для вычисления его факториала: "))
calc_factorial(initial_val)

# 4. Написать свою имплементацию функции range() из Python 2.x (аналогично Python 3,
# только возвращает список).


def python2_range(start, stop, step):
    """
    :type start: int
    :type stop: int
    :type step: int
    """
    i = 1
    if step > 1:
        result_list = [0] * int((stop - start + step) // step)
    else:
        result_list = [0] * int(stop - start)
    result_list[0] = start
    if stop == 0:
        print(result_list)
    else:
        while start < (stop - 1):
            result_list[i] = start + step
            start += step
            i += 1
        print(result_list)


start = int(input("Введите первый член арифметической прогрессии: "))
stop = int(input("Введите последний член арифметической прогрессии: "))
step = int(input("Введите шаг арифметической прогрессии: "))
python2_range(start, stop, step)
