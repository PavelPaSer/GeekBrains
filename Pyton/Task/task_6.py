# Задание 1 Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

n = input("введите число: ")
sum = 0

for s in n:
    if s.isdigit():
        sum += int(s)
        
print(sum)

# n = 0,56
# res = sum([int(s) for s in str(n) if s.isdigit()])
# print(f"Cумма цыфры: {res} ")
