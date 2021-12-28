class HeadDept:
    def __init__(self, company, name, surname, pos_title, wage, bonus):
        self.company = company
        self.name = name
        self.surname = surname
        self.position = pos_title
        self._income = {"wage": wage, "bonus": bonus}


class Position(HeadDept):
    def full_name(self):
        return f"{self.name} {self.surname}"

    def full_salary(self):
        return f"{sum(self._income.values())} euro"


manager = Position("LTMI", "Claudia", "Consiglo", "Quality Manager", 5761, 734)
print(manager.company)
print(manager.full_name())
print(manager.position)
print(manager.full_salary())