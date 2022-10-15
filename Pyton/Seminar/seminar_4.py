
# ТЕМА ИЗУЧЕНИЯ ТИПОВ ДАННЫХ ФУНКЦИЙ И МОДУЛЕЙ

"""
fib = [0, 1]

for i in range(10 - 1):
    fib.append(fib[-1] + fib[-2]) # предыдущий элемент плюс предыдущий
print(fib)

neg = [0, 1]

for i in range(10):
   neg.append(neg[-2] - neg[-1])  # cоздали отрицальные 

neg.reverse()

print(neg + fib[1:]) # чтоб не повторялся нолик можем начать с [1:]"""

""" 
def My_List_Mix(Arg_in):
#Метод перемешивающий список
Temp_arg_in = []
for i in range(0, len(Arg_in) ) :
Temp_arg_in.append(None)

for i in range(0, len(Arg_in) ) :
while True:
Rand_int=random.randint(0,len(Arg_in) - 1)
if Temp_arg_in[Rand_int] == None:
Temp_arg_in[Rand_int] = Arg_in[i]
break
return Temp_arg_in 
"""

"""
lst = []

for i in range(22):
    lst.append(str(i)) # в список мы добавляем стр i 
lst.append('🥺') # так же добавляем если нужно
s = ', '.join(lst) # 
print(s) 
"""

# РАБОТА С ФАЙЛАМИ
""" 
# open('new_file', 'at', encoding='utf-8') 
# r - открытие на чтение w - открыватие на записаь с перезаписью a - открытие на запись с дополнением (дозаписываем) 
# если файл открыт на запись то его читать не сможем
# если открыт на чтение писать в него не сможем
# в какой кодировке работает encoding 

open('new_file33', 'w', encoding='utf-8') # создадим файл на запись
# для того что начать с ним рабоать, его нужно передать куда-то
f = open('new_file33', 'w', encoding='utf-8')
f.write('sdasd') # запись
# после надо закрыть, если поставить на чтение то закрывать не обязательно
f.close()
# изначально работает с копией, после клос все переходит в оригинал
"""

# Можно сократить 
"""
with open('new_file33', 'a', encoding='utf-8') as f:
    f.write('qwew\n')
print(11 / 0)
# мы что-то делаем, результат действия сохраняем в переменную f 
# затем с ней работаем
# как только блок закончился, он его автоматом закроет
"""

# ЧТЕНИЕ ФАЙЛОВ
"""
with open('new_file', 'r', encoding='utf-8') as f:
    f.write('qwew\n')
# print(1, f.read()) # 1 хотим прочитать первый раз
# print(2, f.read()) # 2 раз прочитать пробуем, но тут не чего не будет. т.к. можно один раз считать
print(2, f.readLine()) # читает перву строку
print(2, f.readLines()) # читает все строки
"""

# ЛУЧШЕ СНАЧАЛА ПРОЧИТАТЬ ПОТОМ ПОМЕНЯТЬ
"""
with open('new_file', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print(lines)
lines[3] = 'Hello!!!\n'# говорим что лайнс трейтий это теперь строчка хеллоу

with open('new_file', 'w', encoding='utf-8') as f: # теперь делаем перезапись
    for line in lines: # каждый элемент в списке лайне, берется каждый элемент и поспенно сохраняется и мы его используем
        f.write(line) # мой лайн
"""

# РЕКУРСИЯ 
# МЫ ситуацию в котороет повторяется эта ситуация
# это функция которая вызывает сама себя
# у рекурсии должен быть выход
"""
def rec(x):
    if x < 4:
        print(x)
        rec(x+1)
        print(x)
rec(1)

Ответ: 
1
2
3
3
2
1
"""
# пример на факториал
"""
def fact(n):
    if n < 0: # меньше нуля 
       return # будет какая-то ошибка
    elif n == 1: # иначе,
        return 1 # возращаем единицу 
    return fact(n - 1) * n  # в противном случае мы возращаем факториал n - 1 умноженное на n

print(fact(5))
"""

# Пример фибоначи. Минус применения рекурсии:
"""
def fib(n):
    if n <= 2: # меньше или нулевое число
       return 1# мы возращаем один
    
    return fib(n - 1) + fib(n - 2)

print(fib(25)) # при больних числах очень долго будет, т.к. обход рекурсивный и дерово растет (повтороние больших операций)
"""
# Можно использовать КЭШирование - это способ сохранения предыдуших вызовов 

"""
mem = {1: 1, 2: 1} # для первого числа это один для второго это один
def fib(n):
    if n not in mem: # если n не разу не считал
        mem[n] = fib(n - 1) + fib(n - 2) # то я его высчитывая всего один раз
    return mem[n]# когда посчитаем вернем его  
print(fib(405)) # можно считать большие цыфры. ЧТоб не просчитывали все заново мы используем кэширование и больше не использую
"""