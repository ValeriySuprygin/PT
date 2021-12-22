init_list = [56, 71, 2, 500, 28, 42, 5, 4, 123]
print("Представленный список: ", init_list)
most_neighbor = [init_list[n] for n in range(1, len(init_list)) if init_list[n] > init_list[n - 1]]
print("Список 'Наибольший сосед слева': ", most_neighbor)