
# Практика 
"""
1. Напишите программу вычисления арифметического выражения заданного строкой. 
Используйте операции +,-,/,*. приоритет операций стандартный. 
*Пример:* 
2+2 => 4; 
1+2*3 => 7; 
1-2*3 => -5;

2 Добавьте возможность использования скобок, меняющих приоритет операций.
*Пример:* 
1+2*3 => 7; 
(1+2)*3 => 9;


3. Дана последовательность чисел. Получить список уникальных элементов заданной последовательности.

[1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]
"""
# str1 = '2+2'
# neg = False
# lst = []
# # for i, char in enumerate(str1):
# #     if char == '+' or char == '-' or char == '*':
# #         if neg:
# #             lst.append('-' + str1[i:])
# #         else:
# #             lst.append(str1[:i])
# for i, char in enumerate(str1):
#     lst.append(char)
# print(lst) # ['2', '+', '2']

# lst = []

# # for i, char in enumerate(str2):
# #     lst.append(char)

# print(lst)
# lst_res = []
# temp = 0
# for i, char in enumerate(lst):
#     if char == '*':
#         temp = lst_res.append(int(lst[i-1]) * int(lst[i+1]))
#     if char == '+':
#         lst_res.append(int(lst[i-1]) + temp)

# print(lst_res)
# result = 0
# for i in range(len(lst_res)):
#     result += lst_res[i]

# print(result)

# lst = []
# str2 = '1+2*3'
# for i, char in enumerate(str2):
#     lst.append(char)

# print(lst)
# lst_res = []
# temp = 0
# for i, char in enumerate(lst):
#     if char == '*':
#         temp = lst_res.append(int(lst[i-1]) * int(lst[i+1]))
#     if char == '+':
#         lst_res.append(int(lst[i-1]) + temp)

# print(lst_res)
# result = 0
# for i in range(len(lst_res)):
#     result += lst_res[i]

# print(result)

# ВСЕ НЕ ПРАВИЛЬНО
# РЕШЕНИЕ ПРЕДПОДАВАТЕЛЯ

# как сделать функцию если будут () 
s = '10*55+21*2'

lst = []
last = -1
for i in range(len(s)):
    if s[i] in {'+', '-', '*', '/'}:
      lst.append(s[last + 1:i])
      lst.append(s[i])
      last = i
lst.append(s[last + 1])
print(lst)
# ['10', '*', '55', '+', '21', '*', '2'] 
# s = lst 



lst_res = [int(s[0])]
i = 1
while i < len(s):  # говорим пока i меньше чем длина нашего s
    if s[i] == '+':  # если мы встречаем плюс 
        lst_res.append(int(s[i + 1])) # то мы след за плюсом добавляем 
    # если мы встрелии минус 
    elif s[i] == '-':  # 
        lst_res.append(-int(s[i + 1])) 
    elif s[i] == '*':  # 
        lst_res[-1] = lst_res[-1] * int(s[i + 1]) # посдедний элемент мы заменяем на произведение последнего на тот который у нас сейчас
    elif s[i] == '/':  # 
        lst_res[-1] = int(lst_res[-1] / s[i + 1])
    i += 2 # слующие число пропускает 

print(lst_res)
print(sum(lst_res))


# РЕШЕНИЕ ДРУГОЙ ГРУППЫ
"""
question = "1 - 2 * 3"
question = question.split()
print(question)

def calculator(question):
answer = []
n = 0
for i in range(len(question)):
if n > i:
continue
if question[i].isdigit():
answer.append(question[i])
elif question[i] == "+":
continue
elif question[i] == "-":
n += 1
answer.append(-int((question[n])))
elif question[i] == "*":
n += 1
temp = int(answer.pop()) * int(question[n])
answer.append(temp)
elif question[i] == "/":
n += 1
temp = int(answer.pop()) / int(question[n])
answer.append(temp)
n += 1

final_answer = 0
for i in range(len(answer)):
final_answer += int(answer[i])
return final_answer
"""