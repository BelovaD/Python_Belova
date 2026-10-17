#Задача 6

n = int(input())
student_scores = {}

for _ in range(n):
    name, score_str = input().split()
    score = int(score_str)

    if name not in student_scores:
        student_scores[name] = score
    else:
        student_scores[name] += score

print()

for name, total_score in student_scores.items():
    print(f"{name}: {total_score}")