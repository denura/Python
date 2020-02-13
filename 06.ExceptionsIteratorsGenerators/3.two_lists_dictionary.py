"""3. Есть два списка разной длины, в одном ключи, в другом значения. Составить словарь.
Для ключей, для которых нет значений использовать None в качестве значения. Значения, для которых
нет ключей игнорировать."""

from itertools import zip_longest

list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [1, 2, 3]

print({key: value for key, value in zip_longest(list1, list2) if key is not None})
