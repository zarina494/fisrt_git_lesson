student_list = ['zarina','emir','bayza', 'nazira']
current_list = []
i = 0
student_len = len(student_list)
come_in = 1
while come_in != '0':
    come_in = input('vvedite imya studenta:')
    if come_in not in current_list: #prishedshii
        if come_in in student_list:  # proveryaem
            current_list.append(come_in)  # dobavim studenta
            print('prishel')
        else:
            print('takogo studenta net')
    else:
        print('student uje prishol')
current_list_not = student_list
while i < len(current_list):
    if current_list[i] in current_list_not:
        current_list_not.remove(current_list[i])
    i += 1
print('Spisok prisutstvuyushih:', current_list)
print('spisok otsutstvuyushih:',current_list_not)