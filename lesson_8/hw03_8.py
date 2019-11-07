# Создайте собственный класс-исключение, который должен проверять содержимое списка на отсутствие элементов типа
# строка и булево. Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные
# и заполнять список. Класс-исключение должен контролировать типы данных элементов списка.


class ListDataError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


my_list = []
buffer = None

while buffer != '':
    print(f'Текущее состояние списка: {my_list}')
    buffer = input('Введите новое значение для списка:\n')
    try:
        if buffer == 'True' or buffer == 'False':
            raise ListDataError('Вы пытаетесь записать в список логическое значение')
        elif buffer.isalpha() or (buffer.isalnum() and not buffer.isdigit()):
            raise ListDataError('Вы пытаетесь записать в список строку')
        elif buffer.isdecimal():
            my_list.append(int(buffer))
        elif is_float(buffer):
            my_list.append(float(buffer))
    except ListDataError as e:
        print(f'Возникли проблемы с элементом списка: {str(e)}')
        pass


