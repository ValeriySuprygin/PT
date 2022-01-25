from abc import ABC, abstractmethod


class Garments(ABC):
    models = []

    def __init__(self, props):
        self.props = props
        Garments.models.append(self)

    @abstractmethod
    def cloth_expense(self):
        pass

    def __del__(self):
        if self in Garments.models:
            Garments.models.remove(self)


class Topcoat(Garments):
    @property
    def cloth_expense(self):
        return round(self.props / 6.5 + 0.5, 2)


class Suit(Garments):
    @property
    def cloth_expense(self):
        return round((self.props * 2 + 0.3), 2)


topcoat_1 = Topcoat(50)
suit_1 = Suit(1.72)


total_cloth_expense = 0
for w in Garments.models:
    total_cloth_expense += w.cloth_expense
print(f"Total cloth expense: {total_cloth_expense}")
topcoat_1.__del__()

total_cloth_expense = 0
for w in Garments.models:
    total_cloth_expense += w.cloth_expense
print(f"Total cloth expense: {total_cloth_expense}")