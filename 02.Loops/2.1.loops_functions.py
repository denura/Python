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


#number = int(input("Введите верхнюю границу интервала: "))
#is_even(number)

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


#a = int(input("Введите число a - нижнюю границу диапазона: "))
#b = int(input("Введите число b - верхнюю границу диапазона: "))
#c = int(input("Введите число c - делитель для чисел заданного диапазона: "))
#divisibility(a, b, c)

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


#initial_val = int(input("Введите число для вычисления его факториала: "))
#calc_factorial(initial_val)

# 4. Написать свою имплементацию функции range() из Python 2.x (аналогично Python 3,
# только возвращает список).


def python2_range():
    n = 7  # skolko chlenov vivest
    i = 1
    acc_an = 2
    list_ = [0] * n
    list_[0] = acc_an
    print(acc_an)
    while i < n:
        acc_an = acc_an - 2
        list_[i] = acc_an
        print('nomer elementa: %d,sam element %d' % (i, acc_an))
        i += 1
    print(list_)
    print(sum(list_))
    # 2
    # nomer elementa: 1,sam element 0
    # nomer elementa: 2,sam element -2
    # nomer elementa: 3,sam element -4
    # nomer elementa: 4,sam element -6
    # nomer elementa: 5,sam element -8
    # nomer elementa: 6,sam element -10
    # [2, 0, -2, -4, -6, -8, -10]
    # -28