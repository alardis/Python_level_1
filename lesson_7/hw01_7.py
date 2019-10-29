# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который
# должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
#
# 31   22
# 37   43
# 51   86
#
# 3    5    32
# 2    4    6
# -1   64   -8
#
# 3   5   8   3
# 8   3   7   1
#
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
# Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.


class Matrix:
    __data: list

    def __init__(self, data: list):
        self.__data = data.copy()
        print(f'Создали матрицу с параметром: {self.__data}')

    def __str__(self):
        result = ''
        for row in self.__data:
            for cell in row:
                result = f'{result}{cell}\t'
            result = result.strip('\t')
            result = f'{result}\n'
        result = result.strip('\n')
        return result

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError('Слагаемое не является матрицей')

        new_data = []
        if len(self.__data) != len(other.__data):
            raise ValueError('Матрицы разных размеров, сложение невозможно')
        for row_self, row_other in zip(self.__data, other.__data):
            if len(row_self) != len(row_other):
                raise ValueError('Матрицы разных размеров, сложение невозможно')
            local_list = []
            for cell_self, cell_other in zip(row_self, row_other):
                local_list.append(cell_self + cell_other)
            new_data.append(local_list)
        return Matrix(new_data)


matrix = Matrix([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(matrix)
matrix2 = Matrix([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
print(matrix + matrix2)
