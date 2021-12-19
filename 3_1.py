def div_op(n1, n2):
    try:
        n1, n2 = float(n1), float(n2)
        div_op_result = n1 / n2
    except ValueError:
        return "Неверное значение для функции, требуется ввести число!"
    except ZeroDivisionError:
        return "Деление на ноль невозможно!!!"
    return print("Результат деления: ", round(float(div_op_result), 10))

print(div_op(input("Введите первое число: "), input("Теперь второе: ")))