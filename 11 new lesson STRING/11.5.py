string = 'sdobrymutrombishkek'
if string.istitle() and len(string)<10:
    string = string.upper()
    print(string)
elif string.istitle() and len(string)<10:
    string = string.lower()
    print(string)
elif len(string)>10:
    string= string.capitalize()
    print(string)

