# Методы startswith и endswith
# Метод startswith проверяет начинается ли строка с заданной подстроки. Метод
# возвращает истину или ложь. Метод endswith проверяет окончание строки
# переданной в качестве аргумента подстрокой.

text = 'Однажды в студёную зимнюю пору'
print(text.startswith('Однажды'))
print(text.endswith('зимнюю', 0, -5))

# Оба метода помимо подстроки могут принимать параметры start и stop. В этом
# случае проверка начала либо конца будет проводиться в указанном диапазоне.