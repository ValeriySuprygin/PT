from itertools import count

enumerator = count(int(input('Введите целое число, от которого начнется генерация: ')))
print('Тринадцать чисел, начиная с введенного: ')
for x in range(13):
    print(next(enumerator), end=' ')