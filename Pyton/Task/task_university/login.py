

import csv
import menu_teache_and_stydent as mt

file_teacher = "Pyton/Task/task_university/login/1A_class_teacher.txt"
file_stydent = 'Pyton/Task/task_university/login/1A_class_stydent.txt'


def login_menu():
    while True:   
        last_login = input('Для входа выберите нужное действие\n\n'
                            '"1" - Отправить запрос на регистрацию \n'
                            '"0" - Выйти\n\n'
                        
                            'Если Вы уже зарегистрированы, введите свой \n'
                            'Login: ')
        print()
        with open(file_teacher) as fp:
            reader_teach = csv.reader(fp, delimiter=";",)
        # next(reader, None)  # skip the headers
            data_read_teach = [row[0] for row in reader_teach]
            data_set_teach = set(data_read_teach)

        with open(file_stydent) as fp:
            reader_styd = csv.reader(fp, delimiter=";",)
        # next(reader, None)  # skip the headers
            data_read_styd = [row[0] for row in reader_styd]
            data_set_styd = set(data_read_styd)

        if last_login in data_set_teach:
            mt.print_menu_teacher()


        if last_login in data_set_styd:
            mt.print_menu_stydent()
    
        if last_login == '1': # запрос на регистрацию
            new_user()

        elif last_login == '0':
            print('Вы вышли из ситемы')
            break

        elif last_login != data_set_teach and data_read_styd:
            print("ВНИМАНИЕ!\nВы ввели несуществующий логин.\nПовторите попытку или отправьте заявку на регистрацию")

def new_user():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
    info.append(first_name)
    first_name = input('Введите адрес своей электронной почты: ')
    info.append(first_name)
    phone_number = ''
    valid = False
    while not valid:
        phone_number = input('Введите номер телефона: ')
        if len(phone_number) != 11:
            print('В номере телефона должно быть 11 цифр. Пример: 89898885585')
        else:
            phone_number = int(phone_number)
        valid = True
    info.append(phone_number)
    with open ('/Users/pavelpashkov/GB/Pyton/Task/task_university/new_user/new_user.txt', 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info[0]}\nИмя: {info[1]}\nАдрес электронной почты: {info[2]}\nНомер телефона: {info[3]}\n\n')
        print('\n\nЗапрос на регистрацию успешно отправлен. Ожидайте ответа на запрос в течение 3х рабочих дней\n\n')

