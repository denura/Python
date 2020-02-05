"""5. В этом задании можно отступить от PEP8.
    Цель - выполнить задание за минимальное возможное количество символов в функции
    (если потребовался импорт отдельных модулей для функции, то инструкции импорта тоже считаются).
    Напишите функцию, которая будет принимать ввод пользовательской строки. В строке 1 или более
    отрицательных/положительных чисел.
    Функция должна вернуть ближайшее к нулю значение.
    пример foo() -> пользователь ввел '1 2 -0.5 0.75 22' -> функция доджна вернуть -0.5
    """


def near_zero(input_string):
    near_zero_element = abs(input_string[0])
    for element in input_string:
        abs_element = abs(element)
        if near_zero_element > abs_element:
            near_zero_element = abs_element

    print(near_zero_element)
    return near_zero_element

# input_string = input("Введите строку чисел:")
input_string = (1, 2, -0.5, 0.75, 22)
near_zero(input_string)
