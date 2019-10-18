# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать итоговый массив чисел,
# соответствующих требованию. Элементы вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.


import random


base_list = [random.randint(0, 20) for _ in range(20)]
print(f'Рандомный список: {base_list}')

unique_list = []
[unique_list.append(item) for item in base_list if item not in unique_list]

print(f'Уникальный список: {unique_list}')