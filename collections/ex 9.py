#Задача 9

n = int(input())
students = []

for _ in range(n):
    name, grade_str = input().split()
    students.append((name, int(grade_str)))

max_grade = -1
best_student = ""

for name, grade in students:

    if grade > max_grade:
        max_grade = grade
        best_student = name

print()
print(best_student)