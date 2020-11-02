list1 = [1,1,1,1,1,2,2,3,3,5,5,6]
print(list1)
def count_list(number):
    j=0
    for list_number in list1:
        if list_number == number:
            j+=1
    print(j)
count_list(1)
