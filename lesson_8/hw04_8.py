# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.


from abc import ABC


class OfficeEquipment(ABC):
    __id: int
    __price: float
    __title: str
    __status: str

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        pass

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value > 0:
            self.__price = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def id(self, value):
        self.__title = value

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, value):
        self.__status = value

    def __init__(self, id, title, price, status):
        self.__id = id
        self.__title = title
        self.__price = price
        self.__status = status


class Printer(OfficeEquipment):
    __cartridge_status: str

    @property
    def cartridge_status(self):
        return self.__cartridge_status

    @cartridge_status.setter
    def cartridge_status(self, value):
        self.__cartridge_status = value

    def __init__(self, id, title, price, status, cartridge_status):
        super().__init__(id, title, price, status)
        self.__cartridge_status = cartridge_status


class ScannerEquipment(OfficeEquipment):
    __resource: int

    @property
    def resource(self):
        return self.__resource

    @resource.setter
    def resource(self, value):
        self.__resource = value

    def __init__(self, id, title, price, status, resource):
        super().__init__(id, title, price, status)
        self.__resource = resource


class PhotoCopier(OfficeEquipment):
    __print_mode: str

    @property
    def print_mode(self):
        return self.__print_mode

    @print_mode.setter
    def print_mode(self, value):
        self.__print_mode = value

    def __init__(self, id, title, price, status, print_mode):
        super().__init__(id, title, price, status)
        self.__print_mode = print_mode


class WareHouse:
    pass
