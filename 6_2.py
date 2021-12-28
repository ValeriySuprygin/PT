class Paving:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def pav_calc_mass(self, weight=25, thickness=0.09):  # тощину асфальта задавать в метрах!
        print(f"Масса асфальта: {(self._length * self._width * weight * thickness) / 1000} т")


def road():
    while True:
        try:
            param = Paving(int(input("Введите длину дорожного полотна в м: ")),
                           int(input("Введите ширину дорожного полотна в м: ")))
            param.pav_calc_mass()
            break
        except ValueError:
            print("Только числовые значения!")


road()