products = {'gucci boots': 10000, 'channel': 20000, 'adidas boots': 8000,
            'nike sport-suit': 23000, 'gucci sport-suit': 24000,
            'Lonsdale suit': 8000, 'nike boots': 9000,
            'dior chest': 10000, 'raben waist': 15000,
            'wedding dress': 500000}

user = 'user'
password = 'user123456'


def check_login(login, password):
    if len(login) < 20 and user == login and password == password and not password.isalpha() and not password.isdigit():

        print('Vy voshli v sistemu!')
    else:
        print('Nepravelnye dannye!')


check_login('user', 'user123456')


def counter(money, price):
    if money > price:
        money = money - price
        return money
    else:
        return 'Ne dostatochno sredst!'

def cart():
    cart_list = []
    for i in range(3):
        product = input('Vvedite nazvanie tovara: ')
        if product in products:
            cart_list.append(product)
    return cart_list


test_cart = cart()
def wallet(money):
    test_cart1 = []
    for line in test_cart:
        if money >= products[line]:
            money = counter(money, products[line])
            test_cart1.append(line)

    return {'4to ya hotel kupit:':test_cart1, 'Konechniy vybor:': test_cart, 'Sdacha:':money}


print(wallet(50000))