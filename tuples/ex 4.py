#Задача 4

n = int(input())
a, b = 1, 1

print()

for _ in range(n):
    print(a)
    a, b = b, a + b
