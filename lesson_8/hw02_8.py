# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна корректно обработать
# эту ситуацию и не завершиться с ошибкой.


class CustomZeroDivide(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


try:
    one = int(input('Введите первое число:\n'))
    two = int(input('Введите второе число:\n'))
    if two == 0:
        raise CustomZeroDivide('Похоже, вы тут делаете то, что нельзя')
    three = one / two
    print(f'{one} / {two} = {one/two}')
except CustomZeroDivide:
    print('Пожалуйста, не делите на ноль. Так нельзя\n')
    print(f'{one} / {two} = ...')
