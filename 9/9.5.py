list1 = [1,2,3,4]
def change_list(mode,number):
    if mode == 'remove':
         list1.remove(number)
    elif mode == 'add' and number in list1:
        list.append(number)
    else:
        print('Vy vveli nevernie dannie')


change_list('remove',1)
change_list('add',1)
print(list1)



