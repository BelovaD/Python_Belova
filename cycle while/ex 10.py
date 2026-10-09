#Задача 10

numb = int(input())
secret = int(42)

while numb != secret:
    if numb > 42:
        print('МЕНЬШЕ')
    elif numb < 42:
        print('БОЛЬШЕ')
    numb = int(input())
print('УГАДАЛ!')