#Задача 2

numb = int(input())

result = "" 

while numb != 0:
    result = result + str(numb) + " " 
    numb = int(input())

print(result)