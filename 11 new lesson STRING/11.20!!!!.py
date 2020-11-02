# 22.	В форме интернет-магазина пользователю нужно ввести свой номер телефона.
# Номер телефона состоит из 10 цифр, однако некоторые пользователи вводят его в формате
# +996558588086, некоторые - 996550588086, а некоторые и вовсе вводят только 9 цифр (без первой) 558588086.
# Вам необходимо привести номер к стандарту +996558588086
phone = input()
if phone.startswith('996'):
    phone = '+'+ phone
    print(phone)
elif phone.startswith('+996'):
    print(phone)
elif not phone.startswith('+996') and not phone.startswith('0') and len(phone) < 9:
    phone = '+996'+phone
    print(phone)
else:
    print('Vvedite pravelnye dannye!')






