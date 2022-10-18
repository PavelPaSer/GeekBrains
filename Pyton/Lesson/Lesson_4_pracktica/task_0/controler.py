import model # будет рабоать с нашей моделью (model)
import view 

def buttom_click(): # напишем метод который будет позволять пользователю нажимать кнопку для ввода
    value_a = view.get_value()
    value_b = view.get_value() # возврашаемся во view
    model.init(value_a, value_b) # инецилизируем данные
    result = model.sum() # вычислим сумму
    view.view_data(result) # вернем значение в наше вью дата

# КАК ЗАСТАВИТЬ РАБОАТЬ нужно доп точка входа (main.py)
