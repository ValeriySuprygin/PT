from itertools import cycle

print('\n--- Повторяю! ---')
assigned_list = ['Учится', '100 раз учится', 9.780, 'm/c2', 335, 'м/сек']
enumerator = cycle(assigned_list)

for x in range(len(assigned_list) * 2):
    print(next(enumerator), end=' ')