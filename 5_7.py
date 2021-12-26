import json


with open("5_7.json", "w", encoding="utf-8") as f_f:
    with open("5_7.txt", encoding="utf-8") as n_airlines:
        income = {string.split()[0]: int(string.split()[2]) - int(string.split()[3]) for string in n_airlines}
        summary = [income, {"Average income: ": round(sum([int(n) for n in income.values() if int(n) > 0]) /
                                                   len([int(n) for n in income.values() if int(n) > 0]))}]
    json.dump(summary, f_f, ensure_ascii=False, indent=4)