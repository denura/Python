"""1. Написать несколько функций, которые в качестве единственного аргумента принимают список (или
кортеж) целых чисел.
- первая функция должна вернуть квадраты элементов коллекции;
- вторая функция должна вернуть только элементы на четных позициях;
- третья функция возвращает кубы четных элементов на нечетных позициях.
"""


def square_numbers(list_whole_numbers):
    """функция должна вернуть квадраты элементов коллекции"""
    iterator = 0
    result_list_whole_numbers = [0] * len(list_whole_numbers)
    for number in list_whole_numbers:
        result_list_whole_numbers[iterator] = number * number
        iterator += 1
    print("Квадраты элементов коллекции:", result_list_whole_numbers)
    return result_list_whole_numbers

def even_position_elements(list_whole_numbers):
    """функция должна вернуть только элементы на четных позициях"""
    input_iterator = 0
    result_list_whole_numbers = []
    for number in list_whole_numbers:
        if input_iterator % 2 == 0:
            result_list_whole_numbers.append(list_whole_numbers[input_iterator])
        input_iterator += 1
    print("Список элементов на четных позициях", result_list_whole_numbers)
    return result_list_whole_numbers


list_whole_numbers = (1, 2, 3, 5, 7)
print("Кортеж целых чисел:", list_whole_numbers)

square_numbers(list_whole_numbers)
even_position_elements(list_whole_numbers)
