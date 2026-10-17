#Задача 8

words = input().lower().split()
word_counts = {}

for word in words:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

print()

for word, count in word_counts.items():
    print(f"{word}: {count}")
