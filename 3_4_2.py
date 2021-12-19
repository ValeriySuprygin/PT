def expo_func2(d, s):
    try:
        d, s = float(d), int(s)
        if d <= 0 or s >= 0:
            return 'Условие не выполнено:\nd должен быть больше 0\ns должен быть меньше 0'
        else:
            result = 1
            for _ in range(abs(s)):
                result /= d
            return f'Результат возведения d в степень s: {round(result, 6)}'
    except ValueError:
        return "Я работаю только с числами!"


var1 = input('Введите действительное положительное число, d = ')
var2 = input('Введите целое отрицательное число, s = ')

print(expo_func2(var1, var2))
