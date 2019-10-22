# Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.


import os

with open(f'{os.path.abspath("Python_level_1/lesson_5")}/new_file.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    av_sum = 0
    for num, line in enumerate(lines):
        if line.isspace():
            continue
        else:
            line = line.strip()
            words = line.split(' ')
            try:
                salary = int(words[1])
                av_sum += salary
                if salary <= 20000:
                    print(f'Сотрудник {words[0]} имеет низкую зарплату ({words[1]})')
            except ValueError:
                print(f'Проверьте данные в файле на строке {num}')

    print(f'\nСредняя зарплата при этом составляет: {av_sum / len(lines)}')
