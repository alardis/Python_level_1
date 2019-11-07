# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса
# (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.


class ComplexNumber:
    __rez: float
    __imz: float

    @property
    def rez(self):
        return self.__rez

    @rez.setter
    def rez(self, value):
        self.__rez = value

    @property
    def imz(self):
        return self.__imz

    @imz.setter
    def imz(self, value):
        self.__imz = value

    def __init__(self, rez, imz):
        self.rez = rez
        self.imz = imz

    def __str__(self):
        if self.imz > 0 and self.rez != 0:
            return f'{self.rez}+{self.imz}i'
        elif self.imz < 0 and self.rez != 0:
            return f'{self.rez}-{abs(self.imz)}i'
        elif self.rez == 0:
            return f'{self.imz}i'
        else:
            return f'{self.rez}'

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.rez+other.rez, self.imz+other.imz)
        else:
            raise ValueError('Значение не подходит для сложения с комплексным числом')

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            return ComplexNumber(self.rez*other.rez - self.imz*other.imz, self.imz*other.rez + self.rez*other.imz)
        elif isinstance(other, int) or isinstance(other, float):
            return ComplexNumber(self.rez * other, self.imz * other)
        else:
            raise ValueError('Значение не подходит для умножения на комплексное число')


# проверка создания объекта
number1 = ComplexNumber(4, 2)
print(number1)
# проверка сложения
print(ComplexNumber(1, 1) + ComplexNumber(2, 2))
# проверка умножения
print(ComplexNumber(1, 2) * ComplexNumber(2, 3))
print(ComplexNumber(2, 2) * 2)
