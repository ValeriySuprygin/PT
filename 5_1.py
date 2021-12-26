writer_autodidact = open('5_1.txt', 'w', encoding='utf-8')

string = " "
while string:
    string = input("Ну, напишите что хотели: ")
    writer_autodidact.write(f"{string}\n") if string != "" else writer_autodidact.close()