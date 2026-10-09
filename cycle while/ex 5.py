#Задача 5

password1 = input()
password2 = input()

if  password1 != password2:
    print("Пароли не совпадают!")

elif len(password1) < 8:
    print("Слишком короткий!")

else:
    print("OK")
