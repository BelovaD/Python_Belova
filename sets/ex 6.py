#Задача 6

m = int(input())
k = int(input())

all_lessons_students = set()
for _ in range(k):
    all_lessons_students.add(input())

for _ in range(m - 1):
    k = int(input())
    current_lesson_students = set()
    for _ in range(k):
        current_lesson_students.add(input())
    
    all_lessons_students &= current_lesson_students

for student in all_lessons_students:
    print(student)
