# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен извлекать число, месяц, год
# и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных.


class DateValidationError(Exception):

    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


class MyDate:
    __day: int
    __month: int
    __year: int

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        self.__day = value

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value):
        self.__month = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    @classmethod
    def date_parser(cls, date_string):
        date_list = date_string.split('-')
        if len(date_list) == 3:
            return int(date_list[0]), int(date_list[1]), int(date_list[2])

    # первый член - число
    # второй член - месяц
    # третий член - год
    @staticmethod
    def date_analizer(*args):
        if args:
            day, month, year = args[0]
        else:
            raise ValueError(f'Передано значение: {args}')

        day_pass, month_pass, year_pass = False, False, False

        # валидируем день
        if 1 >= day / 31 > 0 and isinstance(day, int):
            day_pass = True
        else:
            raise DateValidationError('Проверьте день')

        # валидируем месяц
        if 1 >= month / 12 > 0 and isinstance(month, int):
            month_pass = True
        else:
            raise DateValidationError('Проверьте месяц')

        # валидируем год
        if 3 >= year / 1000 > 0 and isinstance(month, int):
            year_pass = True
        else:
            raise DateValidationError('Проверьте год')

        return day_pass and month_pass and year_pass

    def __init__(self, date_string):
        date_tuple = self.date_parser(date_string)
        if MyDate.date_analizer(date_tuple):
            self.day = date_tuple[0]
            self.month = date_tuple[1]
            self.year = date_tuple[2]

    def get_date(self):
        return f'{self.day} - {self.month} - {self.year}'


mydate = MyDate('11-10-2001')
print(mydate.get_date())

mydate1 = MyDate('134-10-2001')