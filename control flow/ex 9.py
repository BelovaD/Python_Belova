#Задача 9

n = int(input())
count = 0

for i in range(n):
    num = int(input())
    if num <= 0:
        continue
    count += num

print(count)