"""Задание 1. Разработать класс Complex, которые бы описывал комплексные числа, позволял их
складывать, вычитать, умножать, делить и получать модуль. Вывод действительной и мнимой частей
должен быть с точностью до двух знаков после запятой. На вход: действительная и мнимая часть числа,
разделенная пробелом.
Sample Input: 2 1
5 6
На выходе: для двух комплексных чисел вывод должен быть в следующей последовательности в отдельных
строках: C + D
C – D
C * D
C/D
mod(C)
mod(D)
Sample Output: 7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i
P.S. Не забудьте про перегрузку магических методов, пожалуйста"""
class ComplexClass(object):
    def metod1(self, x):
        pass

    def __init__(self, C, D):
        self.C = C
        self.D = D

    def __add__(self, other):
        return C[0] + D[0]

    def __sub__(self, other):
        return

    def __mul__(self, other):
        return

    def __div__(self, other):
        return

    def __abs__(self):
        return


# a = ComplexClass(1)
# print(a + 1)
C = ComplexClass(2, 1)
D = ComplexClass(5, 6)
print(C + D)
print(C - D)
print(C * D)
print(C / D)
print(abs(C))
print(abs(D))
# C = input("Введите действительную и мнимую части первого числа, разделенные пробелом: ")
# D = input("Введите действительную и мнимую части второо числа, разделенные пробелом: ")
