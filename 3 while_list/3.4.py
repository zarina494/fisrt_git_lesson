number = int(input())

magic_number1 = 5
magic_number2 = -5

if number > 0:
    if number == magic_number1:
        print("yes")
    else:
        print("no")
elif number < 0:
    if number == magic_number2:
        print("yes")
    else:
        print("no")