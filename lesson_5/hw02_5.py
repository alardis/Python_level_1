# Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.


import os

with open(f'{os.path.abspath("Python_level_1/lesson_5")}/new_file.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()
    for num, line in enumerate(lines):
        if line.isspace():
            continue
        else:
            words = line.strip().split(' ')
            print(f'Строка {num}: количество слов -- {len(words)}')
