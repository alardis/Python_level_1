# Реализовать два небольших скрипта:
# а) бесконечный итератор, генерирующий целые числа, начиная с указанного,
# б) бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools.


import itertools
import random


mode = input('Какой скрипт будем смотреть?\nБесконечно возрастающий итератор(1) или Цикличный генератор(2)?\n')

if mode == '1':
    print('Выбран вариант 1. Бесконечно возрастающий итератор.')
    begin_number = input('Введите целое число, с которого начнем генерировать числа\n')
    try:
        begin_number = int(begin_number)
        for item in itertools.count(begin_number):
            print(item)
            decision = input('Продолжить вывод? Наберите "Нет", чтобы прекратить, или нажмите Enter, если согласны.  ')
            if decision == 'Нет':
                break
    except ValueError:
        print('Проблемы с числом. Попробуйте запустить программу еще разок.')
elif mode == '2':
    print('Выбран вариант 2. Бесконечный циклический итератор.')
    list_to_cycle = [random.randint(0, 10) for item in range(4)]
    print(f'Список значений, который будет закциклен:  {list_to_cycle}')
    for item in itertools.cycle(list_to_cycle):
        print(item)
        decision = input('Продолжить вывод? Наберите "Нет", чтобы прекратить, или нажмите Enter, если согласны.  ')
        if decision == 'Нет':
            break
