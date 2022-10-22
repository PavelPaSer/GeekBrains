"""
Создать телефонный справочник с возможностью импорта и экспорта данных в нескольких форматах. 
Программа должна уметь импортировать записи из файла, который сама экспортировала.
под форматами понимаем структуру файлов, например:
в файле на одной строке хранится одна часть записи, пустая строка - разделитель
Обязательные пункты меню: 
1 Просмотр записей (ВЫПОНИЛ с выбором форматом для просмотра файла)
2 Добавление записи (ВЫПОЛНИЛ с выбором форматом сохранения файла)
3 Экспорт (ВЫПОЛНИЛ с выбором форматом выбора файла)
4 Импорт (НЕ ВЫПОЛНИЛ)
5 Выход из программы (ВЫПОЛНИЛ)
"""


MAIN_FILENAME = '/Users/pavelpashkov/GB/Pyton/Task/task_Telefon_info/list.txt'
MAIN_FILENAME_2 = '/Users/pavelpashkov/GB/Pyton/Task/task_Telefon_info/list.csv'
import time


# МОДУЛЬ ИНТЕРФЕЙСА 
def print_menu():
    print('Введите действие(от 1 до 5): ')
    time.sleep(1)
    print('1. Показать контакты')
    print('2. Добавить новый контакт')
    print('3. Экспорт')
    print('4. Импорт')
    print('5. Выйти из программы')
def print_menu_demonstrate():
    print('Введите действие(от 1 до 2): ')
    print('1. Показать контакт в ".txt"')
    print('2. Показать контакт в ".csv"')
def print_menu_save():
    print('Введите действие(от 1 до 2): ')
    print('1. Сохранить в ".txt"')
    print('2. Сохранить в ".csv"')
def print_menu_exsport():
    print('Введите действие(от 1 до 2): ')
    print('1. Экспорт в ".txt"')
    print('2. Экспорт в ".csv"')

# МОДУЛЬ ПОКАЗА Контактов
def demonstrate_txt():
    with open(MAIN_FILENAME, "r", encoding="utf-8") as f:
        res = f.read()
    print()
    print("Данные с файла: '.txt':")
    print(res)
def demonstrate_csv():
    with open(MAIN_FILENAME_2, "r", encoding="utf-8") as f:
        res = f.read()
    print()
    print("Данные с файла: '.csv':")
    print(res)
def demonstrate_menu():    
    nums = int(input())
    if nums == 1:
        demonstrate_txt()
    elif nums == 2:
        demonstrate_csv()

# МОДУЛЬ ЕКСПОРТ
def exsport_menu():
    nums = int(input())
    if nums == 1:
        export_txt()
    elif nums == 2:
        export_csv()
def export_csv():
    filename = input("Введите имя файла: ")
    with open(MAIN_FILENAME_2, "rb") as data:
        with open(f"/Users/pavelpashkov/GB/Pyton/Task/task_Telefon_info/exsport_file/exsport_{filename}.csv", "wb") as new_file:
            new_file.writelines(data.readlines())
def export_txt():
    filename = input("Введите имя файла: ")
    with open(MAIN_FILENAME, "rb") as data:
        with open(f"/Users/pavelpashkov/GB/Pyton/Task/task_Telefon_info/exsport_file/exsport_{filename}.txt", "wb") as new_file:
            new_file.writelines(data.readlines())

# МОДУЛЬ ВВОДА КОНТАКТОВ
def interface_user_save():
    info = []
    last_name = input('Введите фамилию: ')
    info.append(last_name)
    first_name = input('Введите имя: ')
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
    description = input('Введите описание: ')
    info.append(description)
    print_menu_save()
    num = int(input())
    if num == 1:
        with open (MAIN_FILENAME, 'a', encoding = 'utf-8') as data:
            data.write(f'{info[0]};{info[1]};{info[2]};{info[3]}\n')
        
    elif num == 2:
        with open (MAIN_FILENAME_2, 'a', encoding = 'utf-8') as data:
            data.write(f'Фамилия: {info[0]}\n\nИмя: {info[1]}\n\nНомер телефона: {info[2]}\n\nОписание: {info[3]}\n\n\n')

# ГЛАВНОЕ МЕНЮ
def main_logic(command):
    if command == 1:
        print_menu_demonstrate()
        demonstrate_menu()
    elif command == 2:
        interface_user_save()
    
    elif command == 3:
        print_menu_exsport()
        exsport_menu()
    
    # #elif command == 4:


while True:
    time.sleep(1)
    print_menu()
    n = int(input())
    if n == 5:
        break
    main_logic(n)

print("Вы вышли из системы")
