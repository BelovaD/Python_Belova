#Задача 8

n = int(input())
results = []

for _ in range(n):
    a, b = map(int, input().split())
    results.append((min(a, b), max(a, b)))

print()

for lesser, greater in results:
    print(f"{lesser} {greater}")
