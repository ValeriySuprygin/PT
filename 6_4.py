from random import choice


class Vehicle:
    direction = ["Север", "С-В", "Восток", "Ю-В",
                 "Юг", "Ю-З", "Запад", "С-З"]

    def __init__(self, tl, cl, sp, pl=False):
        self.title = tl
        self.color = cl
        self.speed = sp
        self.is_police = pl
        print(f'Это ТС: {tl} цвет: {cl}.\nЭто ГИБДД или ЦОДД? {pl}')

    def move(self):
        print(f'{self.title}: машина проехала.')

    def stop(self):
        print(f'{self.title}: затем остановилась.')

    def turn(self):
        print(f'{self.title}: и повернула на {choice(self.direction)}.')

    def ind_speed(self):
        return f'{self.title}: со скоростью: {self.speed}.'


class CityCar(Vehicle):

    def ind_speed(self):
        return f'{self.title}: Скорость ТС: {self.speed}. Превышение!!!' if self.speed > 79 else super().ind_speed()


class Wagon(Vehicle):

    def ind_speed(self):
        return f'{self.title}: Скорость ТС: {self.speed}. Превышение!!!' if self.speed > 59 else super().ind_speed()


class CommercialCar(Vehicle):

    def ind_speed(self):
        return f'{self.title}: Скорость ТС: {self.speed}. Превышение!!!' if self.speed > 59 else super().ind_speed()


class SportCar(Vehicle):

    def ind_speed(self):
        return f'{self.title}: Скорость ТС: {self.speed}.' \
               f'Это лишение ВУ"!!!' if self.speed > 79 else super().ind_speed()


class PoliceCar(Vehicle):

    def __init__(self, tl, cl, sp):
        super().__init__(tl, cl, sp, pl=True)


police_car = PoliceCar('Полиционерское авто', 'сине-белое', 120)
truck = Wagon('Фура', 'грязный', 40)
commercial_car = CommercialCar('Газелька', 'чумазый', 40)
sport_car = SportCar('Ракета', 'огненный', 200)
town_car = CityCar('Малолитражка', 'салатовый', 65)

list_of_cars = [police_car, truck, commercial_car, sport_car, town_car]

for v in list_of_cars:
    v.move()
    print(v.ind_speed())
    v.turn()
    v.stop()
    print()