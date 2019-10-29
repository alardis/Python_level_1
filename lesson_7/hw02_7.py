# Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого проекта
# — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC


class Clothes(ABC):

    def get_material_size(self):
        pass


class Suit(Clothes):
    __height: float

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if 2.1 > value > 1.4:
            self.__height = value
        else:
            raise ValueError('Некорректный диапазон роста')

    def __init__(self, height):
        self.height = height

    def get_material_size(self):
        return 2*self.height + 0.3


class Coat(Clothes):
    __size: int

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if 60 > value > 35:
            self.__size = value
        else:
            raise ValueError('Значение размера некорректно')

    def __init__(self, size):
        self.size = size

    def get_material_size(self):
        return self.size/6.5 + 0.5


suit = Suit(1.8)
print(suit.get_material_size())

coat = Coat(52)
print(coat.get_material_size())