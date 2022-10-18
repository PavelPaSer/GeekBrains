from datetime import datetime as dt  
from time import time
# фиксируем время
def temperature_logger(data): # модуль отвечает за логирование температуры
    time = dt.now().strftime('%H:%M') # получаем время '%H:%' - опишем время во сколько данные пришли
    with open('log.csv', 'a') as file: # записываем в файлик
        file.write('{};temperature;{}\n' # втром значение будет data (куда придет значение)
                    .format(time, data))

def pressure_logger(data):
    time = dt.now().strftime('%H:%M') # получаем время '%H:%' - опишем время во сколько данные пришли
    with open('log.csv', 'a') as file: # записываем в файлик
        file.write('{};pressure;{}\n' # втром значение будет data (куда придет значение)
                    .format(time, data))

def wind_speed_logger(data):
    time = dt.now().strftime('%H:%M') # получаем время '%H:%' - опишем время во сколько данные пришли
    with open('log.csv', 'a') as file: # записываем в файлик
        file.write('{};wind_speed;{}\n' # втром значение будет data (куда придет значение)
                    .format(time, data))

# переходим на новый модуль "user_interface"