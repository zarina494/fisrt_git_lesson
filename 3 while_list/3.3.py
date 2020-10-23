# isem znak 4isla
phone="0558573883"
email="user@name.com"
password="123456"

check_input=input ("phone or email: ") #vybiraem 4to vvodit

if check_input=="phone":
    phone_check=input("vvedite telefon:" )  #vvodim telefon
    password_check=input("vvedite parol:")
    if phone_check == phone and password_check == password:
        print("Vy vosli v sistemu!")
    else:
        print(" Vy vveli ne verno")
elif check_input == "email":
    email_check = input("vvedite email:")   # vvodim emal
    password_check = input("vvedite parol:")
    if email_check == email and password_check == password:
        print("Vy vosli v sistemu!")
    else:
        print(" Vy vveli ne verno")

    i