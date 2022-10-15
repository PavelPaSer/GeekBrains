# 2 Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# *Пример*

# - при N=236     ->        [2, 2, 59]

number = int(input("Введите число N: "))
while number > 1:
    for i in range(2, number + 1):
        if(number % i == 0):
            number //= i
            print(i)
            break




# question = int(input("Введите число N: "))
# answer = []
# while question > 1:
#     for i in range(2, question + 1):
#         if question % i == 0:
#             answer.append(i)
#             question = int(question / i)
#             break
# print(answer)