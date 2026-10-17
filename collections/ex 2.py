#Задача 2

n = int(input())
grades_dict = {}

for _ in range(n):
    name, grade = input().split()
    grades_dict[name] = grade

print()

for name, grade in grades_dict.items():
    print(f"{name}: {grade}")
