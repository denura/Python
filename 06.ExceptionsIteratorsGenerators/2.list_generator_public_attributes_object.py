"""2. Написать генератор списка для получения списка всех публичных атрибутов объекта"""


def foo():
    """nothing"""
    return 0


print([arg for arg in dir(foo) if not arg.startswith('_')])
