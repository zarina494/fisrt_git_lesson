user_db = ''
password_db = ''
def register(username,password,repeat_password):
    if password == repeat_password:
        user_db = username
        password_db = password
        return user_db,password_db
    else:
        return 'Paroli ne sovpadaut!'

print(register('zarina','123456','1234567'))
