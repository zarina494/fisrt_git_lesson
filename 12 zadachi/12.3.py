import random
product_list = ['asus','acer','iphone','samsung','intel hd',
                'nvidia','adata','kingston','macbook','xiomi',
                'iMac','amd','apacer']
def register(login,password,check_password):
    register_list = []
    if password == check_password:
        code = random.sample([1,2,3,4,5,6,7,8,9,0],4)
        register_list.append(login)
        register_list.append(password)
        return register_list
    else:
        return 'Nepravelnye dannie'

user = (register('user','123456','123456'))
username = user[0]
password = user[1]
print(username,password)

def check_login(login,password):
    if username == login and password == password:
        print('Vy voshli v sistemu!')
    else:
        print('Nepravelnye dannye!')
check_login('user','123456')

def write_to():
    file1 = open('product_list.txt', 'w')
    for product in product_list:
        file1.write(product + '\n')
write_to()
#5


def write_product(product_list):
    with open('product_list.txt', 'w') as file1:
        for product in product_list:
            file1.write(product + '\n')

write_product(product_list)

def sort_list(product_list):
    with open('product_list.txt', 'w') as file2:
        f2 = file2.readlines()
        for product in f2:
            if product == 'asus' or product == 'acer' or product == 'macbook' or product == 'iMac':
                file1 = open('computers.txt','w')
                file1.write(product)

            elif product == 'iphone' or product == 'samsung':
                file2 = open('phones.txt,', 'w')
                file2.write(product)
            elif product == 'intel_hd' or product == 'nvidia' or product == 'amd':
                file3 = open('video cart.txt', 'w')
                file3.write(product)
            elif product == 'adata' or product == 'kingston' or product == 'apacer':
                file4 = open('jestkii_diski.txt', 'w')
                file4.write(product)
sort_list(product_list)












