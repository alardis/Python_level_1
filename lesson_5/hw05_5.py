# Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.


import os
import random

# сперва создадим текстовый файл и набьем в него чисел
with open(f'{os.path.abspath("Python_level_1/lesson_5")}/new_file.txt', 'w+', encoding='utf-8') as file:
    number_list = []
    for i in range(10):
        number_list.append(str(random.randint(0, 40)))
    file.write(' '.join(number_list))

with open(f'{os.path.abspath("Python_level_1/lesson_5")}/new_file.txt', 'r', encoding='utf-8') as file:
    number_list_2 = file.readline().split(' ')
    print(f'Прочитанный из файла список -- {number_list_2}')
    for num, item in enumerate(number_list_2[:]):
        try:
            number_list_2[num] = int(item)
        except ValueError:
            print('Ошибка при переводе числа из списка в числовой формат для сложения, проверьте')
    print(f'Сумма чисел, записанных в файл -- {sum(number_list_2)}')
