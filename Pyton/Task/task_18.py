# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# *Пример*

# - при [1, 1, 2, 3, 3, 4, 1, 5, 7, 8, 8, 7, 9]     ->        [2, 4, 5, 9]

lst = list(map(int, input("Введите числа через пробел от 1 до 9:\n").split()))
new_list = []
for i in range(len(lst)):
    for j in range(len(lst)):
        if i != j and lst[i] == lst[j]:
            break
    else:
        new_list.append(lst[i])
print(new_list)