"""2. Написать функцию, которая принимает произвольное количество любых аргументов.
    Аргументами могут быть вложенные списки и кортежи, содержащие числа и другие списки и кортежи.
    Пример вызова функции: foo(1, 2, [3, 4, (5, 6, 0)], a=(10, 11), b=(3, 4, [5, 6, [7, 8], []]))
    Функция должна вернуть произведение и сумму всех ненулевых элементов вложенных чисел.
    Возможны циклические ссылки в аргументах. Пример такого аргумента: a = [1, 2, 3]; a.append(a)
    При обнаружении циклической ссылки нужно сообщить пользователю и вернуть None.
    """


def multiplication_and_sum(*arguments_lists):
    """В Python можно передать переменное количество аргументов двумя способами:
    *args для неименованных аргументов;
    **kwargs для именованных аргументов.
    """
    sum_int = 0
    mul_int = 1
    sum_other = 0
    mul_other = 1
    for argument in arguments_lists:
        if isinstance(argument, int):
            sum_int += argument
            mul_int *= argument
            print(sum_int)
            print(mul_int)
        else:
            while not isinstance(argument, int):
                for arg in argument:
                    sum_other += argument
                    mul_other *= argument
                    print(sum_other)
                    print(mul_other)


multiplication_and_sum(1, 2, [3, 4, (5, 6, 0)], (10, 11), (3, 4, [5, 6, [7, 8], []]))
