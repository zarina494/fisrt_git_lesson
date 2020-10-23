day_plan = ['eat','walk','study','sleep']
plan_len = len(day_plan)
i = 0 # s4et4ik
while i < plan_len:
    action = input('Vvedite plan deistviya:')
    if action in day_plan:
        act_index = day_plan.index(action) # nahodim index nashego deistviya
        if act_index == 0: # deistvie v preoritete
            day_plan.remove(action)  # delo sdelano vy4erkivaem iz deistviya
            i += 1
        else:
            print('Ne zaplanirovannye dela')
    else:
        print('Vy eto ne planirovali!')
    print(f'ostavshiesya dela{day_plan}')

