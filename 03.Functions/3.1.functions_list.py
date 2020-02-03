"""1. Написать несколько функций, которые в качестве единственного аргумента принимают список (или
кортеж) целых чисел.
- первая функция должна вернуть квадраты элементов коллекции;
- вторая функция должна вернуть только элементы на четных позициях;
- третья функция возвращает кубы четных элементов на нечетных позициях.
"""


def square_numbers(tuple_whole_numbers):
    """функция должна вернуть квадраты элементов коллекции"""
    iterator = 0
    result_list_whole_numbers = [0] * len(tuple_whole_numbers)
    for number in tuple_whole_numbers:
        result_list_whole_numbers[iterator] = number * number
        iterator += 1
    print("Квадраты элементов коллекции:", result_list_whole_numbers)
    return result_list_whole_numbers


def even_position_elements(tuple_whole_numbers):
    """функция должна вернуть только элементы на четных позициях"""
    input_iterator = 1
    result_list_whole_numbers = []
    for number in tuple_whole_numbers:
        if input_iterator % 2 == 0:
            result_list_whole_numbers.append(tuple_whole_numbers[input_iterator - 1])
        input_iterator += 1
    print("Список элементов на четных позициях", result_list_whole_numbers)
    return result_list_whole_numbers


def cube_even_numbers_odd_position(tuple_whole_numbers):
    """функция возвращает кубы четных элементов на нечетных позициях"""
    input_iterator = 1
    list_odd_position = []
    list_cube_even_numbers_odd_position = []
    for number in tuple_whole_numbers:
        if input_iterator % 2 != 0:
            list_odd_position.append(tuple_whole_numbers[input_iterator - 1])
        input_iterator += 1
    print("Список элементов на нечетных позициях", list_odd_position)
    for number in list_odd_position:
        if number % 2 == 0:
            print("Четный элемент предыдущего списка: ", number)
            list_cube_even_numbers_odd_position.append(number * number * number)
    if list_cube_even_numbers_odd_position:
        print("Кубы четных элементов на нечетных позициях", list_cube_even_numbers_odd_position)
    else:
        print("Четных элементов на нечетных позициях не обнаружено")
    return list_cube_even_numbers_odd_position

    return list_cube_even_numbers_odd_position


tuple_whole_numbers = (1, 2, 3, 5, 7)
print("Кортеж целых чисел:", tuple_whole_numbers)

square_numbers(tuple_whole_numbers)
even_position_elements(tuple_whole_numbers)
cube_even_numbers_odd_position(tuple_whole_numbers)
