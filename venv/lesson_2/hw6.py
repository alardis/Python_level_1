# coding=utf-8
# *Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения). Структуру нужно сформировать программно,
# т.е. запрашивать все данные у пользователя. Пример готовой структуры:
# [ (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”}) ]


print('Давайте создадим подобие базы данных. Помните, что вы можете выйти из цикла создания, набрав "quit"')

structure_list = []
data_dict = None
input_data = ''
while input_data != 'quit':
    input_data = input('Введите название товара\n')
    if input_data == 'quit':
        break
    data_dict = {"название" : input_data}

    input_data = input('Введите цену товара\n')
    if input_data == 'quit':
        break
    while not input_data.isdigit():
        input_data = input('Что-то пошло не так. Введите цену товара еще раз\n')
    data_dict.update({"цена" : int(input_data)})

    input_data = input('Введите количество товара\n')
    if input_data == 'quit':
        break
    while not input_data.isdigit():
        input_data = input('Что-то пошло не так. Введите количество товара еще раз\n')
    data_dict.update({"количество": int(input_data)})

    input_data = input('Введите название единицы товара\n')
    if input_data == 'quit':
        break
    data_dict.update({"ед": input_data})

    item_tuple = (len(structure_list) + 1, data_dict)
    structure_list.append(item_tuple)


print(structure_list)
