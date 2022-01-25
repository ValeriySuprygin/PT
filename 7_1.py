class Matrix:
    def __init__(self, dt):
        self.dt = dt

    def __str__(self):
        return '\n'.join('\t'.join([f"{pnt:03}" for pnt in ln]) for ln in self.dt)

    def __add__(self, var):
        try:
            matx = [[int(self.dt[ln][pnt]) + int(var.dt[ln][pnt]) for pnt in range(len(self.dt[ln]))]
                    for ln in range(len(self.dt))]
            return Matrix(matx)
        except IndexError:
            return f'Matrix dimension error'


matx_1 = [[7, 2, 46], [4, 12, 21], [67, -8, -15]]
matx_2 = [['4', '34', '22'], ['-91', '32', '-66'], ['20', '3', '57']]


x_1 = Matrix(matx_1)
x_2 = Matrix(matx_2)
user_mtrx = x_1 + x_2
print(x_1)
print(user_mtrx)