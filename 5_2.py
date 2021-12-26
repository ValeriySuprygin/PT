with open("5_2.txt", encoding='utf-8') as new_year:
    string = new_year.readlines()
    for index, value in enumerate(string, 1):
        num_words = len(value.split())
        print(f'Строка {index} включает {num_words} слов(а)')