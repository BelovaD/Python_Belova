# Задача 5

password1 = input()
password2 = input()

if len(password1) < 8:
    print("Слишком короткий!")

elif password1 != password2:
    print("Пароли не совпадают!")

else:
    print("OK")
