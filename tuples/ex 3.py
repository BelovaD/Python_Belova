#Задача 3

n = int(input())
lines = [input() for _ in range(n)]
sorted_lines = sorted(lines)

print()

for line in sorted_lines:
    print(line)