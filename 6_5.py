class DrawingStationery:
    def __init__(self, title="Бери и рисуй!"):
        self.title = title

    def draw(self):
        print(f"Это принадлежности для рисования. {self.title}")


class Pen(DrawingStationery):
    def draw(self):
        print(f"Начни рисовать ручкой {self.title}!")


class Pencil(DrawingStationery):
    def draw(self):
        print(f"Можешь также карандашами {self.title}!")


class FeltPen(DrawingStationery):
    def draw(self):
        print(f"Фломастерами {self.title} будет очень красиво!")


class Crayons(DrawingStationery):
    def draw(self):
        print(f"А мелками {self.title} просто супер!")


draw_stat = DrawingStationery()
pen = Pen("Parker")
pencil = Pencil("Erich Krause")
felt_pen = FeltPen("из 'Леонардо'")
crayons = Crayons("MAPED")


drawing_supplies = [draw_stat, pen, pencil, felt_pen, crayons]


for d in drawing_supplies:
    d.draw()

print("И тогда...сам Бэнкси будет тебя копировать!")