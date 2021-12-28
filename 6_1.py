import time
import itertools


class TrafficLight:
    __signal = [["КРАСНЫЙ - СТОП!", [7, 31]], ["ЖЕЛТЫЙ - ОЖИДАЙТЕ", [2, 33]],
                ["ЗЕЛЕНЫЙ - ПРОЕЗЖАЙТЕ", [14, 32]], ["ЖЕЛТЫЙ - ОЖИДАЙТЕ", [2, 33]]]

    def operating_mode(self):
        for color in itertools.cycle(self.__signal):
            print(f"\r\033[{color[1][1]}m\033[1m{color[0]}\033[0m", end="")
            time.sleep(color[1][0])


traffic_light = TrafficLight()
traffic_light.operating_mode()