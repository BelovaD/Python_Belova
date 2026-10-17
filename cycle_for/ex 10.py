#Задача 10

n = int(input())

count = 0

for i in range(n):
    num = int(input())

    if i % 2 == 0:
        count += num
    else:
        count -= num

print(count)
