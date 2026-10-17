#Задача 6

n = int(input())
numbers = [int(input()) for _ in range(n)]

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print()

for num in numbers:
    print(num)