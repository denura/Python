"""3. Написать функцию вычисления факториала числа"""


def calc_factorial(initial_val):
    """
    :type initial_val: int
    """
    factorial = 1
    if initial_val == 0:
        print("%.d! = %d" % (initial_val, factorial))
    else:
        while initial_val > 1:
            factorial *= initial_val
            initial_val -= 1
        print("Факториал введенного числа = ", factorial)


initial_val = int(input("Введите число для вычисления его факториала: "))
calc_factorial(initial_val)
