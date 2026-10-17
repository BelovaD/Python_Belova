#Задача 4

n = int(input())
lines = [input() for _ in range(n)]
sorted_lines = sorted(lines, key=lambda s: (len(s), s))

print()

for line in sorted_lines:
    print(line)
