'''
Создайте программу для игры с конфетами человек против человека.
Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
Все конфеты оппонента достаются сделавшему последний ход. 
Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
a) Добавьте игру против бота
b) Подумайте как наделить бота ""интеллектом""
'''
import random
import time
print('Приглашаю Вас поиграть в увлекательную игру КОНФИТИ.\n'
    'Прежде чем начать ознакомтесь с правилами игры:')
time.sleep(3)
text_rules = ('\n'
                'Я даю Вам 2021 конфету, вы берете их поочереди,\n'
                'причем, за один раз можно взять не больше 28 конфет.\n'
                'Выигрывает тот, кто последним ходом заберет все конфеты.\n'
                'Ну что начнем?')
print(text_rules)
time.sleep(1)
player_1 = input('\n Игрок № 1. Ваше Имя: ')
player_2 = input('\n Игрок № 2. Ваше Имя: ')
print('\nДля начала опеределим кто первый начнет игру.\n')
time.sleep(2)

x = random.randint(1, 2)
if x == 1:
    vin = player_1
    no_vin = player_2
else:
    vin = player_2
    no_vin = player_1
print(f'{vin} ты ходишь первым!')
time.sleep(3)

def player_vs_player():
    total_ = 2021
    max_ = 28
    count = 0
    while total_ > 0:
        if count == 0:
            step = int(input(f'\n {vin} Введите число: '))
            if step > total_ or step > max_:
                step = int(input(
                    f'\nМожно взять не больше {max_}, попробуй еще раз: '))
            total_  = total_ - step
        if total_ > 0:
            print(f'\nОсталось конфет: {total_}')
            count = 1
        else:
            print('Все кончились конфетки')

        if count == 1:
            step = int(input(f'\n{no_vin} Введите число = '))
            if step > total_ or step > max_:
                step = int(input(
                    f'\nМожно взять не больше {max_}, попробуй еще раз: '))
            total_  = total_ - step
        if total_ > 0:
            print(f'\nОсталось конфет: {total_}')
            count = 0
        else:
            print('Все кончились конфетки')

    if count == 1:
        print(f'{vin} ПОБЕДИЛ')
    if count == 0:
        print(f'{vin} ПОБЕДИЛ')

player_vs_player()
