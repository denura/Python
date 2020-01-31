"""1. Написать несколько функций, которые в качестве единственного аргумента принимают список (или
кортеж) целых чисел.
- первая функция должна вернуть квадраты элементов коллекции;
- вторая функция должна вернуть только элементы на четных позициях;
- третья функция возвращает кубы четных элементов на нечетных позициях.
"""

def square_numbers(input_list_whole_numbers):
    iterator = 0
    for number in input_list_whole_numbers:
        input_list_whole_numbers[iterator] = number * number
        iterator += 1
    print("Квадраты элементов коллекции:", input_list_whole_numbers)


input_list_whole_numbers = input("Введите список целых чисел (разделитель - пробел): ").split(" ")
square_numbers(input_list_whole_numbers)
