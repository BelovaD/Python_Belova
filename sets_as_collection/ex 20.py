#Задача 20

username = input()
allowed = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
is_valid = True

for char in username:
    if char not in allowed:
        print(f"Неверный символ: {char}")
        is_valid = False
        break

if is_valid:
    print("OK")