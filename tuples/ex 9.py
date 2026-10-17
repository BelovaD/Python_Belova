#Задача 9

n = int(input())

people = []

for _ in range(n):
    line = input()
    last_name, height_str = line.split()
    height = int(height_str)
    people.append((height, last_name))

sorted_people = sorted(people, reverse=True)

print()

for height, last_name in sorted_people:
    print(f"{last_name} {height}")