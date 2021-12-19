def awesome_function(i_1, i_2, i_3):
    i_1, i_2, i_3 = int(i_1), int(i_2), int(i_3)
    a_list = [i_1, i_2, i_3]
    try:
        a_list.remove(min(a_list))
        return print("Сумма двух наибольших: ", sum(a_list))
    except TypeError:
        return "Некорректный тип значения. Вводить только числа!"

print(awesome_function(input("Введите первое число: "), input("Теперь второе: "), input("И третье: ")))


