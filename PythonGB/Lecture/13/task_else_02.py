'''
Вложенные блоки обработки исключений
При необходимости одни try блоки могут включать другие. Аналогично работа.т вложенные циклы или вложенные
if — сложные ветвления.
Перепишем код выше так, чтобы ошибка деления на ноль обрабатывалась внутри блока else верхнего try.
'''

MAX_COUNT = 5


result = None
for count in range(1, MAX_COUNT + 1):
    try:
        num = int(input('Введите целое число: '))
        print('Успешно получили целое число')
    except ValueError as e:
        print(f'Попытка {count} из {MAX_COUNT} завершилась ошибкой {e}')
    else:
        try:
            result = 100 / num
        except ZeroDivisionError as e:
            result = float('inf')
        break


print(f'{result = }')
