# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться
# в новый текстовый файл.


import os

translator = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
try:
    with open(f'{os.path.abspath("Python_level_1/lesson_5")}/new_file.txt', 'r', encoding='utf-8') as file,\
            open(f'{os.path.abspath("Python_level_1/lesson_5")}/new_new_file.txt', 'a+', encoding='utf-8') as sec_file:
        lines = file.readlines()
        for line in lines:
            words = line.split(' ')
            if words[0] in translator.keys():
                words[0] = translator[words[0]]
            sec_file.write(' '.join(words))
except FileNotFoundError:
    print('Один из файлов отсутствует!')
