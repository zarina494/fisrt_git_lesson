 #  Дан список строк(письма пришедшие на почту). Требуется написать: функцию которая будет
# записывать строки в файл, каждая новая строка начинается с новой строки, функцию которая
# будет считывать содержимое файла, все строки которые относятся к спаму, следует записывать
# в новый файл(пример: строка начинается: «Buy right now!», «Sales», строки которые содержат
# имя пользователя – «Emma» , но не содержатся слова с мольбами о помощи нужно добавить в
# другой файл, строки где содержатся слова “help” или “SOS” или начинаются с “Dear” нужно
# добавить в другой файл. Добавление файлов и создание начальных функций закончено!
strings = ['hello Emma, how are u?',
           'Dear Emma, please fix production',
           'SALES lining sales','buy right now dont lose your chance',
           'Emma help me please','Emma SOS production is down']

def write_to():
    with open('mail.txt','w') as file1:
        for mail in strings:
            file1.write(mail.lower() + '\n')
write_to()
def mail_check():
    with open('mail.txt') as file1:
        f1 = file1.readlines()
        for spam in f1:
            if spam.startswith('buy right now!') or spam.startswith('sales'):
                file2 = open('spam.txt','a')
                file2.write(spam+ '\n')
            elif spam.startswith('dear') or 'sos' in spam or 'help' in spam:
                file3 = open('work.txt','a')
                file3.write(spam+ '\n')
            else:
                file4 = open('my_mail.txt', 'a')
                file4.write(spam+ '\n')

print(mail_check())
















mail_box = []
