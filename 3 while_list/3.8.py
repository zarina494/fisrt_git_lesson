time = int(input())
breakfast = False
lunch = False
dinner = False
if 0<=time<24:
    if 8<=time<12:
        breakfast = True
        print(f"Zaftrak!{breakfast}", lunch, dinner)
    elif 12<=time<16:
        lunch = True
        dinner = True
        print(f"Ugin! {lunch}", dinner, breakfast)
    else:
        print("My ne rabotaem")
else:
    print("Vy s drugoi planety")

