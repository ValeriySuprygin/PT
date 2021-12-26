with open("5_6.txt", 'r', encoding="utf-8") as course_sum:
    abc = course_sum.readlines()
    for i in abc:
        string = ''.join((n if n in '1234567898' else ' ') for n in i)
        new_string = [int(i) for i in string.split()]
        print(f"{i.split()[0]} {sum(new_string)}")