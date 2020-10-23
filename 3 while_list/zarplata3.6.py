hour_salary = 70
salary = 0      # na4alnaya zaplata
work = int(input("VVedite koli4estvo 4asov:"))

work_day = 8

if work > 1 and work <= 24:
    if work > work_day:
        check = work - work_day
        salary = (work_day * hour_salary) + ((check * hour_salary)*2)
        print(f"Vasha zarplata z segodnya: {salary}$")
    else:
        salary = hour_salary * work
        print(f"Vasha ZP za segodnya: {salary}")
else:
    print(" Vresh!")



