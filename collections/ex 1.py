#Задача 1

word = input()
char_counts = {}

for char in word:
    if char not in char_counts:
        char_counts[char] = 1
    else:
        char_counts[char] += 1

print()

for char, count in char_counts.items():
    print(f"{char}: {count}")
