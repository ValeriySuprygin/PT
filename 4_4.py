from random import randint

gen_list = [randint(-15, 15) for _ in range(30)]
nonrec_list = [n for n in gen_list if gen_list.count(n) == 1]
print(f"Generated list\n{gen_list}\nNon-recurring\n{nonrec_list}")