# coding=utf-8
# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать. Если в слово длинное, выводить только первые 10 букв в слове.



user_line = input('Введите строку из нескольких слов, разделенных пробелами\n')

word_list = user_line.split(' ')

for num, word in enumerate(word_list):
    word_to_print = word if len(word) <= 10 else word[:10]
    print(f'{num}: {word_to_print}')
