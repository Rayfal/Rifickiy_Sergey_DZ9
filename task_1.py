"""
Создать класс TrafficLight (светофор).
определить у него один атрибут color (цвет) и метод running (запуск);
атрибут реализовать как приватный;
в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный;
продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение;
переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный);
проверить работу примера, создав экземпляр и вызвав описанный мето
"""


import itertools
import time


class TrafficLight:
    __color: str
    __timing: dict

    def __init__(self, red_time: int = 7, yellow_time: int = 2, green_time: int = 5):
        self.__timing = {
            'red': red_time,
            'yellow': yellow_time,
            'green': green_time
        }

    def running(self):
        for mode, timer in itertools.cycle(self.__timing.items()):
            self.__color = mode

            for second in range(timer):
                print(f'{self} [{second + 1}]')
                time.sleep(1)

    def __repr__(self):
        return f'The signal is on now: {self.__color}'


try:
    traffic_light = TrafficLight(7, 2, 5)
    traffic_light.running()
except KeyboardInterrupt:
    print("Exit the program")