#Задача 3

n = int(input())
numbers = [int(input()) for _ in range(n)]
sums = []

for i in range(n - 1):
    pair_sum = numbers[i] + numbers[i + 1]
    sums.append(pair_sum)

print(*sums)