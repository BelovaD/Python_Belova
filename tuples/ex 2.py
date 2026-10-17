#Задача 2

n = int(input())
students = []

for _ in range(n):
    line = input()
    last_name, grade_str = line.split()
    grade = int(grade_str)
    students.append((last_name, grade))

print()

for last_name, grade in students:
    print(f"{last_name} {grade}")

print()

for last_name, grade in students:
    if grade == 4 or grade == 5:
        print(f"{last_name} {grade}")
