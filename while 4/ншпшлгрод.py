user_name = "Maksim"
password = "123456"
i = 0
while i < 5:
    login = input("Введите имя пользователя:")
    check_passord = input ("Введите пароль:")
    if login == user_name and check_passord == password:
        print("Вы вошди в систему!")
        break
    else:
        print("Вы ввели неверные данные!")
        i = i + 1
