# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой


def user_data_func(**kwargs) -> str:
    if kwargs:
        result = ''
        for key, value in kwargs.items():
            result += value + ', '
        result = result.strip(', ')

        return result
    else:
        return 'У вас проблемы с данными о пользователе.'


print(user_data_func(
    username='Ярослав',
    surname='Иванов',
    birthyear='1985',
    usercity='Moscow',
    email='ata@ata.ru',
    phonenumber='+7916-555-55-55',
))
