username = 'user'
password = '12345'

def login(login,check_password):
    if username == login and password == check_password:
        print('Vy voshli v sistemu!')
    else:
        print('Ne vernye dannye')

login('user','12345') # eto vyzov funciyu bez nee ne vozmojno zaiti

