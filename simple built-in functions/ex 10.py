#Задача 10

numb1 = int(input())
numb2 = int(input())
operation = input()

if operation == '+':
    print(numb1 + numb2)
elif operation == '-':
    print(numb1 - numb2)
elif operation == '*':
    print(numb1 * numb2)
elif operation == '/':
    if numb1 == 0 or numb2 == 0:
        print('ОШИБКА')
    else:
        print(numb1 / numb2)
else:
    print('ОШИБКА')
