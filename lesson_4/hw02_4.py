# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.


import random


base_list = [random.randint(0, 10) for _ in range(10)]
print(f'Рандомный лист: {base_list}')

new_list = []
for num, item in enumerate(base_list):
    if num > 0 and base_list[num-1] < item:
        new_list.append(item)

print(f'Новый список: {new_list}')