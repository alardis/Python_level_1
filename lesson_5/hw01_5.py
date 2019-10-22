# Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

import os

with open(f'{os.path.abspath("Python_level_1/lesson_5")}/new_file.txt', 'w', encoding='utf-8') as file:
    line = None
    while line != '':
        line = input('Введите строку, которую хотите записать в файл. Если не хотите, нажмите Enter\n')
        file.write(f'{line}\n')
