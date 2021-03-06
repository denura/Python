"""4. Напишите шаблон регулярного выражения, который соответствовал бы следующему формату времени:
YYYY-MM-DDThh:mm:ss±hh:mm (ISO формат).
Пример:
2005-08-09T18:31:42+03:30
2005-08-09T18:31:42-03:30
"""


import re

REG_EXP = re.compile('^\d{4}(-\d{2}){2}T\d{2}(:\d{2}){2}[-+]\d{2}:\d{2}$')
SAMPLE1 = '2005-08-09T18:31:42+03:30'
SAMPLE2 = '2005-08-09T18:31:42-03:30'
print(re.match(REG_EXP, SAMPLE1), '\n', re.match(REG_EXP, SAMPLE2))
