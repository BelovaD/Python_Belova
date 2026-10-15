#Задача 7

n = int(input())

all_names = []
for _ in range(n):
    all_names.append(input())

duplicates = set()

for name in all_names:
    if all_names.count(name) > 1:
        duplicates.add(name)

count = 0
for name in all_names:
    if name in duplicates:
        count += 1

print(count)

