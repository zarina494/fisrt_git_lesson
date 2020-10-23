product_list = ['bread','cheese','egg','meat']
# buterbrod 0+1
# biphsteks 2+3
# gamburger 0+2+3
# 4isburger 0+1+2+3
cook_list = []
print('U vas imeyutsya takie produkty:', product_list)
product = input('Vozmte product:')
i = 0
while product != '0' and i <= len(product_list):
    if product in product_list:
        cook_list.append(product)
    else:
        print('Ispolzuyte producty s tarelki!')
    product = input('Vozmit product:')
    i += 1
j = 0
butter = ['bread', 'cheese']
biff = ['meat', 'egg']
ham = [' bread', 'egg', 'meat']
ch_ham =  [' bread', 'cheese', 'egg', 'meat']
#product1 =[]
#product2= []
#product13 =[]
#product4 = []
if len(cook_list) == len(butter):
    j = 0
    while j < len(cook_list):
        if cook_list[j] in butter:
            j += 1
        else:
            print('vy dali mne ne vernyi product:')
            break
    if j == len(butter):
        print('Vy mojete prigotovit buter')
elif len(cook_list) == len(ham):
    j = 0
    while j < len(cook_list):
        if cook_list[j] in biff:
            j += 1
        else:
            print('vy dali mne ne vernyi product:')
            break
    if j == len(biff):
        print('Vy mojete prigotovit buter')
elif len(cook_list) == len(cook_list):
    j = 0
    while j < len(cook_list):
        if cook_list[j] in ham:
            j += 1
        else:
            print('vy dali mne ne vernyi product:')
            break
    if j == len(ham):
        print('Vy mojete prigotovit buter')
elif len(cook_list) == len(cook_list):
    j = 0
    while j < len(cook_list):
        if cook_list[j] in ch_ham:
            j += 1
        else:
            print('vy dali mne ne vernyi product:')
            break
    if j == len(ch_ham):
        print('Vy mojete prigotovit buter')