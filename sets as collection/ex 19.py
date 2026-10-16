#Задача 19

n = int(input())

for _ in range(n):
    line = input()
    
    if line.startswith("####"):
        continue
    elif line.startswith("%%"):
        print(line[2:])
    else:
        print(line)