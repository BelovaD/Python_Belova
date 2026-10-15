#Задача 9

m = int(input())

all_dishes = []
for i in range(m):
    dish = input()
    all_dishes.append(dish)

n = int(input())

cooked_dishes = set()

for i in range(n):
    line = input()
    words = line.split()
    
    for dish in words:
        cooked_dishes.add(dish)

for dish in all_dishes:
    if dish not in cooked_dishes:
        print(dish)
