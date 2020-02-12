"""Написать базовый класс Observable, который бы позволял наследникам:
при передаче **kwargs заносить соответствующие значения как атрибуты
сделать так, чтобы при print отображались все публичные атрибуты
>>> class X(Observable):
...     pass
>>> x = X(foo=1, bar=5, _bazz=12, name='Amok', props=('One', 'two'))
>>> print x
X(bar=5, foo=1, name='Amok', props=('One', 'two'))
>>> x.foo
1
>>> x.name
'Amok'
>>> x._bazz
12
"""