"""6. Напишите шаблон регулярного выражения, который соответствует вопросительным предложениям,
в которых одно слово (более 2 символов) повторяется 4 или более раз."""


import re

REG_EXP = re.compile('(\w{3,}\s?){4,}[?]')
TEST_STR = 'test test test test test? test test test test test?'
ITERATOR = re.finditer(REG_EXP, TEST_STR)
for match in ITERATOR:
    print('Совпадение найдено в позициях:', match.span())
