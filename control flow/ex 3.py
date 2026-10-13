#Задача 3

cat_index = -1
line_number = 0

while True:
    text = input()
    
    if text == "СТОП":
        break
        
    line_number += 1
    
    if ("кот" in text or "Кот" in text) and cat_index == -1:
        cat_index = line_number

print(cat_index)
