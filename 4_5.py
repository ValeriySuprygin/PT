from functools import reduce

def sum_mul_list(ah, oh):
    return ah * oh


gen_list = [aha for aha in range(100, 1001, 2)]
print(f"Сгенерированный список:\n{gen_list}\nРезультат перемножения всех чисел списка:"
      f"\n{reduce(sum_mul_list, gen_list)}")