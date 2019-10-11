# coding=utf-8
# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
# необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них. Подсказка.
# Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].


rating_list = [7, 5, 3, 3, 2]

fish_bite = False
was_added = False
print(rating_list)

new_rating = input('Введите новый рейтинг, пожалуйста\n')
if new_rating.isdigit():
    new_rating = int(new_rating)

    for num, rating in enumerate(rating_list[:]):
        print(f'Проверяем {num}: {rating}')

        if not fish_bite and new_rating <= rating:
            print(f' -- Навелись на позиции {num}: {rating}')
            fish_bite = True
        elif fish_bite and new_rating > rating:
            print(f' -- Собираемся добавлять {new_rating}')
            rating_list.insert(num, new_rating)
            was_added = True
            break
    
    if not fish_bite and not was_added:
        rating_list.insert(0, new_rating)
    elif fish_bite and not was_added:
        rating_list.append(new_rating)

    print(rating_list)
else:
    print('Ошибка ввода. Запустите еще раз и введите число, все-таки.')

