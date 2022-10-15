#Задание 2 Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
#Пример:
#пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
"""
n = int(input('введите N число: '))

factorial = 1
for i in range(1, n + 1):
     factorial *= i
     print(factorial, end = " ")
print()
"""

# После через: MAP
n = int(input('введите N число: '))
lst = [i for i in range(1, n + 1)]

def foo(x):
     res = 1
     for i in range(1, x + 1):
          res *= i
     return res

print(list(map(foo, lst)))