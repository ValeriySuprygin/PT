from random import randint

with open("5_5.txt", "w", encoding="utf-8") as calc_f:
    f_list = [randint(1, 100) for _ in range(100)]
    calc_f.write(" ".join(map(str, f_list)))

print(f"Сумма сгенерированных чисел = {sum(f_list)}")