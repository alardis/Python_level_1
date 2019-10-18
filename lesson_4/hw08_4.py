# Напишите Lambda функцию которая принимает на вход положительное целое число, а в ответ возвращает произведение
# всех цифр данного числа игнорируя нули.
# Например на вход 123405 в результате 120


from functools import reduce


lambda_strong = lambda number: reduce(lambda a1, a2: a1*a2 if a2 != 0 else a1*1,
                                      [(number // 10**i) % 10 for i in range(100) if number // (10**i) > 0])


print(lambda_strong(120002))
