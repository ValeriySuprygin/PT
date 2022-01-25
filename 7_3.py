class OrgCell:
    def __init__(self, qty):
        self.qty = qty

    def mod_request(self, colmns):
        return '\n'.join([' infusoria ' * colmns for _ in range(self.qty // colmns)]) + '\n' + ' infusoria ' \
               * (self.qty % colmns)

    def __str__(self):
        return f"{self.qty}"

    def __add__(self, var):
        print("Organic cells summary: ")
        return OrgCell(self.qty + var.qty)

    def __sub__(self, var):
        print("Organic cells subtraction: ")
        return OrgCell(self.qty - var.qty) if self.qty - var.qty > 0 \
            else "There are fewer cellules in the first cell than in the second, subtraction is impossible!"

    def __mul__(self, var):
        print("Organic cells multiplication: ")
        return OrgCell(self.qty * var.qty)

    def __floordiv__(self, var):
        print("Organic cells integer division: ")
        return OrgCell(self.qty // var.qty)


org_cell_ameba = OrgCell(19)
org_cell_infusoria = OrgCell(17)
print(org_cell_ameba + org_cell_infusoria)
print(org_cell_ameba - org_cell_infusoria)
print(org_cell_ameba * org_cell_infusoria)
print(org_cell_ameba // org_cell_infusoria)
print(org_cell_infusoria.mod_request(5))