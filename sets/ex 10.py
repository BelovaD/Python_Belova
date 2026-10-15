#Задача 10

line1 = input().split()
set1 = set()
for n in line1:
    set1.add(int(n))

line2 = input().split()
set2 = set()
for n in line2:
    set2.add(int(n))

result = set1 ^ set2

if len(result) == 0:
    print("EMPTY")
else:
    list = sorted(result)
    
    for n in list:
        print(n, end=" ")
