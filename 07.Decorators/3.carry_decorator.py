"""3. Каррирование. Преобразовать вызов функции с конечным количеством позиционных аргументов
f(a, b, c, d) в вызов вида f(a)(b)(c)(d), используя декоратор. Пример:
  @carry
  def foo(a, b):
        return a + b

   foo(1)(5)  # вернет 6
"""


