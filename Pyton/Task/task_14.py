# Задача №25: Напишите программу, которая будет преобразовывать десятичное число в двоичное. Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

number = int(input('Введите число: '))
 
numberb = ' '
 
while number > 0:
    numberb = str(number % 2) + numberb
    number = number // 2
 
print(numberb)

# print(bin(number)) 