money = int(input("VVedite vasu summu"))

product_price = 3000

if money > product_price:
    result = money - product_price
    print(" Vasa sda4a", result)
elif money == product_price:
    print(" Spasibo za pokupku!")
else:
    print( "U vas ne dostato4no sredstv")