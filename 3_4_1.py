#def expo_func(a, b):
#    try:
#       a, b = float(a), int(b)
#        result = a ** b
#    except TypeError:
#        if a <= 0 or b >= 0:
#            return "Первое число должно быть действительное положительное, а второе - целое отрицательное"
#    return print("Результат возведения в степень: ", result)

# print(expo_func(input("Введите первое число: "), input("И второе: ")))

def expo_func(a, b):
    try:
        result = a ** b
    except TypeError:
        return "Enter a float number and a negative power"
    return result

print(expo_func(6.1, -3))

# в таком виде функция не ломается при первом аргументе отрицательном, пытался выше сделать корректно.