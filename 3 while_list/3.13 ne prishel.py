score_list = []
score = 1
while score != 0:
    score = int(input('vvedite ocenku rebenka:'))
    if 0 < score <= 5:
        score_list.append(score_list)
        if score == 5:
            print('molodec!')
        elif score == 4:
            print('neploho')
        if score == 3:
            print('staraisya!')
        elif score == 2:
            print('poluchish')
        elif score == 1:
            print(';(((((')
    else:
        print('Nepravilnaya ocenka')
print(score_list)
summary = sum(score_list)
print(summary/len(score_list))