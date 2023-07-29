# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [3, 'Hello', 7.2, 7.2, 1, 1, 'Hello', 1, 9]

print(f'Исходный список:\n{my_list}')

print(f'\nРезультирующей списк, без дубликатов:\n{list(set(my_list))}')
