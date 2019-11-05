# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу
# в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.


import hw04_8 as backup


class WareHouse:
    __counter = 1
    __data_storage = {}

    @property
    def data_storage(self):
        return self.__data_storage

    def __add__(self, other: backup.OfficeEquipment):
        record = {'id': other.id, 'title': other.title, 'price': other.price, 'status': other.status}
        if isinstance(other, backup.Printer):
            record.update({'cartridge_status': other.cartridge_status})
        elif isinstance(other, backup.PhotoCopier):
            record.update({'print_mode': other.print_mode})
        elif isinstance(other, backup.ScannerEquipment):
            record.update({'resource': other.resource})
        self.__data_storage.update({self.__counter: record})
        self.__counter += 1


# проверяем, как это все работает
warehouse = WareHouse()
printer = backup.Printer(123, 'Принтер HP', 123, 'new', 'new')
scanner = backup.ScannerEquipment(124, 'Сканер', 10000, 'old', 78854)
photocopier = backup.PhotoCopier(125, 'Ксерокс', 5000, 'too_old', 'color')

warehouse + printer
warehouse + scanner
warehouse + photocopier

print(warehouse.data_storage)
print(1)
