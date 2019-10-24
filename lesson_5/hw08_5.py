# Написать лямбда функцию на вход принимающую строку из латинских символов на выходе возврадает символ
# в нижнем регистре который чаще всего встречается в строке,
# учитывать что символ верхнего регистра и символ нижнего регистра равны.
# Наша задача определить именно букву которая чаще всего встречается в строке


from collections import Counter


often_letter_2 = lambda line: max(zip(
    (lambda local_line: {key: value for key, value in Counter(line.lower()).items()
                         if not key.isdigit() and not key.isspace()})(line).values(),
    (lambda local_line: {key: value for key, value in Counter(line.lower()).items()
                         if not key.isdigit() and not key.isspace()})(line).keys()
))[1]

print(often_letter_2('Раз два три четыре пять'))
