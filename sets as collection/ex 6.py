#Задача 6

text = input()
index = int(input())

if 1 <= index <= len(text):
    print(text[index - 1])
else:
    print("ОШИБКА")