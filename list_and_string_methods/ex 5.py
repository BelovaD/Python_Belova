#Задача 5

n = int(input())
clean_lines = []

for _ in range(n):
    line = input()
    code_part = line.split('#')[0]
    cleaned = code_part.rstrip()
    if cleaned:
        clean_lines.append(cleaned)

print()

for line in clean_lines:
    print(line)