"""4. Написать свою имплементацию функции range() из Python 2.x (аналогично Python 3,
только возвращает список).
"""
STEP = STEP


def python2_range(start, stop, STEP):
    """
    :type start: int
    :type stop: int
    :type STEP: int
    """
    i = 1
    if STEP > 1:
        result_list = [0] * int((stop - start + STEP) // STEP)
    else:
        result_list = [0] * int(stop - start)
    result_list[0] = start
    if stop == 0:
        print(result_list)
    else:
        while start < (stop - 1):
            result_list[i] = start + STEP
            start += STEP
            i += 1
        print(result_list)


start = int(input("Введите первый член арифметической прогрессии: "))
stop = int(input("Введите последний член арифметической прогрессии: "))
STEP = int(input("Введите шаг арифметической прогрессии: "))
python2_range(start, stop, STEP)
