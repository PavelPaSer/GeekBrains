     # Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = int(input('Введите число x '))
y = int(input('Введите число y '))
z = int(input('Введите число z ')) 

a = x * y * z
b = x + y + z

if a > 0:
     a = 0
elif a < 1:
     a = 1
if b > 0:
     b = 1
elif b < 1:
     b = 1

if a == b:
     print('Истинна')
elif a != b:
     print('Ложь')


## Пробовал решить другим способом, который вы озвучили на семинаре, но не могу понять что сделал не так. 
# подскажите что сделал не так, спасибо

#x = int(input('Введите число x '))
#y = int(input('Введите число y '))
#z = int(input('Введите число z '))

#NumberA= not x or y or z
#NumberB = not x and y and z
#result = NumberA == NumberB

#if result:
#     print('Истинна')
#else:
#     print('Ложь')