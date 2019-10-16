# Задача: написать функцию которая на вход принимает список с неопределенным уровнем вложенности других списков,
# например  [1,  2, [3, 4, [5]], 6, [[[7, [8]]]]]
# Функция должна вернуть плоский список сохраняя последовательность [1, 2, 3, 4, 5, 6, 7, 8]


def list_convert(outerlist, item_to_check):
    print(f"Рассматриваем элемент (начало): {item_to_check}")
    if type(item_to_check) is list:
        for i in item_to_check:
            print(f"Рассматриваем элемент при вызове функции: {i}")
            list_convert(outerlist, i)
    else:
        print(f"добавляем в список: {item_to_check}")
        outerlist.append(item_to_check)


mylist = []
list_to_plain = [1,  2, [3, 4, [5]], 6, [[[7, [8]]]]]
list_convert(mylist, list_to_plain)

print(mylist)

# а теперь попробуем то же самое с лямбдой
mylist1 = []
lambda_plain = lambda item: mylist1.append(item) if type(item) is not list else [lambda_plain(i) for i in item]

[lambda_plain(i) for i in list_to_plain]

print(f"mylist1: {mylist1}")
