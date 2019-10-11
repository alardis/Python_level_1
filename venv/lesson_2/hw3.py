# coding=utf-8
# Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц
# (зима, весна, лето, осень). Напишите решения через list и через dict.


# вариант решения через LIST
winter = [12, 1, 2]
spring = [3, 4, 5]
summer = [6, 7, 8]
autumn = [9, 10, 11]

month = input('Введите номер месяца, пожалуйста\n')
if month.isdigit() and int(month) >= 1 and int(month) <= 12:
    month = int(month)
    if month in winter:
        print('Месяц зимний')
    elif month in spring:
        print('Месяц весенний')
    elif month in summer:
        print('Месяц летний')
    elif month in autumn:
        print('Месяц осенний')
else:
    print('У вас что-то не так с входным значением, попробуйте еще разок запустить')


# теперь попробуем решить через dict
print('\nТеперь решим задачу несколько иначе, через dict')

year_dict = {'зимний' : [12, 1, 2], 'весенний' : [3, 4, 5], 'летний' : [6, 7, 8], 'осенний' : [9, 10, 11]}
print(type(year_dict))
month = input('Введите номер месяца, пожалуйста\n')
if month.isdigit() and int(month) >= 1 and int(month) <= 12:
    month = int(month)

    for key, value in year_dict.items():
        if month in value:
            print(f'Месяц {key}')
            break
else:
    print('У вас что-то не так с входным значением, попробуйте еще разок запустить')

