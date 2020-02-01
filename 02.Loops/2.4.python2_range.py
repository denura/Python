"""4. Написать свою имплементацию функции range() из Python 2.x (аналогично Python 3,
только возвращает список).
"""


def python2_range(start, stop, step):
    """
    :type start: int
    :type stop: int
    :type step: int
    """
    iterator = 0
    result_list = []
    if step > 0:
        while start + (iterator * step) < stop:
            result_list.append(start + iterator * step)
            iterator += 1
    elif step < 0:
        while start + (iterator * step) > stop:
            result_list.append(start + iterator * step)
            iterator += 1
    else:
        print("Ошибка: шаг арифметической прогрессии не может быть нулевым!")
    print("Арифметическая прогрессия:", result_list)


start = int(input("Введите первый член арифметической прогрессии: "))
stop = int(input("Введите последний член арифметической прогрессии: "))
step = int(input("Введите шаг арифметической прогрессии: "))
python2_range(start, stop, step)
