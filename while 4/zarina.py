bmw = 20
merc = 18
fit = 9
fuel = int(input("Запрвьте авто:"))
i =0
while i <3:
    auto = input("Введите наименования авто для тестирования:")
    result= 0
    final = 0
    path = 240
    if auto == "bmw":
        result = path / 100
        result = bmw * result  # кол литров расхода поезки на Ы-К
        final = fuel - result
        if final >0:
            print(f'После поездки остаток:{final} литров')
        else:
            result = 100 // bmw # расход 1 литров на км
            result = result * fuel
            path = path - result
            print(f"(Вам осалось ехать: {round(path)}км ")
    elif auto == "merc":
        result = path / 100
        result = merc * result  # кол литров расхода поезки на Ы-К
        final = fuel - result
        if final > 0:
            print(f"(После поездки остаток: {final} литров")
        else:
            result = 100 // merc  # расход 1 литров на км
            result = result * fuel
            path = path - result
            print(f"(Вам осалось ехать: {round(path)}км")
    elif auto == "fit":
        result = path / 100
        result = fit * result  # кол литров расхода поезки на Ы-К
        final = fuel - result
        if final > 0:
            print(f"После поездки остаток: (round{final}) литров")
        else:
            result = 100 // fit  # расход 1 литров на км
            result = result * fuel
            path = path - result
            print(f"(Вам осалось ехать: {path} км")
