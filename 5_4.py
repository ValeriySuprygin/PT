trans_to_rus = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("5_4.txt", "w", encoding="utf-8") as eng_f:
    with open("5_4_rus.txt", encoding="utf-8") as rus_f:
        eng_f.writelines([line.replace(line.split()[0], trans_to_rus.get(line.split()[0])) for line in rus_f])