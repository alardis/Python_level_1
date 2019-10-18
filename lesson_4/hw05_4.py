# Реализовать формирование списка, используя функцию range() и возможности генератора. В список должны войти четные
# числа от 100 до 1000 (включая границы). Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().


from functools import reduce

base_list = [item for item in range(100, 1001) if item % 2 == 0]


def my_func(prev_item, item):
    return prev_item * item


print(f'Произведение всех чисел в списке: {reduce(my_func, base_list)}')
