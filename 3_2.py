def trainee_info(name, birthday, city, email, phone, qr_code):
    return f"Ф.И.О.: {name}; Дата рождения: {birthday}; Город проживания: {city};" \
           f" email: {email}; Номер телефона: {phone}; QR код: {qr_code}."

print(trainee_info(name = input("Введите Имя, Отчество и Фамилию студента через пробел: ").split(),
      birthday = input("Введите дату рождения студента в формате ДД.ММ.ГГГГ: "),
      city = input("Введите город проживания студента: "), email = input("Введите email студента: "),
      phone = input("Введите номер телефона студента: "), qr_code = input("Введите QR код студента: ")))