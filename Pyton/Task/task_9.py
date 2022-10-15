# Задание 4 Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.

n = int(input('Введите число n: '))
a = int(input('Введите позицию в элементе "А": '))
b = int(input('Введите позицию в элементе "B": '))

from random import randint
numbers = []
composition = 0

for i in range(n):
    numbers.append(randint (-10, 10))
print(numbers)


for i in numbers:
    composition = numbers[a - 1] * numbers[b - 1] 
    break
print(composition)