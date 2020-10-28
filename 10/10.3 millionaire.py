def millionaire():
    answer_list = ['shekspir','pushkik','bunin','bulgakov']
    true_answer = 'bulgakov'
    print('Otvette na vopros: Kto napisal Master i Margarita?')
    print('Varianty otvetov:',answer_list)
    help = input('Nujny varianty podskazki?')
    if help == 'da':
        poll = input('U vas 3 podskazki: 50/50,zvonok drugu,pomosh zala')
        if poll == '5050':
            for i in range(2):
                if answer_list[i] != true_answer:
                    answer_list.remove(answer_list[i])
            print(answer_list)
            my_answer = input('Vvedite svoi otvet:')
            if my_answer == true_answer:
                return 'Pravelnyi otvet'

            else:
                'Vy otvetili ne verno'

        elif poll == 'pomosh zala':
            help_list = []
            for i in range(6):
                help_list = input('Vvedite pomosh zala:')
                help_list.append(true_answer)
            print(help_list)
            my_answer = input('vvedite svoi otvet:')
            if my_answer == true_answer:
                return 'Vy pobedili'
            else:
                return 'Ne verniy otvet'
        elif poll == 'Zvonok drugu:':
            call_answer = input('Vvedite otvet na vopros:')
            print(call_answer)
            my_answer = input('Vvedite svoi otvet:')
            if my_answer == true_answer:
                return'Vypobedili'
            else:
                return 'Ne verno'
        else:
            print('Vvedite da ili net')

print(millionaire())