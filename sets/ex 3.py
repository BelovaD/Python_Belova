#Задача 3

set1 = set()
set2 = set()

while True:
    line = input().strip()
    if line == "":
        break
    set1.add(int(line))

while True:
    line = input().strip()
    if line == "":
        break
    set2.add(int(line))

sets = set1 & set2

if sets:
    print(*(sets))
else:
    print("EMPTY")