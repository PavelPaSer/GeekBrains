from user_interface import temperature_view 
from user_interface import wind_speed_view
from user_interface import pressure_view 
# делаем импорт нашего интерфейса извлейкам отедльгые методы
# Нужно описать, то что будет генерить этот HTML файл.
# обычно делаем при помощь библиотек, но сейчас тренируемся

def create(device = 1): # принимает какой-то дейвас с какого дейваса
    style = 'style="font-size:30px;"' # описываем стиль 30 шрифт
    html = '<html>\n <head></head>\n  <bode>\n' # есть заготовка для html 
    html += '    <p {}>temperature: {} c</p>\n'\
        .format(style, temperature_view(device)) #
    html += '    <p {}>wind_speed: {} m/c</p>\n'\
        .format(style, wind_speed_view(device))
    html += '    <p {}>pressure: {} mmHg</p>\n'\
        .format(style, pressure_view(device))
    html += '    </body>\n</html>'

    with open('index.html', 'w') as page: # создаем файл и сохраняем 
        page.write(html)
    return html

# теперь смотри как это все будет рабоать > main 





