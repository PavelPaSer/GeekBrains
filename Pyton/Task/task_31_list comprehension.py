# Задание 31 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11
"""
Как было до: 
# n = input("введите число: ")
# sum = 0

# for s in n:
#     if s.isdigit():
#         sum += int(s)
        
# print(sum)
"""
# После через: LIST COMPREHENSION

n = input("введите число: ")
res = sum([int(s) for s in str(n) if s.isdigit()])
print(f"Cумма цыфры: {res} ")