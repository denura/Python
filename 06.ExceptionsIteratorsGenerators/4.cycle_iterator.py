"""4. Написать функцию-генератор cycle которая бы возвращала циклический итератор."""


def cycle(iterator):
    """функция-генератор, которая возвращает циклический итератор"""
    li = []
    for element in iterator:
        li.append(element)
        yield element
    n = 0
    le = len(li)
    while True:
        yield li[n]
        n += 1
        if n >= le:
            n = 0
