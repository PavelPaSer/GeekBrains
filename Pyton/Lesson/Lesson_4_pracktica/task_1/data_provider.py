from random import randint 
# модуль генерации случю чисел

def get_temperature(sensor):
    return randint(-20, 0) if sensor else randint(0, 20)

def get_pressure(sensor):
    if sensor: # можно по разному написать
        return randint(720, 750) # пониженное
    else:
        return randint(750, 770) # повышенное давление

def get_wind_speed(sensor):
    if sensor == 1: 
        return randint(0, 30) 
    else:
        return randint(30, 50)
# теперь переходим в логирования(logger), т.к. после получения значение нужно их зафиксировать

