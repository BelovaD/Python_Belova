#Задача 6

password1 = input()
password2 = input()

while (len(password1) < 8 or len(password2) < 8 or 
       '123' in password1 or '123' in password2 or 
       password1 != password2):
    
    if '123' in password1 or '123' in password2:
        print('Пароль содержит 123!')

    elif password1 != password2:
        print('Пароли не совпадают!')

    elif len(password1) < 8 or len(password2) < 8:
        print('Пароль слишком короткий!')
        
    password1 = input()
    password2 = input()

print('OK')