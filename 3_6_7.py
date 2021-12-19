def reg_func(syllable):
    latin_letters = 'abcdefghijklmnopqrstuvwxyz'
    return syllable.title() if not set(syllable).difference(latin_letters) else False


string = input('Введите слова на латинице, разделяя их пробелами:\n').split()
for v in string:
    result = reg_func(v)
    if result:
        print(reg_func(v), ' ')