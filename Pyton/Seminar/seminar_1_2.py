    ## СЕМИНАР 1. Знакомсвто с Pyton
    # Динамическая дипизация, значит:
# a = 5
#print(type(a)) # переманная сама орпеделяется int или str dooble 
#a = 'dsad'
#print(type(a))
# Ответ:
# <class 'int'>
# <class 'str'>

## ELIF(elif) - это условие которое проверяет если у нас первое условия было ложно. Идет с верху в низ

## Условный оператор - это алгоритмическая конструкция которая определяет ветвеление

# Обычное ветвеление:

# a = 5
# b = 15
# c = a * b
# print(c)

# Через условный оператор if :
# Сушествует два условный опертора:
# 1. Полный - Если что-то произошло (истина), то мы что-то делаем, а если нет то не чего не делаем
# 2. Не полный - если на улицу дождь одеваем рез ботинки если нет то трапочные

# # Например:
# a = 5
# b = 15
# c = a * b
# if a > 5: # если истина то это выполняем и остальное уже не проверяем
#     c = c * 2
# elif a > 9:# проверка второго условия (если разные блоки)
#     c = c * 4
# elif a > 15:
#     c = c * 5
# else: # иначе выполняется это действие 
#     c = c * 3
## если вместо elif будут if то он проверитт первый даже если это истена он всеравно сделаем проверка
# если условия только одно истина то лучше не испольтзовать

# print(c)

## ЦЫКЛЫ

# Циклов два вида Whelt and For 
# whele - пока что-то истина мы что-то делаем (если не знаем сколько раз нужно выполнить )
# for - итерационный (Если мы заранее знаем сколько итераций нам нужно выполнить)

# n = int(input()) # кол-во выполненых раз цикла

# sum_ = 0
# for i in range(n): # range - кол-во операций, i до n
#     number = int(input()) # вводит пользователь 
#     sum_ += number

# print(sum_)

# если прользователь не известное кол-во, будет вводить пока не введет ноль
# ноль это будет сигнал для выхода, и мы не знаем когда он введет ноль

# number = int(input()) # кол-во выполненых раз цикла

# cnt = 0 # создаем переменную каунт(счетчик)
# sum_ = 0
# while number != 0: #меняем, пока n != 0
#     sum_ += number # сумируем число
#     cnt += 1 # добавляем к счетчику который у нас есть, потом спрашиваю новое число
#     number = int(input())     
# print(sum_)

# ** Range - он знает какое числое ему выдать, знает когда оставноится и знает шаг который нужно прибавить к предущему число
# например:
# from __future__ import barry_as_FLUFL


# for i in range(2, 15, 3): # i примет значение от 2 до 15 с шагом 3
#     print(i)
# # ответ: 
#2
#5
#8
#11
#14
# если указать 5ку for i in range(5) то будет ровно 5 чисел от 0 до 4

# цикл for говорит сколько раз можем сделать
# whille пока условия истино выполняем цикл, как будет лож не выполняем

# ДВа ключевых слова:
# break - завершает цикл
# continue - переходит к след операции 
# # 1. пример: 
# for i in range(10): 
#     print(i)
#     if i == 7: # например напишем условие, если равно 7ми то break
#         break # закончим на 7 ми

# 2. пример: 
# for i in range(10): 
#     print(i)
#     if i == 7:
#             continue # выводит результат без 7 числа если равно (т.к. пропускает эту строчку и проходит ниже)
#     print(i)

# у цикла фор есть условные операторы
# from re import X
# from unicodedata import name


# for i in range(10): 
#     if i == 7:
#         break # выводит результат без 7 числа если равно (т.к. пропускает эту строчку и проходит ниже)
#     print(i)
# else: # пишется только если выполняется все штатно с break не штатно т.к. на 7 завершается
#     print('цикл завершился штатно')

# ## ФУНКЦИЯ
# def f():
#     print('Как вас зовут')
#     name = input()
#     print(f'Здравствуйте, {name}')

# f() # вызоываем и выполняются эти строчки. Обычно используют когда что-то надо высчитать:
# Пример:
# def f_x(x): # можно записать так def f_x(x, y, z)
#     return x**2 + 15 * x - 92 # возвращает/ значение которое подставится вместо этого выражения 
# y = f_x(35)
# print(y)

# # СПИСОК
# def f(a, b):
#     return len(a) # возращаем длину списка a

# print(f([1, 2, 3, 4, 5], [333])) # ответ 5 т.к. возратили длину списка a первого

# split - это разделение строки
# dir - можно посмотреть все методы функции
str_ = 'wqewq'
print(dir(str_))
a = [ 'capitalize', # делает первую буква заглавной остальные строчные
'casefold', 
'center', 
'count',  # считает сколько подстрока входит под нее
'encode', 
'endswith', # заканчивается ли подстрока
'expandtabs', 
'find', # найти идекс вхождения какой-то подстраки
'format', 
'format_map', 
'index', 
'isalnum', 
'isalpha', 
'isascii', 
'isdecimal', 
'isdigit', # стррока только из цифр
'isidentifier', 
'islower', 
'isnumeric', 
'isprintable', 
'isspace', 
'istitle', 
'isupper', 
'join', # склеить через эту подсрочку  
'ljust', 
'lower', 
'lstrip', 
'maketrans', 
'partition', 
'removeprefix', 
'removesuffix', 
'replace', 
'rfind', # найти справа
'rindex', 
'rjust', 
'rpartition', 
'rsplit', 
'rstrip', 
'split', 
'splitlines', 
'startswith', 
'strip', 
'swapcase', # все заглавные сделать строчными и наоборот 
'title', 
'translate', 
'upper', 
'zfill']

# как пишеося
#print(help(str.isalpha))

print(str_.isdigit())