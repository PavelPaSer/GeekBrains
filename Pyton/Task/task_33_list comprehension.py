# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму,
# округлённую до трёх знаков после точки.
# Пример:
# Для n = 6 -> 14.072
"""
number = int(input(' '))
result = 0
for i in range(1, number + 1):
    result += ((1 + 1 / i) ** i)
print(round(result, 3))
"""

# После через: LIST COMPREHENSION
number = int(input(' '))
print(round(sum([(1 + 1 / i) ** i for i in range(1, number + 1)]), 3))
