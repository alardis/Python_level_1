# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Время перехода между режимами должно составлять 7 и 2 секунды.
# Проверить работу примера, создав экземпляр и вызвав описанный метод.


import time

class TrafficLight:
    __color = None

    def running(self):
        time_to_start = time.time()
        current_time = None
        __color = 'красный'
        print(f'Режим светофора: {__color}')

        while __color != 'зеленый':
            current_time = time.time()
            if current_time - time_to_start == 1:
                print(time.time())

            if current_time - time_to_start >= 7 and __color == 'красный':
                __color = 'желтый'
                print(f'Режим светофора: {__color}')
                time_to_start = time.time()
            elif current_time - time_to_start >= 2 and __color == 'желтый':
                __color = 'зеленый'
                print(f'Режим светофора: {__color}')


light = TrafficLight()
light.running()
