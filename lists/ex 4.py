#Задача 4

n = int(input())
lines = [input() for _ in range(n)]

print(*lines[::-1], sep='\n')