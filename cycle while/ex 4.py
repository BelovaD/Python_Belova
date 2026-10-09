#Задача 4

password1 = input()
password2 = input()

while (len(password1) < 8 or len(password2) < 8 or 
       len(password1) > 20 or len(password2) > 20 or 
       password1 != password2):
    
    if len(password1) < 8 or len(password2) < 8:
        print('Пароль слишком короткий!')
    elif len(password1) > 20 or len(password2) > 20:
        print('Пароль слишком длинный!')
    elif password1 != password2:
        print('Пароли не совпадают!')
        
    password1 = input()
    password2 = input()

print('OK')
