import random
file1 = open('players.txt','w')
for i in range(4):
    cost = random(2,11) + random.randint(2,11)
    check = input(f'Vasha ruka: {cost} Nujna eshe karta? Da ili net')
    if check == 'da':
        cost = cost + random.randint(2,11)
    elif check == 'Net':
        cost = cost
    else:
        print('Otvet to4no')
    cards.append (cost)
print(cards)
i = 0
while i < len(cards):
    if cards [i] > 21:
        cards [i] = 0
    i +=1
max_cost= max(cards)
max_index = cards.index(max_cost)
winner = players_list[max_index]
print(f'Vstre4aite pobeditelya!{winner}')


