# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
# изученных на уроках по ООП.


import hw05_8 as backup5
import hw04_8 as backup4


def validator(message, data_type):
    success = False
    result = None
    while not success:
        buffer = input(f'{message}\n')
        if data_type == 'int':
            try:
                result = int(buffer)
                success = True
            except ValueError:
                print('Неверный формат данных, попробуйте еще раз:')
        elif data_type == 'float':
            try:
                result = float(buffer.replace(',', '.'))
                success = True
            except ValueError:
                print('Неверный формат данных, попробуйте еще раз')
    return result


warehouse_new = backup5.WareHouse()
print(f'Состояние склада на начало:\n{warehouse_new.data_storage}')

buffer = None
while buffer != '':
    try:
        buffer = input('Выберите тип оборудования:\nПринтер -- 1\nСканер -- 2\nФотокопир -- 3\n')
        creation_mode = int(buffer)

        id = validator('Введите id оборудования', 'int')
        title = input('Введите название оборудования\n')
        price = validator('Введите цену оборудования', 'float')
        status = input('Введите статус оборудования\n')
        equipment = None

        if creation_mode == 1:
            cartridge_status = input('Введите описание состояния картриджа оборудования\n')
            equipment = backup4.Printer(id, title, price, status, cartridge_status)
            # print(f'Блок создания принтера, склад: {warehouse.data_storage}')
            warehouse_new + equipment
            # print(f'Блок создания принтера, склад: {warehouse.data_storage}')
        elif creation_mode == 2:
            resource = validator('Введите оставшийся ресурс оборудования в листах\n', 'int')
            equipment = backup4.ScannerEquipment(id, title, price, status, resource)
            warehouse_new + equipment
        elif creation_mode == 3:
            print_mode = input('Введите описание режима печати оборудования\n')
            equipment = backup4.PhotoCopier(id, title, price, status, print_mode)
            warehouse_new + equipment

        print(f'Текущее состояние склада:\n{warehouse_new.data_storage}')
        buffer = input('Желаете создать еще один экземпляр оборудования? Введите "Да", если желаете. '
                       'Если нет, отправьте пустую строку\n')
    except ValueError:
        print(f'buffer -- "{buffer}"')
        if buffer == '':
            print('Программа завершает работу. Хорошего дня!')
        else:
            print('Проверьте вводимое значение и попробуйте еще разок создать оборудование')