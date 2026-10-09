#Задача 4

numb = float(input())

while numb != 0:
    if numb > 28:
        print('ЖАРКО')
    elif numb < 15.5:
        print('ХОЛОДНО')
    else:
        print('НОРМАЛЬНО')
    numb = float(input())