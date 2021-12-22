from sys import argv


def wage():
    try:
        time_hours, rate, bonus, vat = map(float, argv[1:])
        print(f"Ваша зароботная плата составила: "
              f"{(time_hours * rate + bonus) - ((time_hours * rate + bonus) * vat) / 100} руб.")
    except ValueError:
        print("Нужно ввести все 4 требуемых числовых параметра. Не используйте буквы и/или пробелы.")


wage()