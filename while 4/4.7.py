numbers = [1,'red', 2,3,'yellow', 12.4,[7, 11.5]]
int_list = []
float_list = []
str_list = []
i = 0
while i < len(numbers):
    if isinstance(numbers[i], str):
        str_list.append(numbers[i])
    elif isinstance(numbers[i],float):
        float_list.append(numbers[i])
    else:
        int_list.append(numbers[i])
    i += 1
print(f'Obshii spisok{numbers}')
print(f'Spisok soderjasii stroki:{str_list}')
print(f'Spisok soderjasii celye 4isla:{int_list}')
print(f'Spisok soderjasii drobnye 4isla:{float_list}')