"""1. Написать несколько функций, которые в качестве единственного аргумента принимают список (или
кортеж) целых чисел.
- первая функция должна вернуть квадраты элементов коллекции;
- вторая функция должна вернуть только элементы на четных позициях;
- третья функция возвращает кубы четных элементов на нечетных позициях.
"""


def square_numbers(list_whole_numbers):
    """
    :type list_whole_numbers: int
    """
    iterator = 0
    for number in list_whole_numbers:
        list_whole_numbers[iterator] *= number
        iterator += 1
    print("Квадраты элементов коллекции:", list_whole_numbers)


list_whole_numbers = [1, 2, 3, 5, 7]
print("Список целых чисел:", list_whole_numbers)

square_numbers(list_whole_numbers)
