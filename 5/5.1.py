sum_km = 10
wait = 2
path = int(input('Put:'))
cost = 40
wait_status = input('Voditel ojidaet:')
come_status = input('Klient jdet:')
i = 1
while come_status != 'True':
    cost = cost + wait
    i = i + 1
    come_status = input('Klient jdet:')
cost = cost + (path * sum_km)
print(cost)