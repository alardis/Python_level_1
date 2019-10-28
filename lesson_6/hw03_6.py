# Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"profit": profit, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_full_profit). Проверить работу примера на реальных данных (создать экземпляры класса Position,
# передать данные, проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name, surname, position, profit, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'profit': profit, 'bonus': bonus}


class Position(Worker):

    def __init__(self, name, surname, position, profit, bonus):
        super().__init__(name, surname, position, profit, bonus)

    def get_full_name(self):
        print(f'Полное имя сотрудника: {self.name} {self.surname}')

    def get_full_profit(self):
        full_profit = 0
        for key, value in self._income.items():
            full_profit += value
        print(f'Доход с учетом премии: {full_profit}')


position_test = Position('Андрей', 'Иванов', 'менеджер', 400, 100)
position_test.get_full_name()
position_test.get_full_profit()
