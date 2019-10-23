# Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и наличие лекционных,
# практических и лабораторных занятий по этому предмету и их количество. Важно, чтобы для каждого предмета
# не обязательно были все типы занятий. Сформировать словарь, содержащий название предмета
# и общее количество занятий по нему.
# Вывести словарь на экран.

# формат файла:
# Философия. Лекционное занятие: 10, Практическое занятие: 13


import os


with open(f'{os.path.abspath("Python_level_1/lesson_5")}/new_file.txt', 'r', encoding='utf-8') as file:
    lines_list = file.readlines()
    lessons_dict = {}
    for line in lines_list:
        record = line.split('. ')
        lesson_key = record[0]
        lesson_val = 0
        for work in record[1].split(', '):
            work_detailed = work.split(': ')
            lesson_val += int(work_detailed[1])
        lessons_dict.update({lesson_key: lesson_val})

for key, value in lessons_dict.items():
    print(f"{key}: {value}")

