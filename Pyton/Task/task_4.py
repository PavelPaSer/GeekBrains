# Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).

number = int(input('Введите номер четверти: '))
if number == 1:
    print('(Х > 0; Y > 0)')
elif number == 2:
    print('(Х < 0; Y > 0)')
elif number == 3:
    print('(Х < 0; Y < 0)')
elif number == 4:
    print('(Х > 0; Y < 0)')
elif 0 < number > 4:
     print('Введите четверть от 1 до 4')
     