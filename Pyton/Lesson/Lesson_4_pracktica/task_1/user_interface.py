import data_provider as prov
import logger as log

def temperature_view(senson): # метод показывающий информ о погоде
    data = prov.get_temperature(senson) # получение данных температуры 
    log.temperature_logger(data) # пишем информацию о значение которое мы получили 
    return data # вернем значения которые получили


def pressure_view(senson): 
    data = prov.get_pressure(senson) 
    log.pressure_logger(data) 
    return data 

def wind_speed_view(senson): 
    data = prov.get_wind_speed(senson) 
    log.wind_speed_logger(data) 
    return data 

# описание 3 модудя, теперь остается html_creater