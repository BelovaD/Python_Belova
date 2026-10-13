#Задача 1

is_found = False
for i in range(5):
    text = input()
    if 'кот' in text or 'Кот' in text:
        is_found = True
if is_found:
    print('МЯУ')
else:
    print('Кот не найден')
