# Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки. Необходимо вычислить прибыль каждой компании и среднюю прибыль.
# Реализовать список, содержащий словарь (название фирмы и прибыль) и словарь с одним элементом (средняя прибыль).
# Добавить в первый словарь еще один элемент, содержащий результат вычисления отношения прибыли к убыткам.
# Итоговый список сохранить в файл.
# Подсказка: использовать менеджеры контекста.

# формат записи:
# Рога и Копыта, ООО, 100000, 4788

import os

with open(f'{os.path.abspath("Python_level_1/lesson_5")}/new_file.txt', 'r', encoding='utf-8') as file,\
        open(f'{os.path.abspath("Python_level_1/lesson_5")}/new_new_file.txt', 'a+', encoding='utf-8') as new_file:
    data_list = file.readlines()
    # print(data_list)
    whole_list = []
    av_income = 0
    for item in data_list:
        local_data_list = item.split(', ')
        income = 0
        try:
            income = int(local_data_list[2]) - int(local_data_list[3])
        except ValueError:
            print('Проверьте финансовые показатели организации!')
        whole_list.append({'Название': f'{local_data_list[1]} {local_data_list[0]}', 'Прибыль': income})
        av_income += income
    av_income = av_income / len(data_list)
    whole_list.append({'Средняя прибыль': av_income})
    # print(whole_list)

    for item in whole_list:
        for key, value in item.items():
            line = f'{key}: {value}'
            # print(line)
            new_file.write(f'{line}\n')
        new_file.write('\n')