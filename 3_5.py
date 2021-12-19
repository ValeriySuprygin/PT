def _sum():
    a = 0
    while True:
        user_list = input("Введите последовательность чисел через пробел (для выхода: 'w'): ").split()
        for n in user_list:
            if n.lower() == "w":
                return a
            else:
                try:
                    a += int(n)
                except ValueError:
                    print("Для выхода нажмите: 'w'.")
        print(f"Сумма чисел в последовательности = {a}")

print(_sum())
