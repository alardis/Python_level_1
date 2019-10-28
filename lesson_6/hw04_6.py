# Опишите несколько классов: TownCar, SportCar, WorkCar, PoliceCar. У каждого класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также несколько методов: go, stop, turn(direction), которые должны
# сообщать, что машина поехала, остановилась, повернула (куда).


class Car:
    speed: int
    color: int
    name: int
    is_police: bool

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина поехала со скоростью {self.speed}')

    def stop(self):
        print('Машина остановилась')

    def turn(self, direction:str):
        print(f'Машина поворачивает {direction}')


class TownCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class SportCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):

    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


towncar = TownCar(300, 'Красный', 'Мазератти')
towncar.go()
print(type(towncar))

sportcar = SportCar(400, 'Белый', 'Феррари')
sportcar.stop()
print(type(sportcar))

workcar = WorkCar(120, 'Синий', 'Киа')
workcar.turn('направо')
print(type(sportcar))

policecar = PoliceCar(400, 'Бело-синий', 'Додж')
policecar.go()
print(type(policecar))
