
def input_nubs(inputText): # функция ввода данных типа int
    mark = False
    while not mark:
        try:
            number = int(input(f'{inputText}'))
            mark = True
        except ValueError:
            print('Это не число типа int ')
    return number

def main_menu():
    while True:
        key = input('Добро пожаловать\n 0 - Вход\n1 - Выход')