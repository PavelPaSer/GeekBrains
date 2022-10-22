
import datetime as DT
import time

def print_menu_stydent(): # меню ученик
    while True:
        print()
        print('Выберите нужный пункт меню: ')
        menu = input(('1 Расписание\n'
                  '2 Домашнeе задание\n'
                  '3 Оценки\n\n'
                  '0 Назад\n'
                  'Введите пункт меню: '))
        if menu == '1':
            time.sleep(1)
            data_schedule()
        if menu == '2':
            time.sleep(1)
            data_dom_zadania()
        if menu == '3':
            time.sleep(1)
            data_rating()
        if menu == '0':
            break 



def print_menu_teacher(): # меню учитель
    while True:
        print()
        print('Выберите нужный пункт меню: ')
        menu = input(('1 Расписание\n'
                  '2 Добавить домашнeе задание\n'
                  '3 Посмотреть домашнeе задание\n'
                  '4 Добавить оценки\n'
                  '5 Просмотр оценок\n'
                  '6 Данные студентов\n\n'
                  '0 Назад\n'
                  'Введите пункт меню: '))
        if menu == '1':
            time.sleep(1)
            data_schedule()
        if menu == '2':
            time.sleep(1)
            lesson_add()
        if menu == '3':
            time.sleep(1)
            data_dom_zadania()
        if menu == '4':
            time.sleep(1)
            rating_add()
        if menu == '5':
            time.sleep(1)
            data_rating()
        if menu == '6':
            time.sleep(1)
            data_stydent()
        if menu == '0':
            break 



def data_schedule(): # рассписание просмотр  
    print()  
    with open('/Users/pavelpashkov/GB/Pyton/Task/task_university/schedule/schedule.txt', "r", encoding="utf-8") as f:
        res = f.read()
    print()
    print(res)

def lesson_add(): #добавлять дом. задание
    print('\nВведите домашнее задание')
    info = []
    description = input('Введите название предмета: ')
    info.append(description)
    last_name = input('Учитель: ')
    info.append(last_name)
    phone_number = input('Домашнее задание')
    info.append(phone_number)
    first_name = input('Введите дату задания(dd.mm.yyyy):\n')
    vypusk = DT.datetime.strptime(first_name, '%d.%m.%Y').date() 
    info.append(vypusk)   
    with open ('/Users/pavelpashkov/GB/Pyton/Task/task_university/rating/lesson_rating.txt', 'a', encoding = 'utf-8') as data:
        data.write(f'Предмет: {info[0]}\Учитель: {info[1]}\nДом. задание: {info[2]}\nДата назначения задания: {info[3]}\n\n')

def data_dom_zadania(): # прочитать дом. задание
    print()
    with open('/Users/pavelpashkov/GB/Pyton/Task/task_university/dom_zadania/task_home.txt', "r", encoding="utf-8") as f:
        res = f.read()
    print()
    print("Домшнее задание: ")
    print(res)

def rating_add(): # добавлять оценки учеников
    print('\nВведите данные для оценки учеников')
    info = []
    description = input('Название урока: ')
    info.append(description)
    last_name = input('Учитель: ')
    info.append(last_name)
    first_name = input('Введите Фамилию Имя ученика: ')
    info.append(first_name)
    phone_number = input('Введите оценку от 1 до 5: ')
    info.append(phone_number)
    first_name = input('Введите дату оценки(dd.mm.yyyy):\n')
    vypusk = DT.datetime.strptime(first_name, '%d.%m.%Y').date() 
    info.append(vypusk)   
    with open ('/Users/pavelpashkov/GB/Pyton/Task/task_university/rating/lesson_rating.txt', 'a', encoding = 'utf-8') as data:
        data.write(f'Название урока: {info[0]}\nУчитель: {info[1]}\nФамилия Имя ученика: {info[2]}\nОценка: {info[3]}\nДата оценки: {info[4]}\n\n')

    
def data_rating(): # смотреть оценки
    print()
    with open('/Users/pavelpashkov/GB/Pyton/Task/task_university/rating/lesson_rating.txt', "r", encoding="utf-8") as f:
        res = f.read()
    print()
    print("Оценки учеников: ")
    print(res)

def data_stydent(): # смотреть данные учеников
    print()
    with open('/Users/pavelpashkov/GB/Pyton/Task/task_university/login/1A_class_stydent.txt', "r", encoding="utf-8") as f:
        res = f.read()
    print()
    print("Данные учеников: ")
    print(res)

# def menu_input():
#     while True:
#         time.sleep(1)
#         menu = input(('1 - Главное меню\n'
#                       '0 - Выход\n'

#                   '\nВыберите нужный пункт меню: '))
#         if menu == '1':
#             print_menu_teacher()
#         if menu == '0':
#             print('Вы вышли из ситемы')
#             break