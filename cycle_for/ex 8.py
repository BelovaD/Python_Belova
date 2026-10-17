#Задача 8

n = int(input())

mult = 1

for i in range(n):
    num = int(input())
    
    if num != 0:
        mult *= num

print(mult)
