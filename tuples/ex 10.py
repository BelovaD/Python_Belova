#Задача 10

n = int(input())
result_tuples = []

for _ in range(n):
    line = input()
    result_tuples.append((len(line), line))

print()

for t in result_tuples:
    print(t)
