list1 = [1,2,3,4,5,6]
def change_list(mode,number):
    if mode == 'remove':
        list1.remove(number)
    elif mode == 'add' and number in list1:
        list1.append(number)
    elif mode == 'pop':
        list1.pop(number)
    else:
        print('Vy vveli nevernie mod')

change_list('remove',1)
change_list('add',1)
change_list('pop',2)
print(list1)