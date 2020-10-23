taxi_za_4as = 10
ojidanie = 0
oplata = ojidanie + taxi_za_4as
proezd = int(input("k oplate:"))


if ojidanie >= 0:
    ojidanie = taxi_za_4as - oplata
    plata = ojidanie + taxi_za_4as
    print(plata)
elif ojidanie:
    print(proezd)
