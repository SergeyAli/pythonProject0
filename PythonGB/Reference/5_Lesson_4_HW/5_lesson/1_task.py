# ------------------------------------------- 1 -----------------------------
# Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом '/'.
#
# Сформируйте словарь, где:
#     второе и третье число являются ключами
#     первое число является значением для первого ключа
#     четвертое и все возможные последующие числа
#     хранятся в кортеже как значения второго ключа


one, two, three, *other = input('Какой текст преобразовать? ').split('/')
result = {
    int(two): int(one),
    int(three): tuple(map(int, other)),
}

print(f'{result = }')
