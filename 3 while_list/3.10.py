username_list = []
password_list = []
i = 1
while i <= 2:
    username = input('Vvedite imya polzovatelya:')
    password = input('Vvedite parol:')
    username_list.append(username)
    password_list.append(password)
    print(f'Polzovatel pod nomerom {i} zaregistripovan')
    i = i + 1
print(username_list)
print(password_list)