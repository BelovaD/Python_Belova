#Задача 11

n = int(input())
results = []

for _ in range(n):
    numbers = [int(x) for x in input().split()]
    
    if len(numbers) == len(set(numbers)):
        results.append("ДА")
    else:
        results.append("НЕТ")

print()
for answer in results:
    print(answer)
