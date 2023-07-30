'''
Классы
Вы уже знаете, что в Python есть несколько областей видимости. Например
переменные объявленные внутри функции, являются локальными переменными
функции. Так же вы помните о модулях, которые могут хранить в себе переменные и
функции. Для обращение к ним используется импорт и точечная нотация:
'''

import random
import supermodule

result1 = random.randint(1, 10)
result2 = supermodule.randint(42)
print(f'{result1 = }')
print(f'{result2 = }')
