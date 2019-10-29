# Реализовать программу работы с клетками. Необходимо создать класс Клетка. В его конструкторе инициализировать
# параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы перегрузки
# арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление (__truediv__())
# . Данные методы должны выполнять увеличение, уменьшение, умножение и обычное (не целочисленное) деление клеток,
# соответственно. В методе деления должно осуществляться округление значения до целого числа.
# В классе необходимо реализовать метод make_cell(), принимающий экземпляр класса и количество клеток в ряду.
# Метод должен возвращать строку виду *****\n*****\n*****..., где количество клеток между \n равно переданному
# аргументу, а количество рядов определяется, исходя из общего количества клеток.
# При создании экземпляра клетки должна происходить перезапись параметра, который хранит количество клеток.
# Подсказка: подробный список операторов для перегрузки доступен по ссылке.


class Cell:
    __how_many: int

    @property
    def how_many(self):
        return self.__how_many

    @how_many.setter
    def how_many(self, value):
        if value > 0:
            self.__how_many = value
        else:
            raise ValueError('Количество клеток не может быть больше нуня!')

    def __init__(self, how_many):
        self.__how_many = how_many

    def make_cell(self, number: int):
        result = ''
        if self.how_many < number:
            result = '*' * self.how_many
        else:
            reserve = self.how_many
            while reserve > 0:
                result = f'{result}{"*" * min(number, reserve)}\n'
                reserve = reserve - number
            result = result.strip('\n')
            return result

    def __str__(self):
        return f'Набор ячеек, количество: {self.how_many}'

    def __add__(self, other):
        if not isinstance(other, Cell):
            raise ValueError('Второе слагаемое не является ячейками!')

        return Cell(self.how_many + other.how_many)

    def __sub__(self, other):
        if not isinstance(other, Cell):
            raise ValueError('Второе слагаемое не является ячейками!')
        elif self.how_many - other.how_many < 0:
            raise ValueError('Ячеек во втором объекте больше, чем в первом. Недопустимая операция')
        return Cell(self.how_many - other.how_many)

    def __mul__(self, other):
        if isinstance(other, Cell):
            return Cell(self.how_many * other.how_many)
        elif isinstance(other, int):
            return Cell(self.how_many * other)
        else:
            raise ValueError('Недопустимый формат множителя')

    def __truediv__(self, other):
        if isinstance(other, Cell):
            return Cell(self.how_many // other.how_many)
        elif isinstance(other, int):
            return Cell(self.how_many // other)
        else:
            raise ValueError('Недопустимый формат делителя')


cells = Cell(15)
cells1 = Cell(6)
print(cells.make_cell(6))
print(cells / cells1)
