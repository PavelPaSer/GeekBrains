# Задача №22: Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
#   [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
# Как было до:

x = [2, 3, 5, 9, 3]
"""
Как было до: 

x = [2, 3, 5, 9, 3]
print(x)
sum = 0
for i in range(1, len(x), 2):
         sum += x[i] 
print(f"Сумма на нечётных позициях равна {b}")   
"""
# После через: LIST COMPREHENSION

b = [sum((x[i]) for i in range(1, len(x), 2))]
print(f"Сумма на нечётных позициях равна {b}")