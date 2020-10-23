path = 240

v= int(input("Vvedite ob'em benzobaka:"))

result = path /100
fuel = v - (result*12)

if fuel >1:
    print(f"Vy doehali do mesta nazna4eniya u vas ostalos': {round(fuel)} litr(a) benzina")
else:
    result = 100/12
    result1 = result * v
    print(f" u vas zakon4itsya benzin na {round(result)} kilometre!")
