"""1.Напишите параметризованный декоратор, который считает и выводит при каждом вызове среднее
время работы функции за n последних вызовов.  Время выводить в миллисекундах.
  Пример использования:
  @average_time(n=2)
  def foo(a):
      sleep(a)
      return a
  foo(3) # вернет 3 и выведет сообщение "Среднее время работы: 3000 мс."
  foo(7) # вернет 7 и выведет сообщение "Среднее время работы: 5000 мс."
  foo(1) # вернет 1 и выведет сообщение "Среднее время работы: 4000 мс."
"""


