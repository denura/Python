"""1. Напишите итератор EvenIterator, который позволяет получить из списка все элементы, стоящие на
чётных индексах. """


class EvenIterator(object):
    """позволяет получить из списка все элементы, стоящие на чётных индексах"""
    def __init__(self, INPUT_LIST):
        self.INPUT_LIST = INPUT_LIST
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < len(INPUT_LIST):
            if self.counter % 2:
                print(INPUT_LIST[self.counter])
            self.counter += 1
            return 1


INPUT_LIST = list('список')
EvenIterator(INPUT_LIST)
