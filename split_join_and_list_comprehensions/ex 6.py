#Задача 6

n = int(input())
food_lines = []

for _ in range(n):
    line = input()
    if "лук" not in line:
        food_lines.append(line)

print()
print(", ".join(food_lines))
