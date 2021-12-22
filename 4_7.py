def _generator_(n):
    _num_ = 1
    for x in range(n + 1):
        yield f'{x}! = {_num_}'
        _num_ *= x + 1

for i in _generator_(int(input('Введите число и ловите факториал: '))):
    print(i)