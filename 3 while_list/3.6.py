money = int(input("Vvedite vasu summu:"))

boots = 3000
wear = 4500
scarf = 900

product = input("Vvedite tovar dlya pokupki (boots wear scarf)")

if product == "boots":
    if money >= boots:
        print("spasibo")
    else:
        print("Nedostato4no sredtv")
elif product == "wear":
    if money >= wear:
        print("spasibo")
    else:
        print("Nedostato4no sredtv")
elif product == "scarf":
    if  money >= scarf:
        print("spasibo")
    else:
        print("Nedostato4no sredtv")