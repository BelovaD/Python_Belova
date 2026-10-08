#Задача 4

text = input()
if 'кот' in text and 'собака' not in text:
    print('МЯУ')
elif 'собака' in text and 'кот' not in text:
    print('ГАВ')