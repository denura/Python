"""
5.1
"""
class ComplexClass(object):
    def metod1(self, x):
        pass

    def __init__(self, attr1):
        self.attr1 = attr1

    def __add__(self, other):
        return "{}".format(other)

a = ComplexClass(1)
print(a + 1)
