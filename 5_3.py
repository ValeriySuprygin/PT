def salary():
    wages = {}
    try:
        with open('5_3.txt', 'r', encoding='utf-8') as pay_slip:
            for string in pay_slip:
                wages[string.split()[0]] = float(string.split()[1])
        print('Меньше 20000 получают: ')
        for surname, wage in wages.items():
            if wage < 20000:
                print(surname)
        print(f'Средняя зарплата равна {(sum(wages.values()) / len(wages))}')
    except IOError:
        print(f'Собственнику нужна новая яхта, придется потерпеть (((')
    except:
        print('Зачем ломаешь то!')


salary()
print('Догадайтесь, сотрудник с какой фамилией получил больше всех )))')