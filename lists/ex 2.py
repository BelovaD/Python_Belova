#Задача 2

n = int(input())
lines = [input() for _ in range(n)]
query = input()

for line in lines:
    if query in line:
        print(line)