"""6. Напишите шаблон регулярного выражения, который соответствует вопросительным предложениям,
в которых одно слово (более 2 символов) повторяется 4 или более раз."""


import re

REG_EXP = re.compile('(\w{3,}\s?){4,}[?]')
test_str = 'test test test test test? test test test test test?'
iterator = re.finditer(REG_EXP, test_str)
for match in iterator:
    print('Совпадение найдено в позициях:', match.span())
