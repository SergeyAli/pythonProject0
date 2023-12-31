# ------------------------------------------- 3 -----------------------------
# Напишите программу, которая получает целое число
# и возвращает его двоичное, восьмеричное строковое представление.
# Функции bin и oct используйте для проверки своего результата.

# *Дополнительно
# Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
# Избегайте магических чисел
# Добавьте аннотацию типов где это возможно

BIN: int = 2
OCT: int = 8

num: int = int(input('Введите число: '))

for div in [BIN, OCT]:
    test_num: int = num
    result: str = ''
    while test_num > 0:
        result = str(test_num % div) + result
        test_num //= div
    print(f'For {div} {result = }')

print(f'{bin(num) = :>15}\n{oct(num) = :>15}')

