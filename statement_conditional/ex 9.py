#Задача 9

print("Введите логин и email.")

login = input()
email = input()

if '@' in email and '@' not in login:
    print('OK')
else:
    print('ОШИБКА')